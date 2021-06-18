"""Routes for the youtube search.
"""
from flask import Flask
from utils.utils import search_and_insert
import threading
import os

TOPIC = os.environ.get('TOPIC')

app = Flask(__name__)

# Import the API routes
from routes.api import *
# Required because app is imported in other modules

if __name__== '__main__':
    t1 = threading.Thread(target=search_and_insert, args=(TOPIC,False,))
    t1.start()
    t1.join()
    t2 = threading.Thread(target=search_and_insert, args=(TOPIC,))
    t2.start()
    app.run(debug=True)
