# # -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

from flask import render_template

from server import app
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
    return ', '.join([project.name
                     for project in github.list_github_projects()])
