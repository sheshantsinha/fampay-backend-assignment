from youtube_api import YouTubeDataAPI
import os
from datetime import datetime
from dbutils.dbutils import MysqlDb
from dbutils.queries import sql_query
import time

SLEEPTIME = 10
api_key = os.environ.get('APIKEY') if "APIKEY" in os.environ else None

def format_youtube_result(data):
    rows = []
    for element in data:
        row = (
            element["video_id"],
            datetime.fromtimestamp(element["video_publish_date"]).strftime("%Y-%m-%d %H:%M:%S"),
            element["video_title"],
            element["video_description"],
            element["video_thumbnail"]
        )
        rows.append(row)
    
    return rows

def build_sql_query(rows):
    values = ', '.join(map(str, rows))
    sql_query = "INSERT INTO temp_youtube_results (video_id, video_publish_date, video_title, video_discription, video_thumbnail) VALUES {}".format(values)
    return sql_query

def search_youtube_data(keyword, max_results=10):
    yt = YouTubeDataAPI(api_key)
    result = yt.search(keyword, max_results=max_results)
    return result

def execute_sql_query(query, create_table=True):
    obj = MysqlDb()
    obj.create_database()
    if create_table:
        obj.create_table()
    obj.execute_command(query)
    obj.execute_command(sql_query)
    obj.execute_command("delete from temp_youtube_results")
    obj.mydb.close()

def execute_sql_query_to_select(query, create_table=True):
    obj = MysqlDb()
    obj.create_database()
    if create_table:
        obj.create_table()
    result = obj.select_values(query)
    return result

def get_count_of_records(table_name="youtube_results"):
    results = execute_sql_query_to_select("select count(*) from {}".format(table_name), False)
    return results[0][0]

def search_and_insert(keyword, cron=True):
    current_max_result = 10
    if not cron:
        result = search_youtube_data(keyword, max_results=current_max_result)
        rows = format_youtube_result(result)
        query = build_sql_query(rows)
        execute_sql_query(query)
    else:
        offset = get_count_of_records()
        while True:
            print("*********Sleeping for {} seconds************".format(SLEEPTIME))
            time.sleep(SLEEPTIME)
            result = search_youtube_data(keyword, max_results=offset+current_max_result)
            rows = format_youtube_result(result)
            query = build_sql_query(rows)
            execute_sql_query(query, False)
            current_max_result+=10

