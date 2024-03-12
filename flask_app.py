from flask import Flask, request
import git


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello from Flask and Github!'


@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('https://github.com/GuilhermeFaga/DSWA5-flask')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400