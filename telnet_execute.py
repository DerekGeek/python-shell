#!/usr/bin/python
__metaclass__=type

import pexpect
import socket
import sys
import time
class TELNET_EXECUTE:
    ret=0
    def __init__(self,username,ip,password,enable_password,en,savedir=None):
        self.username=username
	self.ip=ip
	self.password=password
	self.en=en
	self.enable_password=enable_password
	self.savedir=savedir
	self.prelogin()
        self.login()
    
    def prelogin(self): 
        try:
	    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((self.ip,22)) 
	    s.settimeout(5)
	except socket.error:
	    self.ret=-6
        #    print 'Can not connect'
	    s.close()
	s.close()
        return self.ret
    def login(self):
        class password_error(Exception):pass
        self.ssh=pexpect.spawn('telnet "%s" ' % self.ip)
        try:
	   username_index=self.ssh.expect('sername:')
	   self.ssh.sendline(self.username)
         #  print 'Username sent'
           index=self.ssh.expect(['assword:','continue connecting(yes/no)?'],timeout=5)
         #  print 'Connecting'
           if index==0:
	      self.ssh.sendline(self.password)
	 #     print 'First Password sent'
	   else:
	      self.ssh.sendline('yes\n')
	      self.ssh.expect('assword:')
	      self.ssh.sendline(self.password)
         #     print 'Second Password sent'
	   password_error_index=self.ssh.expect(['assword:','#','>'])
	   if password_error_index==0:
	      raise password_error
	   elif password_error_index==1:
	      pass
	 #     print 'Do not need enable password,already in # Mode'
	 #     print 'Got #'
	   else:
	      if self.en=='enable':
                  self.enable(self.en)

	except password_error:
	 #   print 'Password error' 
	    self.ssh.close()
	    self.ret=-1
        except pexpect.EOF:
         #   print 'EOF'
	    self.ssh.close()
	    self.ret=-2
	except pexpect.TIMEOUT:
	 #   print 'Time out'
	    self.ssh.close()
	    self.ret=-3
        return self.ret

    def enable(self,enable_command):
        class enable_password_error(Exception):pass
	try:
	     self.ssh.sendline(enable_command)
	     enable_index=self.ssh.expect(['assword:',']'])
	     if enable_index==0:
	         self.ssh.sendline(self.enable_password)
	  #       print 'Sending enable password'
	         result=self.ssh.expect(['#','assword:'])
	         if result==0:
	             pass
	  #          print 'Got #'
	         else:
	            raise enable_password_error
             else:
	         pass
	  #      print 'Got ]'
        except enable_password_error:
             print  'Enable password error!'
	     self.ssh.close()
	     self.ret=-4
	except pexpect.TIMEOUT:
	     self.ssh.close()
	     self.ret=-7
        return self.ret

    def conf_t(self):
        class conf_t_error(Exception):pass 
	try:
	   self.ssh.sendline('config t\n')
	   result=self.ssh.expect(['.*\(config\)#','authorization failed.'])
           if result==0:
	      pass
	      
	     # print 'Conf t Authorization success'
	   else:
	      raise conf_t_error
	except conf_t_error:
	    self.ret=-5
	    
           # print 'Conf t Authorization failure!'
        return self.ret
    def send_commands(self,command):
        try:
	    self.ssh.sendline(command+'\n'+' '*150)
	    f=open(self.savedir+'/'+self.ip,'a+')
            self.ssh.logfile=f
	    self.ssh.expect(pexpect.EOF)
	    f.close()
	except pexpect.TIMEOUT:
	    pass
	return True
if __name__=='__main__':
    A=SSH_EXECUTE(username='weizhicong',password='!QAZ2wsx',ip='10.202.7.188',enable_password='!QAZ5tgb',en='enable',savedir='/root/python/savedir')
    #A.conf_t()
    A.send_commands('show run')
