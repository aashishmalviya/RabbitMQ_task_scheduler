import pika


def main():
    # Connect to RabbitMQ service defined in Docker Compose ('rabbitmq' host)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Declare durable queue
    channel.queue_declare(queue='task_queue', durable=True)

    message = 'Hello RabbitMQ! This message is persistent and durable.'

    # Publish persistent message
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2  # make message persistent
        )
    )
    print(f"Sent: {message}")

    connection.close()


if __name__ == "__main__":
    main()
