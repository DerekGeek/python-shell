#!/usr/bin/python
__metaclass__=type
import socket
import threading
import sys
class Checking:
   ip=''
   port=''
   def __init__(self,ip,port):
       self.ip=str(ip)
       self.port=int(port)
       self.connecting()
   def connecting(self):
       try:
           s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	   s.settimeout(1)
           s.connect((self.ip,self.port))    
	   return True
	   s.close()
	   sys.exit(0)
       except socket.error:
	   return False
           s.close()
	   sys.exit(2)
if __name__=='__main__':
    A=Checking('10.228.63.6','22')
    result=A.connecting()
    if result==True:
        print 'yes'
    else:
        print  'no'
