import serial
import time
from read_unseen_email import ip
from read_unseen_email import email_date
 
receiverNum = "+628155226946"
sim800l = serial.Serial(
port='/dev/serial0',
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,
bytesize=serial.EIGHTBITS,
timeout=1
)
 
sms = (ip +" "+"kembali ONLINE pada"+" "+ email_date)
time.sleep(1)
sim800l.write('AT+CMGF=1\n')
print (sim800l.read(24))
time.sleep(1)
cmd1 = "AT+CMGS=\" "+str(receiverNum)+"\"\n"
sim800l.write(cmd1)
print (sim800l.read(24))
time.sleep(1)
sim800l.write(str(sms))
sim800l.write(chr(26))
print (sim800l.read(24))