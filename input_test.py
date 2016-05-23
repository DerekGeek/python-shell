#!/usr/bin/python
import Queue
import subprocess
import re
import sys
class Input:
   queue=Queue.Queue()
   pattern=re.compile('^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
   number=0
   starti=''
   endi=''
   def Input(self):
       class inputSignalError(Exception): pass
       class itemError(Exception):pass
       try:
           list=raw_input('Please input ip list:') 
	   if '-' in list:
	       result_list=list.split('-')
               if len(result_list)==1: 
	          raise inputSignalError
	       elif len(result_list)!=2:
	          raise inputSignalError
	       else:
	          for item in result_list:
		     if not self.pattern.match(item):
		         raise itemError
	          self.starti=result_list[0].split('.')[-1]
		  self.endi=result_list[1].split('.')[-1]
		  for i in range(int(self.starti),int(self.endi)+1):
		      self.queue.put(('.').join(result_list[0].split('.')[:-1])+'.'+str(i))
		  self.number=int(self.endi)-int(self.starti)+1
	   else:
	       matched_list=[]
	       result_list=list.split(',')
               if  len(result_list)==1 and not self.pattern.match(result_list[0]):
	          raise inputSignalError
	       else:
	          for i in result_list:
		      if not self.pattern.match(i):
		          raise itemError
		      else:
	                  matched_list.append(i)
		  for i in matched_list:
		      self.queue.put(i)
               self.number=len(result_list)
       except inputSignalError:
           print 'The Pattern is like this:ip1,ip2,ip3.....Or 10.10.10.1-10.10.10.254'
	   return False
       except itemError:
           print 'The item is Wrong.You must input like this:10.10.10.10'
	   return False

       return True   


   def Input_file(self):
       class itemError(Exception):pass
       path=raw_input('Please input the file path:')
       matched_list=[]
       try:
           file=open(path,'r') 
	   lines=file.readlines()
	   for number,line in enumerate(lines):
	       if not self.pattern.match(line):
	          raise itemError
	       else:
	          matched_list.append(line)
	   for ip in matched_list:
	       self.queue.put(ip.strip(','))
	   self.number=len(matched_list)
       except IOError:
           print 'file does not exist!'
	   return False
       except  itemError:
           print 'Pattern error at line:',number+1
	   return False
       file.close()
       return True
if __name__=='__main__':
    A=Input()
    bool=A.Input()
    if not bool:
       pass
    else:
        print 'success'
