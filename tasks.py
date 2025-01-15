from celery import Celery
import time

app = Celery("tasks", backend="rpc://", broker="pyamqp://guest@localhost//")


@app.task
def add(x, y):
    return x + y

@app.task
def add__slow(x, y):
    time.sleep(15)
    return x + y