from youtube_api import YouTubeDataAPI
import os
from datetime import datetime
from dbutils.dbutils import MysqlDb
from dbutils.queries import sql_query

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

def execute_sql_query(query):
    obj = MysqlDb()
    obj.create_database()
    obj.create_table()
    obj.execute_command(query)
    obj.execute_command(sql_query)
    obj.execute_command("delete from temp_youtube_results")

def search_and_insert(keyword):
    result = search_youtube_data(keyword, max_results=10)
    rows = format_youtube_result(result)
    query = build_sql_query(rows)
    #return 
    execute_sql_query(query)
    #copy_data_from_temp_table()
