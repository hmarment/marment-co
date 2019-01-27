# -*- coding: utf-8 -*-

from __future__ import with_statement, print_function, absolute_import

from datetime import datetime
from sqlalchemy import func
from server import db, ma


class GithubProject(db.Model):
    __tablename__ = "github_project"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255))
    description = db.Column(db.String(length=255))
    created_at = db.Column(db.DateTime, default=func.now())
    last_modified_at = db.Column(db.DateTime,
                                 onupdate=func.utc_timestamp())


class GithubProjectSchema(ma.ModelSchema):
    class Meta:
        model = GithubProject
        sqla_session = db.session
