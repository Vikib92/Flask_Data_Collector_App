import smtplib
from email.mime.text import MIMEText

def send_email(email, height, avg_hgt, cnt):
    from_email = 'viki.b92@gmail.com'
    from_passwd = '949614742844'
    to_email = email
    subject = 'Height data'
    message = 'Hi, your height is <strong>{}</strong>. The average height of all is <strong>{}</strong> from a total of <strong>{}</strong> people'.format(height, avg_hgt, cnt)
    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email
    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_passwd)
    gmail.send_message(msg)