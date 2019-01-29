# # -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

from flask import render_template, jsonify

from server import app, projects
# from server.projects import routes
from server.ext import github

# entry point for Vue front-end
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello, Jub!'


@app.route('/api/github/list')
def list_github_projects():
    # read from database
    github_projects = projects.controllers.read_all()
    app.logger.debug(github_projects)
    return jsonify(github_projects)
