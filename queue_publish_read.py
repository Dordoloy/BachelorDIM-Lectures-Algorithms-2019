# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:52:36 2019

@author: dordoloy
"""


import argparse
import simple_queue_read as read
import simple_queue_publish as publish

parser = argparse.ArgumentParser('Publish or Read on presentation queue')
parser.add_argument('-p', '--publish', action='store_true')
parser.add_argument('-r', '--read', action='store_true')
parser.add_argument('-c', '--concurrency', action='store_true')
parser.add_argument('-n', '--number', type=int, default=1)
parser.add_argument('-s', '--sleep', action='store_true')
args = parser.parse_args()

if (args.publish):
   publish.simple_queue_publish(args.concurrency, args.number)

if (args.read):
   read.simple_queue_read(args.concurrency, args.sleep)
   
