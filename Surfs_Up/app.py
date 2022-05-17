## dependencies
from flask import Flask
## create Flask app instance
app = Flask(__name__)
## create Flask routes
@app.route('/')
def hello_world():
    return 'Hello world'

