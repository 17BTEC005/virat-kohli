import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("ak088301@gmail.com", "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)

