import smtplib
import os
import imghdr

from email.message import EmailMessage

#set email_address and email_password on  your environment variables
email_address = os.environ.get('email_address')
email_password = os.environ.get('email_password')
#print(email)
#contacts = ['hello@sarojb.com.np', 'hi@nischal.com.np', 'hi@aashishtiwari.com.np', 'poshan0126@gmail.com']

msg = EmailMessage()
msg['Subject']='Hello, Lionel Saroj'
msg['From']= email_address 
msg['To']=email_address 
msg.set_content('How are you feeling today?')

#for htmls and stuffs
msg.set_content('This is plain text email')
msg.add_alternative("""\
<!DOCTYPE HTML> 
<html>
   <body> 
        <h1 style = "color: purple;">Hi! I am plain text! Try me </h1>
   </body>
</html>
""", subtype='html')

'''files = ['', '']
for file in files:
    with open(file,'rb') as f:
        file_data = f.read()
        #file_type = imghdr.what(f.name) for pdfs and stuffs we don't need it
        file_name = f.name

   # msg.add_attachment(file_data, maintype='image', subtype = file_type, filename = file_name) for image
    msg.add_attachment(file_data, maintype='application', subtype = 'octet-stream', filename = file_name) 
'''
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(msg)

