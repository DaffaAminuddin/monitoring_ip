from base64 import encode
import MySQLdb
import smtplib
import time
import imaplib
import email
import csv
import os
import email
from email.header import decode_header
import requests
import telepot

ORG_EMAIL = "@gmail.com" 
FROM_EMAIL = "coba.mikrotikmail" + ORG_EMAIL 
FROM_PWD = "hbimavpoqnwpeaiv" 
SMTP_SERVER = "imap.gmail.com" 
SMTP_PORT = 993

def kirim_tele():
    token = '5468371812:AAEyRk91E3o45DYpRLatgzHezYr_kVYJZm0'
    receiver_id = -765375915
    bot = telepot.Bot(token)
    bot.sendMessage(receiver_id, ip+" "+"sedang" +" "+ status+" "+ date)


count = ''
while(True):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')	
        mail.login(FROM_EMAIL, FROM_PWD)
        mail.select() # connect to inbox.
        return_code, data = mail.search(None, 'UnSeen')
        
        #count = len(mail_ids[0].split(" "))
        mail_ids = data[0].decode()
        id_list = mail_ids.split()
        first_email_id = int(id_list[-2])
        latest_email_id = int(id_list[-1])
        #delete email 
        
            #filewriter.writerow(['From', 'Subject','Date'])
        for i in range(latest_email_id,first_email_id,-2):
            typ, data = mail.fetch(str(i),'(RFC822)')
            for response_part in data:
                    arr = response_part[0]
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1].decode("utf-8"))
                        email_subject = msg['subject']
                        email_from = msg['from']
                        email_date = msg['date']
                        status = email_subject[15:22]
                        ip = email_subject[0:14]
                        date = email_date[0:22]
                        if status=='OFFLINE':
                            print('Email baru ditemukan')
                            print(email_subject)
                            requests.post('https://maker.ifttt.com/trigger/ip_monitoring/with/key/sxe-0Fds3FRNMPXgwatzXkv-jX3qiZSZLPjmehaGfqLO8ByKv5NfeMn9iA1j3Jw9', params = { "value1" : ip, "value2" : status, "value3" : date })
                            with open('/home/momon/monitoring_iot/persons.csv', 'w', newline="") as csvfile:
                                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                                filewriter.writerow([ip, status, date])
                            mail.close()
                            mail.logout()
                            time.sleep(2)
                            exec(open('/home/momon/monitoring_iot/upload_sql.py').read())
                            time.sleep(2)
                            kirim_tele()
                            #exec(open('kirim_tele.py').read())

                        if status=='ONLINE':
                            print('Email baru ditemukan')
                            print(email_subject)
                            requests.post('https://maker.ifttt.com/trigger/ip_monitoring/with/key/sxe-0Fds3FRNMPXgwatzXkv-jX3qiZSZLPjmehaGfqLO8ByKv5NfeMn9iA1j3Jw9', params = { "value1" : ip, "value2" : status, "value3" : date })
                            with open('/home/momon/monitoring_iot/persons.csv', 'w', newline="") as csvfile:
                                filewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                                filewriter.writerow([ip, status, date])
                            mail.close()
                            mail.logout()
                            time.sleep(2)
                            exec(open('/home/momon/monitoring_iot/upload_sql.py').read())
                            time.sleep(2)
                            kirim_tele()
                            #exec(open('kirim_tele.py').read())
                        time.sleep(3)


    except Exception as e: print(e)
    

    print (count)