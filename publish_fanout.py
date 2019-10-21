# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:47:08 2019

@author: dordoloy
"""

import os
import pika
import config
import getpass


def publish_fanout():
    
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
    channel.basic_publish(exchange='posts',
                          routing_key='',
                          body='message')
    print("send")

publish_fanout()