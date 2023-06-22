from flask import Blueprint
from src.libraries.tasks import run_counter
from datetime import datetime, timedelta
home_blueprint = Blueprint("home", __name__)

@home_blueprint.route("/home")
def home():
    return '<h1>Home</h1>'


@home_blueprint.route("/counter")
def counter():
    task = run_counter.apply_async(args=({"key":"value"},), eta=datetime.utcnow() + timedelta(minutes=1))
    # task = run_counter.delay({"key":"value"})
    return '<h1>Home</h1>'
