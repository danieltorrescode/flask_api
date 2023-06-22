# from src.libraries.celery_init_app import celery_init_app
from src.server.instance import server

app, celery_app = server.app, server.celery_app

server.celery_app