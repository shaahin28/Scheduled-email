import datetime as dt
import smtplib
import time


def send_email():
    user_email = 'youremail@gmail.com'
    server = smtplib.SMTP ('smtp.gmail.com', 587)
    server.starttls()
    server.login(user_email, 'your password')

    message = 'This email is coming from email_at_time.py via python!'
    server.sendmail(user_email, user_email, message)
    server.quit()

#some of time module functions :

# print(time.ctime()) --> will show us the local time

# time.sleep(seconds) --> Suspend execution of the calling thread for the given number of seconds

# time.time() --> Return the time in seconds since the epoch as a floating point number. epoch in linux is Jan 1st 1970 0:0:0

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('Email sent')


first_email_time = dt.datetime(2019,3,12,15,0,0) # set your sending time
interval = dt.timedelta(minutes=24*60) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval

send_email_at(send_time)
