# RabbitMQ Task Scheduler

To run the **producer** and **consumer** in this Dockerized RabbitMQ project, follow these steps from the project’s root directory (`RabbitMQ_task_scheduler/`):

## 1. Build All Services

Before running, build the Docker images:

```bash
docker-compose build
```

## 2. Start the Project

To start RabbitMQ, the producer, and the consumer as specified in `docker-compose.yml`:

```bash
docker-compose up
```

- This will:
  - Start RabbitMQ,
  - Start the consumer container (listening for messages),
  - Start the producer container (will send a message and then exit).

## 3. Sending More Messages from the Producer

The producer script is set to send a message and exit, you can trigger it again with:

```bash
docker-compose run --rm producer
```

- This command runs a one-off producer container that sends another message to RabbitMQ.
- Run this command as many times as you want to send additional messages.

## 4. Observing the Consumer

- The consumer container will output received messages in the terminal where you ran `docker-compose up`.
- The consumer keeps running, waiting for new messages.

## 5. Checking RabbitMQ UI

Open a new browser tab and go to:

```
http://localhost:15672
```
- Credentials: **user:** guest  **password:** guest
- You can view queues, messages, and activity.

**Summary:**  
- Build with `docker-compose build`
- Start everything with `docker-compose up`
- Send additional producer messages with `docker-compose run --rm producer`
- Consumer output will appear in the terminal