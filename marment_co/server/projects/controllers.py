# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

from flask import make_response, abort
from server import db
from server.projects.models import GithubProject, GithubProjectSchema

# Define the blueprint: 'auth', set its url prefix: app.url/auth
# mod_auth = Blueprint('auth', __name__, url_prefix='/auth')

def read_all():
    """
    This function responds to a request for /api/github/list
    with the complete lists of Github Projects

    :return:        json string of list of github project
    """
    # Create the list of people from our data
    project = GithubProject.query \
        .order_by(GithubProject.created_at.desc()) \
        .all()

    # Serialize the data for the response
    project_schema = GithubProjectSchema(many=True)
    return project_schema.dump(project).data
