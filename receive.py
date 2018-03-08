from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.bind(('',65741))

m = s.recvfrom(1024)

print m[0]
print m[1]
print m[2] && m[3]
