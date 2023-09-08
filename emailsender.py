import smtplib

recieveremail = input("Enter the email of the reciever:\n")

content = input("Enter the content of the mail:\n")

def sendEmail(recieveremail,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo                 #this is to make communicaiton between smtp server and gmail
    server.starttls()           #this is to start the session
    server.login('senderEmail@gmail.com', 'password1234')
    server.sendmail('senderEmail@gmail.com',recieveremail,content)
    server.close()

sendEmail(recieveremail,content)