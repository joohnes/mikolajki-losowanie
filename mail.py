def sendMail(Subject: str = "Random subject", content: str = "Random content", file = None):
    import smtplib
    from email.message import EmailMessage
    import imghdr
    
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = Subject
    msg['From'] = "jacek.m2121@gmail.com"
    msg['To'] = "kubapienkowski@gmail.com" 
    msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'

        
    if file is not None:
        with open(file, 'rb') as fp:
            img_data = fp.read()
        msg.add_attachment(img_data, maintype='image',
                                    subtype=imghdr.what(None, img_data))
    
    with open('mikolajki-losowanie/passwords.txt', 'r') as f:
        password = f.read()
    
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login("jacek.m2121@gmail.com", password= password)
    s.send_message(msg)
    s.quit()