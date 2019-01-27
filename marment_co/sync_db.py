# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

import os
from server import db
from server.projects.models import GithubProject
from server.ext import github

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
projects = github.list_github_projects()
for project in projects:
    p = GithubProject(name=project.name, description=project.description)
    db.session.add(p)

db.session.commit()
