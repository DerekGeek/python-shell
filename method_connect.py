#!/usr/bin/python
from input_test import Input
from read_config import Read_Show_Conf 
from Queue import Queue
import os,time
from spin  import Spinning
import spin,subprocess
class Method_Connect:
      def do_ls(self,args):
          result=subprocess.Popen('ls %s' % args ,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
          stdout,stderr=result.communicate()
          if stdout:
	     print stdout
	  else:
	     print stderr
      def do_connect(self,args):
          try:
             arg=args.split()
             if arg[-1]=='show':
                self.cisco_show()
	     elif arg[-1]=='display':
	        self.h3c_display()
	  except IndexError:
	        print 'no index'
      
      def cisco_show(self):
          A=Input()
	  path=raw_input('Please input the Config file path:')
          savedir=raw_input('print the save dir:')
	  if os.path.isfile(path) and os.path.isdir(savedir):
	      while True:
                answer=raw_input('print the scanning ip method ,Usage list or file or exit :')
		if answer=='list':
	  	    if A.Input():
                       spin.boolean=False
		       Spin=Spinning()
		       Spin.start()
		       for i in range(A.number):
		           B=Read_Show_Conf(A.queue,path,savedir)
		           B.start()
		       A.queue.join()
		    if A.queue.empty():
		       spin.boolean=True
		       print 'scanning done!'
		elif answer=='file':
		    if A.Input_file():
                       spin.boolean=False
		       Spin=Spinning()
		       Spin.start()
		       for i in range(A.number):
		           B=Read_Show_Conf(A.queue,path,savedir)
			   B.start()
		       A.queue.join()
		    if A.queue.empty():
		        spin.boolean=True
			print 'scanning done!'
	        elif answer=='exit':
		    break
                else:
		    print 'Input error'
          else:
	      print 'file %s does not exists or save dir %s  does not exists' % (path,savedir)

      def h3c_display(self):
          A=Input()
	  path=raw_input('Please input the Config file path:')
          savedir=raw_input('print the save dir:')
	  if os.path.isfile(path) and os.path.isdir(savedir):
	      while True:
                answer=raw_input('print the scanning ip method ,Usage list or file or exit :')
		if answer=='list':
	  	    if A.Input():
                       spin.boolean=False
		       Spin=Spinning()
		       Spin.start()
		       for i in range(A.number):
		           B=Read_Show_Conf(A.queue,path,savedir)
		           B.start()
		       A.queue.join()
		    if A.queue.empty():
		       spin.boolean=True
		       print 'scanning done!'
		elif answer=='file':
		    if A.Input_file():
                       spin.boolean=False
		       Spin=Spinning()
		       Spin.start()
		       for i in range(A.number):
		           B=Read_Show_Conf(A.queue,path,savedir)
			   B.start()
		       A.queue.join()
		    if A.queue.empty():
		        spin.boolean=True
			print 'scanning done!'
	        elif answer=='exit':
		    break
                else:
		    print 'Input error'
          else:
	      print 'file %s does not exists or save dir %s  does not exists' % (path,savedir)


