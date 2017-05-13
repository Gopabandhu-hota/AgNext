#! /usr/bin python
import os
import urllib
import serial
import time
import subprocess
ser = serial.Serial('/dev/ttyS0', 115200, timeout = 1)
ser.flush()
ser.flushInput()
ser.flushInput()
ser.flushInput() #I feel there is need of more flushing as sometimes there is still data in b$
ser.flushOutput()

time.sleep(1)
ser.write('AT\r\n')
time.sleep(1)
x = ser.read(50)
print x

time.sleep(1)
ser.write('AT+CIPSHUT\r\n')
time.sleep(1)
x = ser.read(50)
print x
time.sleep(0.5)
ser.flushInput()


#Set the connection type to GPRS
ser.write('AT+SAPBR=3,1,"Contype","GPRS"\r\n')
time.sleep(1)
x = ser.read(50)
log.write(x)
ser.flushInput()


ser.write('AT+SAPBR=3,1,"APN","airtelgprs.com"\r\n')
time.sleep(1)
x = ser.read(50)
print x
ser.flushInput()

time.sleep(5)

#Enable the GPRS
ser.write('AT+SAPBR =1,1\r\n')
time.sleep(0.1)
x = ser.read(50)
log.write(x)
ser.flushInput()

#Query if the connection is setup properly, if we get back a IP address then we can proceed

ser.write('AT+SAPBR=2,1\r\n') #Sparkfun data.sparkfun.com:  54.86.1$
time.sleep(1.5)         #Sometimes it takes more time for connection (i.e. for "CONNECT OK" r$
x = ser.read(100)
print x
ser.flushInput()

#We were allocated a IP address and now we can proceed further by setting up the FTP bearer profile identifier
ser.write('AT+FTPCID=1\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()

#Set the FTP server name to which we want to connect, which in our case is ftp.drivehq.com
ser.write('AT+FTPSERV="ftp.drivehq.com"\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()

#Set the FTP user name, which in my case is dishank_agnext
ser.write('AT+FTPUN="dishank_agnext"\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()

#Set the FTP password for logging in, which in my case is agnext
ser.write('AT+FTPPW="agnext"\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()

#Set the file name which we want to upload to the server, which in our case is batman.jpg
ser.write('AT+FTPPUTNAME=" /home/pi/Downloads/batman.jpg "\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()

#Set the path where the file needs to be uploaded
ser.write('AT+FTPPUTPATH=" /My Pictures/ "\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()

#Start the FTP put session, by giving this command
ser.write('AT+FTPPUT=1\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()

#The below command tells the module that we want to send 83270 bytes of data
ser.write('AT+FTPPUT=2,83270\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()

#we don't want to transfer more data, So we close the FTP put session by the below command
ser.write('AT+FTPPUT=2,0\r\n')
time.sleep(0.1)
x = ser.read(50)
print x
ser.flushInput()
