import socket
import os
pn=socket.SOCK_DGRAM
afn=socket.AF_INET

s=socket.socket(afn,pn)

print("                    ----------------------                     ")
print("--------------------CHAT PROGRAM USING UDP---------------------")
print("                    ----------------------                     ")

print("|---------------------------------------------------------------|")
print(" Enter your System IP:",end=" ")
ip=input()
print(" Enter Sender IP:",end=" ")
sip=input()
print(" Port number:",end=" ")
sport=int(input())
port=7002
print("|---------------------------------------------------------------|")
s.bind( (ip,port) )

def rec():
	x=s.recvfrom(1024)
	cip=x[1][0]
	xd=x[0].decode()
	print("                                  ",end=" ")
	print(f"Received Message:{xd}")
	#print(f"                                  Sender IP:{cip}")

def send(sip,sport):
	#print("                        ",end=" ")
	inp=input("Enter Your Message:")
	s.sendto(inp.encode(), (sip,sport))

while True:
	rec()
	send(sip,sport)

thread1=threading.Thread(target=rec)
thread2=threading.Thread(target=send)

thread1.start()
thread2.start()



	
