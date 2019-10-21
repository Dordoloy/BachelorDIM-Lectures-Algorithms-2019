# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:38:30 2019

@author: dordoloy
"""

import os
import pika
import config
import time


count = 0

def callback(ch, method, properties, body):
    ##
    #Function that print the received message and count the number of message received
    #Args:
    #   @param ch
    #   @param method
    #   @param properties
    #   @param body
    #Returns nothing
    global count
    count += 1
    print("[{0}] Received %r".format(count) % body)
    #print('[x] message Processed, acknowledging (to delete the message from queue)')
    ch.basic_ack(method.delivery_tag)

def sleep_callback(ch, method, properties, body):
    ##
    #Function that print the received message and count the number of message received
    #Args:
    #   @param ch
    #   @param method
    #   @param properties
    #   @param body
    #Returns nothing
    global count
    count += 1
    time.sleep(0.5)
    print("[{0}] Received %r".format(count) % body)
    #print('[x] message Processed, acknowledging (to delete the message from queue)')
    ch.basic_ack(method.delivery_tag)
    
    
def simple_queue_read(concurrecy, sleep = False):
    ##
    #Function that publish a message
    #Args:
    #   @param concurrency
    #   @param sleep
    #Returns nothing
    amqp_url=config.amqp_url
    
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    channel = connection.channel()
    channel.queue_declare(queue='presentation')
    
    if sleep:
        channel.basic_consume(queue='presentation',
                              on_message_callback=sleep_callback,                          
                              auto_ack=False)
    else:
        channel.basic_consume(queue='presentation',
                              on_message_callback=callback,                          
                              auto_ack=False)
        
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

