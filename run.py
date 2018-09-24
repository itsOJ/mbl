"""
    Runs flask server
"""
import os
from mbl import create_app

environment = os.getenv('FLASK_ENV')
app = create_app(environment)


if __name__ == "__main__":
    app.run()
