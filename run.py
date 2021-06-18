"""Routes for the youtube search.
"""

from flask import Flask

app = Flask(__name__)

# Import the API routes
#from routes.youtube import *
from utils.utils import search_and_insert
# Required because app is imported in other modules
if __name__== '__main__':
    search_and_insert("cricket")
    #app.run(debug=True)
