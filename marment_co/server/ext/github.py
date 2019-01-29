# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

import os

from github import Github
from server import app

g = None

def init_github():
    """
    Initialise Github API client
    """
    global g
    if not g:
        g = Github(app.config.get('GITHUB_API_KEY'))#)os.environ['GITHUB_API_KEY'])

def list_github_projects():
    """
    Retrieve all projects from Github API
    """
    init_github()
    global g
    me = g.get_user()
    github_projects = me.get_repos()
    return [project for project in github_projects]

def list_my_github_projects():
    """
    Retrieve all projects from Github API written by me
    """
    init_github()
    global g
    me = g.get_user()
    github_projects = me.get_repos()
    return [project for project in github_projects
            if project.owner.id == me.id
            and not project.fork]
