import pika
import time
from random import randrange

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=pika.PlainCredentials("admin", "admin123")))
channel = connection.channel()

channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print("Received %r" % body)
    time.sleep(randrange(0,5))
    print("Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_message_callback=callback, queue='hello')

print("Waiting for response...")
channel.start_consuming()

connection.close()