import os

from flask import Flask
from flask import render_template
from flask_cors import CORS

from github import Github

app = Flask(__name__,
            static_folder="../client/dist/static",
            template_folder="../client/dist")
app.config.from_object(os.environ['CONFIG_PROFILE'])

# enable CORS
CORS(app)

github = None

def init_github():
    """
    Initialise Github API client
    """
    global github
    if not github:
        github = Github(app.config.get('GITHUB_API_KEY'))

# entry point for Vue front-end
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello, Jub!'


@app.route('/api/github/list')
def list_github_projects():
    init_github()
    global github
    me = github.get_user()
    github_projects = me.get_repos()
    return ', '.join([project.name for project in github_projects])


if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'))

