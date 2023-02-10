print("Hello World!")
import smtplib
smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('alexismaglonso@yahoo.com', 'no53r09ghtGz29#d')
FROM = 'alexismaglonso@yahoo.com'
TO = ['akmaglonso@gmail.com']
SUBJECT = "Testing sending using gmail"
TEXT = "Testing sending mail using gmail servers"
message = """\From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
smtpObj.sendmail(FROM, TO, message)
smtpObj.quit()
