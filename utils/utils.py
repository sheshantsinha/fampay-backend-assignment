import os
from datetime import datetime
from dbutils.dbutils import MysqlDb
from dbutils.queries import sql_query
from utils.youtube import youtube_search
import time

SLEEPTIME = 10
APIINDEX = 0
api_keys = os.environ.get('APIKEY').split(",") if "APIKEY" in os.environ else None

def build_sql_query(rows):
    values = ', '.join(map(str, rows))
    sql_query = "INSERT INTO temp_youtube_results (video_id, video_publish_date, video_title, video_discription, video_thumbnail) VALUES {}".format(values)
    return sql_query

def search_youtube_data(keyword, max_results, page_token):
    global APIINDEX
    result, next_page_token, change_key = youtube_search(api_keys[APIINDEX], keyword, max_results, page_token)
    if change_key:
        APIINDEX = APIINDEX + 1 if APIINDEX + 1 < len(api_keys) else 0
        result = []
        next_page_token = None
    return result, next_page_token

def execute_sql_query(query):
    obj = MysqlDb()
    obj.create_database()
    obj.create_table()
    obj.execute_command(query)
    obj.execute_command(sql_query)
    #obj.execute_command("delete from temp_youtube_results")
    #obj.mydb.close()

def execute_sql_query_to_select(query):
    obj = MysqlDb()
    obj.create_database()
    obj.create_table()
    result = obj.select_values(query)
    return result

def get_count_of_records(table_name="youtube_results"):
    results = execute_sql_query_to_select("select count(*) from {}".format(table_name))
    return results[0][0]

def search_and_insert(keyword, cron=True):
    global SLEEPTIME
    current_max_result = 10
    next_page_token = None
    if not cron:
        rows, next_page_token = search_youtube_data(keyword, current_max_result, next_page_token)
        if len(rows) > 0:
            query = build_sql_query(rows)
            execute_sql_query(query)
    else:
        offset = 0#get_count_of_records()
        while True:
            print("*********Sleeping for {} seconds************".format(SLEEPTIME))
            time.sleep(SLEEPTIME)
            rows, next_page_token = search_youtube_data(keyword, offset+current_max_result, next_page_token)
            if len(rows) == 0:
                print("all videos are populated")
                SLEEPTIME += 20
                next_page_token = None
            else:
                query = build_sql_query(rows)
                execute_sql_query(query)
                current_max_result+=10

