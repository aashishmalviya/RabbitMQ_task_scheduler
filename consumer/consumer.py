import pika


def main():
    # Connect to RabbitMQ service defined in Docker Compose ('rabbitmq' host)
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq'))
    channel = connection.channel()

    # Declare durable queue
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        try:
            message = body.decode()
            print(f"Received: {message}")

            # Simulate message processing; replace with your real task here
            # For example: process_data(message)

            # Acknowledge message only after processing succeeds
            ch.basic_ack(delivery_tag=method.delivery_tag)

        except Exception as e:
            print(f"Error processing message: {e}")
            # Reject and requeue message for retry
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=True)

    # consume messages with manual ack
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print('Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Consumer interrupted")
        channel.stop_consuming()
    finally:
        connection.close()


if __name__ == "__main__":
    main()
