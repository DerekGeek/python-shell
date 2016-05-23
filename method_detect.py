#!/usr/bin/python
from input_test import Input
from ping import Ping
from port_detect import Port_Check
import re,subprocess,sys,time,threading,Queue
import ping
class Method_Detect:
    def emptyline(self):
        pass

    def do_detect(self,args):
       try:
           arg=args.split()
	   if arg[-1]=='by':
	      pass
	   elif arg[-1]=='checking':
	      pass
	   elif arg[-1]=='ip_list':
	      self.ip_list()
	   elif arg[-1]=='ip_file':
	      self.ip_file()
           elif arg[-1]=='telnetable_ip_list':
	      self.check_telnet()
           elif arg[-1]=='telnetable_ip_file':
	      self.file_check_telnet()
	   elif arg[-1]=='sshable_ip_list':
	      self.check_ssh()
	   elif arg[-1]=='sshable_ip_file':
	      self.file_check_ssh()
       except IndexError:
           print 'no index'
    def check_telnet(slef):
        A=Input()
	if A.Input():
	    for i in range(A.number):
	        B=Port_Check(A.queue)
	        B.start()
	    A.queue.join()
        else:
	  pass
    def check_ssh(self):
        A=Input()
	if A.Input():
	    for i in range(A.number):
	        B=Port_Check(A.queue,'22')
	        B.start()
	    A.queue.join()
        else:
	    pass
    def ip_list(self):
        A=Input()
	lock=threading.Lock()
	outqueue=Queue.Queue()
	if A.Input():
            for i in range(A.number):
                B=Ping(A.queue,lock)
                B.start()
            A.queue.join()
        else:
	   pass

    def ip_file(self):
        A=Input()
	lock=threading.Lock()
	outqueue=Queue.Queue()
	if A.Input_file():
            for i in range(A.number):
	        B=Ping(A.queue,lock)
	        B.start()
            A.queue.join()
        else:
	   pass
    def file_check_telnet(self):
        A=Input()
        if A.Input_file():
	    for i in range(A.number):
	        B=Telnet_Check(A.queue)
	        B.start()
	    A.queue.join()
	else:
	    pass
	print 'Done!'

    def file_check_ssh(self):
        A=Input()
	if A.Input_file():
	    for i in range(A.number):
	        B=Telnet_Check(A.queue,'22')
	        B.start()
	    A.queue.join()
	else:
	    pass
	print 'Done!'

if __name__=='__main__':
   cmd=Method()
   cmd.cmdloop()
