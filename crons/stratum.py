#!/usr/bin/env python

import socket
import json
import time
import math

class Stratum(object):

    def __init__(self, host, port):
	self.host = host
	self.port = port
	self.timeout = 2
	self.connect()

    def connect(self):
	try:
	   self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    	   self.socket.connect((self.host, self.port))
	   return self.socket
	except Exception as e:
	   raise e

    def close(self):
	self.socket.close()
	return None

    def get_shares(self, username):
	message = {'id': 1, 'method': 'mining.get_shares', 'params': [username] }
	return self.send_message(message)

    def ping(self):
	message = {'id': 1, 'method': 'ping', 'params': [] }
	return self.send_message(message)

    def send_message(self, message):
	response = json.dumps(message) + "\n"
	self.socket.sendall(response)
	data = self.recv_timeout()
	return data

    def recv_timeout(self):
	self.socket.setblocking(0)
	total_data=[];
	data='';
     
    	begin=time.time()
    	while 1:
           if total_data and time.time()-begin > self.timeout:
              break
         
           elif time.time()-begin > self.timeout*2:
              break
         
           try:
               data = self.socket.recv(8192)
               if data:
                  total_data.append(data)
                  begin=time.time()
               else:
                  time.sleep(0.1)
           except:
               pass
     
        return ''.join(total_data)
	


