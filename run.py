"""Routes for the youtube search.
"""

from flask import Flask
import data

app = Flask(__name__)

# Import the API routes
from routes.youtube import *

# Required because app is imported in other modules
if __name__== '__main__':
    app.run(debug=True)
