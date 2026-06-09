import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=pika.PlainCredentials("admin", "admin123")))
channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print("Received %r" % body)

channel.basic_consume(on_message_callback=callback, queue='hello', auto_ack=True)

print("Waiting for response...")
channel.start_consuming()
connection.close()