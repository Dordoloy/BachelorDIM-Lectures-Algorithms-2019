# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 09:10:55 2019

@author: dordoloy
"""

import os
import pika
import config
import getpass

def callback(ch, method, properties, body):
        print(" [X] %r" % body)
        
        
def read_subscriber():
    
    amqp_url=config.amqp_url
    
    # Parse CLODUAMQP_URL (fallback to localhost)
    url = os.environ.get('CLOUDAMQP_URL',amqp_url)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    
    properties = pika.BasicProperties()
    
    channel = connection.channel()
    channel.exchange_declare(exchange='posts',
                             exchange_type='fanout')
    
    result= channel.queue_declare(exclusive=True,
                                  queue = '')
    
    queue_name = result.method.queue 
    
    channel.queue_bind(exchange='posts',
                       queue = queue_name)
    
    channel.basic_consume(queue=queue_name,
                          on_message_callback=callback,                          
                          auto_ack=True)
    channel.start_consuming()

read_subscriber()