import json
import os
import random
import sys
import time

import pika


def main():
    channel = connection.channel()
    channel.queue_declare(queue='MainQueue', durable=True)
    ind = 0
    while True:
        ind = ind + 1
        info = {"info": "msg", "value": ind}

        channel.basic_publish(exchange='',
                              routing_key='MainQueue',
                              body=json.dumps(info),
                              properties=pika.BasicProperties(content_type='application/json', delivery_mode=2)
                              )
        print(f"Producer '{json.dumps(info)}'")
        time.sleep(random.randint(1, 5))


if __name__ == '__main__':
    print(' [*] Waiting for messages. To exit press CTRL+C')
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.177.75'))
        main()
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    finally:
        connection.close()
