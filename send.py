from socket import *

cs = socket(AF_INET, SOCK_DGRAM)

cs.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
cs.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

cs.sendto(['This is a test', 'Multiple', 'Items', \x2345], ('255.255.255.255', 657481))
