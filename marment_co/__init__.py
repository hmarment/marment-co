# # -*- coding: utf-8 -*-

# from __future__ import with_statement, print_function, absolute_import

# import os

# from flask import Flask
# from flask import render_template
# from flask_cors import CORS
# from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow

# # Define the WSGI application object
# app = Flask(__name__,
#             static_folder="../client/dist/static",
#             template_folder="../client/dist")

# # Load config for current environment (Development / Production)
# app.config.from_object(os.environ['CONFIG_PROFILE'])

# # enable CORS
# CORS(app)

# # Create the SqlAlchemy db instance
# db = SQLAlchemy(app)

# # Initialize Marshmallow
# ma = Marshmallow(app)

# # # Sample HTTP error handling
# # @app.errorhandler(404)
# # def not_found(error):
# #     return render_template('404.html'), 404

# # # Import a module / component using its blueprint handler variable (mod_auth)
# # from app.mod_auth.controllers import mod_auth as auth_module

# # # Register blueprint(s)
# # app.register_blueprint(auth_module)
# # # app.register_blueprint(xyz_module)
# # # ..

# # # Build the database:
# # # This will create the database file using SQLAlchemy
# # db.create_all()
