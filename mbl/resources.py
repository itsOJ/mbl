"""
    Flask RestFul resources
"""

import json

from flask_restful import Resource, reqparse
from flask import current_app as app

from .utils import errors


class All(Resource):
    """
        All Resource
    """

    def __init__(self):
        pass

    def get(self):
        """
            Returns:
                All database items
        """

        return {'data': 'ALL'}, 200
