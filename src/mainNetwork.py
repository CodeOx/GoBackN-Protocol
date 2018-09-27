#!/usr/bin/python

from mininet.topo import Topo, SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI
import subprocess
import fcntl
import os

def main():
    lg.setLogLevel('info')

    net = Mininet(SingleSwitchTopo(k=2))
    net.start()

    h1 = net.get('h1')
    h2 = net.get('h2')

    #p1 = h1.popen('python -u physicalLayer.py -s %s -d %s -m % s &' % (h1.IP(), h2.IP(), 're'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,  close_fds=True)
    p1 = h1.popen('python -u physicalLayer.py -s %s -d %s -m % s &' % (h1.IP(), h2.IP(), 'recieve'))
    #message = p1.stdout.read()
    #print message

    
    #p2 =h2.popen('python -u physicalLayer.py -s %s -d %s -m %s &' % (h2.IP(), h1.IP(), 'pqrs'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,  close_fds=True)
    #message2 = p2.stdout.read()
    #print message2    
    #print "Banchhor"
    #h2.cmd('python -u physicalLayer.py -s %s -d %s -m %s &' % (h2.IP(), h1.IP(), 'recieve'))
    print "Shashwat" 
    p2 =h2.popen('python -u physicalLayer.py -s %s -d %s -m %s &' % (h2.IP(), h1.IP(), 'pqrs'))
    CLI( net )
    p1.terminate()
    #p2.terminate()
    net.stop()

if __name__ == '__main__':
    main()
