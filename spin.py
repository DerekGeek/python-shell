#!/usr/bin/python
import threading,sys
import time
import os
global boolean
boolean=False

class Spinning(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self) 
       
    def run(self):
	start=0
	step=1
	leng=10
        try:
            while not boolean:
                if start<=leng and step!=-1:
                   start+=step
	           time.sleep(1)
                elif start>leng or start >=0:
                   step=-1
                   start+=step
	           time.sleep(1)
                elif start<0:
                   start=0
                   step=1
                sys.stdout.write('\r'+'scanning:'+'*'*start+' ')
	        sys.stdout.flush()
	    sys.stdout.write(' ')
        except KeyboardInterrupt:
                raise
