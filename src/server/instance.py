import os
from flask import Flask
from flask_restx import Api
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from src.server.instance import server
from src.controllers.home import *
# from src.controllers.auth import *

server.run()
from src.libraries.celery_init_app import celery_init_app
load_dotenv('.env')

class Server():
    def __init__(self, ):
        self.app = Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
        self.db = SQLAlchemy(self.app)

        self.app.config.from_mapping(
            CELERY=dict(
                broker_url="redis://localhost",
                result_backend="redis://localhost",
                task_ignore_result=True,
            ),
        )
        self.app.config.from_prefixed_env()
        self.celery_app = celery_init_app(self.app)
        self.api = Api(
            self.app,
            version='1.0',
            title='flask',
            description='API',
            doc='/docs'
        )


    def run(self, ):
        self.app.run(
            debug=True,
            host='0.0.0.0',
            port='8088',
        )


server = Server()
server.celery_app