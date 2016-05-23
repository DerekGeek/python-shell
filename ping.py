#!/usr/bin/python
import threading
import re
import subprocess
import sys,Queue
from icmp_packet import Icmp
global outqueue
outqueue=Queue.Queue()
class Ping(threading.Thread):
    def __init__(self,queue,lock):
        threading.Thread.__init__(self)
        self.queue=queue
        self.lock=lock
    def run(self):
       source_ip='192.168.157.132'
       dest_ip=self.queue.get()
       if self.lock.acquire():
          Ping=Icmp()
          data=Ping.ping(source_ip,dest_ip)
#       outqueue.put(data+','+dest_ip)
          if data!='Nothing':
              if (ord(data[20]))==0 and (ord(data[21]))==0:
                  sys.stdout.write('%s is reachable \n' % dest_ip)
              else:
                  sys.stdout.write('%s is not reachable \n' % dest_ip)
          else:    
              sys.stdout.write('%s is not reachable \n' % dest_ip)
       self.lock.release()
       self.queue.task_done()

      
