import smtplib
import os

def sendEmail(email, name, message):
    sending_email = email
    sending_name = name
    sending_message = message
    sending_subject = "Pallet Request from Customer"

    myEmail = "no.reply.pallet.mail@gmail.com"
    myPassword = "emailforcharlessite"

    charlesEmail = "golfrocks951@gmail.com"
    #charlesEmail = "sfisherman87@gmail.com"

    body = '''\
        Name: %s\n
        Email: %s\n

        %s
    '''% (sending_name, sending_email, sending_message)

    email_text = """\
    From: %s
    Subject: %s

    %s
    """ % (myEmail, sending_subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(myEmail, myPassword)
        smtp_server.sendmail(myEmail, charlesEmail, email_text)
        smtp_server.close()
    except Exception as ex:
        os.system('echo "{}" >> emailErrors.txt'.format(ex))
