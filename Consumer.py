import json

import pika, sys, os


def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f'Consumer {data}/{properties}')


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.177.75'))
    channel = connection.channel()
    channel.queue_declare(queue='MainQueue', durable=True)

    channel.basic_consume(queue='MainQueue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
