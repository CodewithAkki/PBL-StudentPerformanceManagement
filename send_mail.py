import smtplib
from email import utils
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

class sendEmail:
    #Attachments need full file paths
    #this is for amazon ses service

    def __init__(self,sender,sendername,recipient_list,username_stmp,password_stmp
    ,host,port,subject,body_html = None,body_text = None, attachments:list = None) -> None:
        self.sender = sender
        self.sendername = sendername
        self.recipient_list = recipient_list
        self.username_stmp = username_stmp 
        self.password_stmp = password_stmp
        self.host = host
        self.port = port
        self.subject = subject
        self.body_html = body_html 
        self.body_text = body_text
        self.attachments = attachments
    
    def _attachfiles(self,msg):
        if self.attachments is None :
            return msg
        else:
            for attachment in self.attachments:
                file = os.path.basename(attachment)
                part = MIMEBase('application', "octet-stream",Name = file)
                part.set_payload(open(attachment, "rb").read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(file))
                msg.attach(part)
        return msg

    def _attachmailingbody(self,msg):
        if self.body_text is not None:
            part = MIMEText(self.body_text, 'plain')
            msg.attach(part)
        
        if self.body_html is not None:
            part  = MIMEText(self.body_html,'html')
            msg.attach(part)
        return msg
    
    @property
    def sendmail(self):
        msg = MIMEMultipart('alternative')
        msg = self._attachfiles(msg)
        msg = self._attachmailingbody(msg)
        msg['To'] =  ",".join(self.recipient_list)
        msg['Subject'] = self.subject
        msg['From'] = utils.formataddr((self.sendername,self.sender))
        try:
            server = smtplib.SMTP(self.host,self.port)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.username_stmp,self.password_stmp)
            server.sendmail(self.sender,self.recipient_list,msg.as_string())
            server.close()
        except Exception as e:
            print(str(e))
            pass