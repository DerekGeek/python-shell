#!/usr/bin/python
import ConfigParser,re,threading
#from ssh_show import SSH_SHOW
from ssh_execute import SSH_EXECUTE
from telnet_execute import TELNET_EXECUTE
from Queue import Queue
class Read_Show_Conf(threading.Thread):
      def __init__(self,queue,file,savedir):
          threading.Thread.__init__(self)
	  self.queue=queue
	  self.con_file=file
	  self.save_dir=savedir
      def run(self):
          try:
               data=self.queue.get()
               cf=ConfigParser.ConfigParser()
	       cf.read(self.con_file)
               for section in cf.sections():
                   dic=dict(cf.items(section))
		   if dic['method']=='ssh' and dic['producer']=='cisco':
                       ssh_execute=SSH_EXECUTE(ip=data,username=dic['username'],password=dic['password'],enable_password=dic['enable_password'],enable='enable',savedir=self.save_dir) 
		       #print 'Conf_t',ssh_execute.conf_t()
		       if ssh_execute.login()==0 and ssh_execute.prelogin()==0:
		           for command in dic['commands'].split(','):
                               ssh_execute.send_commands(command)
		   elif dic['method']=='ssh' and dic['producer']=='h3c':
                       ssh_execute=SSH_EXECUTE(ip=data,username=dic['username'],password=dic['password'],enable_password=dic['enable_password'],enable='sys',savedir=self.save_dir) 
		       #print 'Conf_t',ssh_execute.conf_t()
		       if ssh_execute.login()==0 and ssh_execute.prelogin()==0:
		           for command in dic['commands'].split(','):
                               ssh_execute.send_commands(command)
		   elif dic['method']=='telnet' and dic['producer']=='cisco':
                       ssh_execute=TELNET_EXECUTE(ip=data,username=dic['username'],password=dic['password'],enable_password=dic['enable_password'],en='enable',savedir=self.save_dir) 
		       #print 'Conf_t',ssh_execute.conf_t()
		       if ssh_execute.login()==0 and ssh_execute.prelogin()==0:
		           for command in dic['commands'].split(','):
                               ssh_execute.send_commands(command)
		   elif dic['method']=='telnet' and dic['producer']=='h3c':
                       ssh_execute=TELNET_EXECUTE(ip=data,username=dic['username'],password=dic['password'],enable_password=dic['enable_password'],en='sys',savedir=self.save_dir) 
		       #print 'Conf_t',ssh_execute.conf_t()
		       if ssh_execute.login()==0 and ssh_execute.prelogin()==0:
		           for command in dic['commands'].split(','):
                               ssh_execute.send_commands(command)
	       self.queue.task_done()
          except KeyError:
	       print 'Config file error!'
	       self.queue.task_done()
	       return False
	  return True
if __name__=='__main__':
    queue=Queue()
    queue.put('1.1.1.1')
    queue.put('192.168.234.253')
    for i in range(2):
        A=Read_Show_Conf(queue,'show.conf')
        A.start()
    A.queue.join() 
