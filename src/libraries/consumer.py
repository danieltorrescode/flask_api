import pika, json

# params = pika.URLParameters('amqp://rabbitmq:123@rabbitmq:5672//')
# connection = pika.BlockingConnection(params)
params= pika.ConnectionParameters('rabbitmq', 5672, '/', pika.PlainCredentials('rabbitmq', '123'))
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare(queue='broker_test')


def callback(ch, method, properties, body):
    print('Received')
    print(method)
    print(properties)
    print(body)


channel.basic_consume(queue='broker_test', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
