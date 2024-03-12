from flask import Flask, request
from git import Repo
import traceback


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask and Github!'


@app.route('/update_server', methods=['POST'])
def webhook():
    try:
        repo = Repo('./mysite')
        git = repo.git
        git.checkout('main')
        git.pull()
        return 'Updated PythonAnywhere successfully', 200
    except Exception as e:
        return traceback.format_exc(), 500