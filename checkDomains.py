import socket
from netaddr import IPNetwork, IPAddress

cidr=('90.80.208.0/24','213.56.199.1/29','81.255.191.81/29','83.206.41.129/28','212.234.154.225/27','194.206.114.0/24')
fname="domains.txt"

#import line in list
with open(fname) as f:
        content = f.readlines()

for dom in content:
        dom=dom.strip()
        try:
                ip=socket.gethostbyname(dom)
                for sub in cidr:
                        if IPAddress(ip) in IPNetwork(sub):
                                print("%s %s %s"%(ip,dom,sub))
        except:
                #print dom
                pass
