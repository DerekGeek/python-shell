#!/usr/bin/python
import ConfigParser,re
from ssh_cisco_show import SSH_SHOW
from ssh_cisco_execute import Cisco

cf=ConfigParser.ConfigParser()
cf.read('execute.conf')

for section in cf.sections():
    dic=dict(cf.items(section))
    ssh_execute=Cisco(ip='192.168.234.253',username=dic['username'],password=dic['password'],enable_password=dic['enable_password']) 
    ssh_execute.conf_t()
    ssh_execute.send_commands(dic['commands'])
