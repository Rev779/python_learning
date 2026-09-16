import smtplib

sender = 'revanthrachapudi8@gmail.com'
password = 'tnbxojjvgzkcutcx'
reciever = 'rachapudisairevanth@gmail.com'
message = 'Hi Rakesh sir , I have sent the python code'

conn=smtplib.SMTP('smtp.gmail.com',587)
conn.starttls()
conn.login(sender,password)
conn.sendmail(sender,reciever ,message)
print('Email sent successfully')