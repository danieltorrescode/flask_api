from celery import shared_task
from celery.contrib.abortable import AbortableTask

from time import sleep

@shared_task(bind=True, base=AbortableTask)
def run_counter(self, form_data):
    for i in range(10):
        print(i)
        sleep(1)
        if self.is_aborted():
            return 'TASK STOPPED!'
    return 'DONE!'

@shared_task
def twenty_seconds():
    print("RUNNING EVERY 20 SECONDS!")