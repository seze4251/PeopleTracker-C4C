from socket import *
import time
import subprocess

host = " 10.0.0.151" #ip address of the server

print host

port = 4447

s=socket(AF_INET, SOCK_STREAM)
#s.settimeout(60)
#s.timeout()
print "socket made"

while True:
	try:
		s.connect((host, port))
		s.send("Client 2 connected")
		print "socket connected!!"
		msg = s.recv(1024)
		print "Message from server: ", msg
		time.sleep(3)
		break
	except:
		print "not connection found will try again in 2 seconds..."
		time.sleep(1)

try:
	while True:
		
		msg = "This is client2"
		s.send(msg)

		msg=s.recv(1024)
		print "Message from server: " + msg
		time.sleep(1)
		
		
except KeyboardInterrupt:
	print "\nClosing"
	s.close

except Exception:
	print "\nOther Raspberry pi close connection"
	print "Close connection"
	s.close
	

def shutdownRPi():
	print "Shutting down"
	command = "/usr/bin/sudo /sbin/shutdown -h now"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        print output

