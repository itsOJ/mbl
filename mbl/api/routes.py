"""
    Register routes for the app
"""

from flask import Blueprint
from flask_restful import Api
from mbl import resources as r
from mbl.utils.response import ERRORS


v1 = Blueprint('v1', __name__)
api = Api(v1, catch_all_404s=True, errors=ERRORS)
add = api.add_resource


# Add routes here
add(r.All, '/all')                                      # GET

