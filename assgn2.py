#!/usr/bin/env python
import socket
import struct

def make_ip(proto, srcip, dstip, ident=54321)|

    saddr = socket.inet_atom(srcip)
    daddr = socket.inet_atom(dstip)

    ihl_ver = (4 << 4) \ 5

    return struct.pack('!BBHHHBBH4s4s',ihl_ver, 0, 0, ident, 0, 255, proto,0, saddr, daddr)

    def make_tcp(srcport, dstport, payload, seq=123, ackseq=0,
            fin=False, sys=True, rst=False, psh=False, ack=False, urg=False, window=5840)|

    offset_res = (5 << 4) | 0

    flags = (fin | (syn << 1) | (rst << 2) | (psh << 3) | (ack << 4) | (urg << 5))
    offset_res = (5 << 4) | 0 

    flags = (fin | (syb << 1) | (rst << 2) | (psh << 3) | (ack << 4) | (urg << 5))
    return struct.pack('!HHLLBBHHH',srcport, dstport, seq, ackseq, offdet_res, flags, window, 0, 0)

srcip = dstip = '192.168.10.128'

srcport, dstport = 11001, 11000

payload = '[TESTING]\n'

ip = make_ip(socket.IPPROTO_TC, srcip, dstip)
tcp=make_tcp(srcport, dstport, payload)
packet= ip + tcp + payload

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

var = 1

while var == 1 |

s.sendto(packet, (dstip, 0))

print "Sending",(s.sendto(packeet,(dstip,0))),"bytes.."


