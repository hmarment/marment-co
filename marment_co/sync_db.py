# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

import os
from server import db
from server.ext import github
from server.projects.models import GithubProject

# Flush database first
db.drop_all()

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
projects = github.list_my_github_projects()
for project in projects:
    p = GithubProject(
        id=project.id,
        name=project.name,
        description=project.description,
        homepage=project.homepage,
        language=project.language,
        created_at=project.created_at)
    db.session.add(p)

db.session.commit()
