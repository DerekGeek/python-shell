#!/usr/bin/python
import socket
import struct
__metaclass__=type
class ip:
    def __init__(self,source,destination):
       self.version=4
       self.ihl=5
       self.tos=0
       self.tl=0 #Total Length
       self.id=54321 #identifier
       self.flags=0
       self.offset=0
       self.ttl=255
       self.protocol=socket.IPPROTO_ICMP
       self.checksum=0
       self.source=socket.inet_aton(source)
       self.destination=socket.inet_aton(destination)
    def pack(self):
        ver_inl=(self.version<<4)+self.ihl
	flags_offset=(self.flags<<13)+self.offset
	'''
	B means unsigned char
	H means unsigned short
	'''
        ip_header=struct.pack("!BBHHHBBH4s4s",
	          ver_inl,
		  self.tos,
		  self.tl,
		  self.id,
		  flags_offset,
		  self.ttl,
		  self.protocol,
		  self.checksum,
		  self.source,
		  self.destination)
        return ip_header

class Icmp:
   def  __init__(self):
        self.type=8
	self.code=0
	self.checksum=0
	self.id=0
	self.seq=0
   def checksum(self,data):
       s=0
       n=len(data)%2
       for i in range(0,len(data),2):
          w=(ord(data[i])<<8)+(ord(data[i+1]))        
	  s=s+w
       if n:
          s+=ord(data[i+1])
       while(s>>16):
	  s=(s&0xffff)+(s>>16)
       s=~s&0xffff
       return s

   def ping(self,source_ip,dest_ip):
       icmp_packet=struct.pack("!BBHHH",self.type,self.code,self.checksum,self.id,self.seq)
       chksum=checksum(icmp_packet)
       icmp_packet=struct.pack("!BBHHH",self.type,self.code,chksum,self.id,self.seq)
       try:
           ipobj=ip(source_ip,dest_ip)
           iph=ipobj.pack()
           packet=iph+icmp_packet
           s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
           s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
           s.settimeout(0.01)
           s.sendto(packet,(dest_ip,1))
           echo_packet=s.recvfrom(1024)[0]
       except socket.timeout:
           return 'Nothing'
       return echo_packet
def checksum(data):
       s=0
       n=len(data)%2
       for i in range(0,len(data),2):
          w=(ord(data[i])<<8)+(ord(data[i+1]))        
	  s=s+w
       if n:
          s+=ord(data[i+1])
       while(s>>16):
	  s=(s&0xffff)+(s>>16)
       s=~s&0xffff
       return s


if __name__=="__main__":
   source_ip='10.191.87.91'
   dest_ip='10.191.87.2'
   Ping=Icmp()
   data=Ping.ping(source_ip,dest_ip)
   if data:
       if (ord(data[20]))==0 and (ord(data[21]))==0:
           print dest_ip,'is reachable'
       else:
           print dest_ip,'is not reachable'
   else:    
       print dest_ip,'is not reachable'
