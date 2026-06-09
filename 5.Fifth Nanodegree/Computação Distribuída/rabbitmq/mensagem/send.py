import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=pika.PlainCredentials("admin", "admin123")))
channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(100):
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World')

print("Sent 'Hello World'")
connection.close()