#!/usr/bin/python
import re,cmd,sys,re,time
from method_detect import Method_Detect
from method_connect import Method_Connect
#from init_help_tab import Params
from init_help_tab_1 import Params
class CLI(cmd.Cmd):
    def __init__(self):
        '''
        Set the default prompt when this cli is starting
	'''
        cmd.Cmd.__init__(self)
	self.prompt="Derek(me)#"
        self.intro="Welcome to derek's shell,version 1.0"
	self.method=Method_Detect()
	self.method_connect=Method_Connect()
        self.params=Params() 
    def completedefault(self,text,line,begid,endidx):
        match=self.params.completedefault(text,line,begid,endidx)
	return match
    def do_hostname(self,args):
        self.prompt=args+'#'
    def help_hostname(self):
        self.params.help_hostname()
    def help_detect(self):
        self.params.help_detect()
    def help_connect(self):
        self.params.help_connect() 
    def help_by(self):
        self.params.help_by()
    def help_checking(self):
        self.params.help_checking()
    def help_cisco(self):
        self.params.help_cisco()
    def help_h3c(self):
        self.params.help_h3c()
    def emptyline(self):
         pass
    def do_detect(self,args):
        self.method.do_detect(args)	
    def do_ls(self,args):
        self.method_connect.do_ls(args)
    def do_connect(self,args):
        self.method_connect.do_connect(args)
 
    def do_quit(self,line):
        print 'Bye,I will miss you!'
        return True
if __name__=='__main__':	
    cmd=CLI()
    cmd.cmdloop()
