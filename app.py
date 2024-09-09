from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///rockpaperscissors.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Configure cache
app.config["CACHE_TYPE"] = "SimpleCache"  # Use simple cache for demonstration
app.config["CACHE_DEFAULT_TIMEOUT"] = 300  # Cache timeout in seconds (5 minutes)

cache = Cache(app)  # Initialize the cache
CORS(app)  

db = SQLAlchemy(app)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run()