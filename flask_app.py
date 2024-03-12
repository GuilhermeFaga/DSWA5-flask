from flask import Flask, request
from git import Repo
from dotenv import load_dotenv

from .check_signature import is_valid_signature

import traceback
import os


load_dotenv('./.env')


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask and Github!'


@app.route('/update_server', methods=['POST'])
def webhook():
    try:
        GITHUB_WEBHOOK_TOKEN = os.getenv("GITHUB_WEBHOOK_TOKEN")
        x_hub_signature = request.headers.get('X-Hub-Signature')

        if x_hub_signature is None:
            return 'Missing X-Hub-Signature', 400
        
        if not x_hub_signature.startswith('sha1='):
            return 'Invalid X-Hub-Signature', 400
        
        if not is_valid_signature(x_hub_signature, request.data, GITHUB_WEBHOOK_TOKEN):
            return 'Invalid X-Hub-Signature', 400
        
        repo = Repo('./mysite')
        git = repo.git
        git.checkout('main')
        git.pull()
        return 'Updated PythonAnywhere successfully', 200
    except Exception as e:
        return traceback.format_exc(), 500