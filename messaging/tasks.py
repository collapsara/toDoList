from celery import Celery
import pika

app = Celery('tasks', backend='amqp', broker='amqp://')


@app.task(ignore_result=True)
def send_message(task_id):
    mb = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = mb.channel()
    channel.basic_publish(exchange='', routing_key='tasks_status', body='Task #{0} is done.'.format(task_id))
    channel.close()
