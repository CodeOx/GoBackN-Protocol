#!/usr/bin/python

from mininet.topo import Topo, SingleSwitchTopo
from mininet.net import Mininet
from mininet.log import lg, info
from mininet.cli import CLI
import subprocess

def main():
    lg.setLogLevel('info')

    net = Mininet(SingleSwitchTopo(k=2))
    net.start()

    h1 = net.get('h1')
    p1 = h1.popen('python physicalLayer.py -i_src %s -i_dest %s &' % (h1.IP(), h2.IP()), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,  close_fds=True)
    p1.stdin.write('recieve')
    p1.stdin.flush()
    message = p1.stdout.read()
    print message

    h2 = net.get('h2')
    p2 = h2.popen('python physicalLayer.py -i_src %s -i_dest %s &' % (h2.IP(), h1.IP()), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE,  close_fds=True)
    p2.stdin.write('send')
    p2.stdin.flush()
    
    CLI( net )
    p1.terminate()
    net.stop()

if __name__ == '__main__':
    main()