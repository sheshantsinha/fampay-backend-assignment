"""Routes for the course resource.
"""

from run import app
from flask import request
from flask import jsonify
from http import HTTPStatus
from utils.utils import get_count_of_records, execute_sql_query_to_select

@app.route("/videos/<int:page>", methods=['GET'])
def get_paginated_videos(page):
    """Get videos per page.

    :param int page: certain video per page.
    :return: all stored videos in a batch of X records
    :rtype: object
    """
    total_records = get_count_of_records()
    records_per_page = 10
    raw_total_pages = total_records/records_per_page
    total_pages = raw_total_pages if raw_total_pages%1 == 0 else int(total_records/records_per_page)+1 
    if page <1 or page > total_pages:
        return "Invalid page number"
    record_offset = (page-1)*records_per_page
    result = execute_sql_query_to_select("select * from youtube_results order by video_publish_date desc limit {}, {} ".format(record_offset, records_per_page))
    response = {
        "result": result
    }
    return response


@app.route("/videos/search", methods=['GET'])
def get_searched_videos():
    print(request.args)
    """Search video in db using querykey as title and description".

    Query parameters: title, description
    :return: all searched query
    :rtype: object
    """
    query = request.args.get('query')
    searchby = request.args.get('searchkey')
    if not query or not searchby:
        return "Invalid"
    if searchby not in ["video_title", "video_discription"]:
        return 
    sql_query = "select * from youtube_results where {}='{}'".format(searchby, query)
    result = execute_sql_query_to_select(sql_query)
    response = {
        "result": result
    }
    return response

@app.route("/videos/anon/search", methods=['GET'])
def get_searched_anon_videos():
    print(request.args)
    """Search video in db using querykey as title and description".

    Query parameters: title, description
    :return: all searched query
    :rtype: object
    """
    query = request.args.get('query')
    if not query:
        return "Invalid"
    sql_query = "select * from youtube_results where video_title LIKE '%{}%' OR video_discription LIKE '%{}%'".format(query, query)
    result = execute_sql_query_to_select(sql_query)
    response = {
        "result": result
    }
    return response