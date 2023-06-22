from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import string
import random

from src.server.instance import server

app, api = server.app, server.api
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://db_user:db_password@0.0.0.0:3306/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return 'User>>> {self.username}'