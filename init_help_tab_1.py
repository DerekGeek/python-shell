#!/usr/bin/python
import re

class Params:
    detect={'by':['ip_list','ip_file'],'checking':['telnetable_ip_list','telnetable_ip_file','sshable_ip_list','sshable_ip_file']}
    connect={'using':['telnet','ssh'],'cisco':['show','execute'],'h3c':['display','execute']}
    all=['detect','connect','by','checking','ip_list','ip_file','telnetable_ip_list','telnetable_ip_file','sshable_ip_list','sshable_ip_file','using','telnet','ssh','cisco','h3c','show','display','excute','ls']

    def completedefault(self,text,line,begidx,endidx):
        tokens=line.split()
	while len(tokens)>2:
	    tokens.pop(0)
	if tokens[0].strip() in self.all:
	    return self.match_reg(tokens[0].strip(),text)
	return []
     
    def match_reg(self,command,text):
         matches=[]
         pattern=re.compile(text+'.*')
	 if command=='detect':
	    self.add_match(self.detect.keys(),matches,pattern)
	 elif command=='by':
	    self.add_match(self.detect['by'],matches,pattern)
	 elif command=='checking':
	    self.add_match(self.detect['checking'],matches,pattern)
	 elif command=='connect':
	    self.add_match(self.connect.keys(),matches,pattern)
	 elif command=='using':
	    self.add_match(self.connect['using'],matches,pattern)
	 elif command=='cisco':
	    self.add_match(self.connect['cisco'],matches,pattern)
	 elif command=='h3c':
	    self.add_match(self.connect['h3c'],matches,pattern)
	 return matches

    def add_match(self,commands,matches,pattern):
         for command in commands:
	    if pattern.match(command):
	        matches.append(command)


    def help_hostname(self):
        '''
	To change the hostname
	'''
        print '\n'.join(['Change the hostname','Usage:hostname character'])

    def help_detect(self):
        print 'Follows:'
        print self.detect.keys()[1]+' '*20+' "Function:Check whether the host is pingable"'
	print self.detect.keys()[0]+' '*14+' "Function:Check whether the host is telnetable or sshable and tell the information of the network equipment"'

    def help_connect(self):
        print 'Follows:'
        print self.connect.keys()[1]+' '*20+'"Function:show cisco equipment and execute commands'
        print self.connect.keys()[2]+' '*22+'"Function:show h3c equipment and execute commands'
    
    def help_by(self):
        print 'Follows:'
	print self.detect['by'][0]+' '*10+'"Function:Check whether the ips are pingable according to the ip list"'
	print self.detect['by'][1]+' '*10+'"Function:Check whether the ips are pingable  according to the ip file"'
    
    def help_checking(self):
        print 'Follows:'
        print self.detect['checking'][0]+' '*10+'"Function:Check if the ips are telnetable  through list"'
        print self.detect['checking'][1]+' '*10+'"Function:Check if the ips are telnetable through file"'
        print self.detect['checking'][2]+' '*13+'"Function:Check if the ips are sshable through list"'
        print self.detect['checking'][3]+' '*13+'"Function:Check if the ips are sshable through file"'

    def help_cisco(self):
        print 'Follows:'
        print self.connect['cisco'][0]+' '*21+'"Function:show the info of the equipment "'
        print self.connect['cisco'][1]+' '*18+'"Function:Execute the commands of the equipment"'

    def help_h3c(self):
        print 'Follows:'
        print self.connect['h3c'][0]+' '*18+'"Function:display the info of the equipment "'
        print self.connect['h3c'][1]+' '*18+'"Function:Execute the commands of the equipment"'
 
    def help_ls(self):
        print 'Follows:'

