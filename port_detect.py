#!/usr/bin/python
import threading
from checkable import Checking
import Queue
import sys
import time
class Port_Check(threading.Thread):
    def __init__(self,queue,port='23'):
        threading.Thread.__init__(self)
        self.queue=queue
        self.port=port

    def run(self):
        ip=self.queue.get()
        check=Checking(ip,self.port)
	result=check.connecting()
	if result:
           sys.stdout.write('Connection to %s on port %s successfully\n' % (ip,self.port))
	else:
           sys.stdout.write('Connection to %s on port %s failed!\n' % (ip,self.port))
	self.queue.task_done()
if __name__=='__main__':
   queue=Queue.Queue()
   queue.put('192.168.157.132')
   A=Telnet_Check(queue)
   A.start()
   queue.join()
