from flask import Flask
from src.config.database import db 
from src.blueprints.home.home import home_blueprint 
from src.libraries.celery_init_app import celery_init_app

app = Flask(__name__)
app.config.from_pyfile('settings.py')
app.register_blueprint(home_blueprint)
db.init_app(app)

app.config.from_mapping(
    CELERY=dict(
        broker_url=app.config['BROKER'],
        result_backend=app.config['BACKEND'],
        task_ignore_result=True,
    ),
)
app.config.from_prefixed_env()
celery_app = celery_init_app(app)

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port='8088',
    )