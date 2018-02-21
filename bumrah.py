import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)    
server.starttls()
server.login("ak088301@gmail.com", "password")
message= "yo"
server.sendmail("ak088301@gmail.com","ashishkrsingh@gmail.com",message)
s.quit()

