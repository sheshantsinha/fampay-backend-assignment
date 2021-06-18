"""Routes for the course resource.
"""

from run import app
from flask import request
from flask import jsonify
from http import HTTPStatus

@app.route("/videos/<int:page>", methods=['GET'])
def get_paginated_videos(page):
    """Get videos per page.

    :param int page: certain video per page.
    :return: all stored videos in a batch of X records
    :rtype: object
    """
    pass


@app.route("/videos/search", methods=['GET'])
def get_searched_videos():
    query_keyword = request.args.get('querykey')
    """Search video in db using querykey as title and description".

    Query parameters: title, description
    :return: all searched query
    :rtype: object
    """
    pass