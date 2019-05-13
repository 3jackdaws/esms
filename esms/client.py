from smtplib import SMTP
from imaplib import IMAP4
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from . import endpoints

class Number:

    def __init__(self, number, carrier):
        self.carrier = carrier
        self.number = number

    @property
    def sms_address(self):
        return endpoints.get_sms_address(self.carrier, self.number)

    @property
    def mms_address(self):
        return endpoints.get_mms_address(self.carrier, self.number)





class SMSSender:

    def __init__(self, host, port):
        self.smtp = SMTP(host, port)
        self._sender = None


    def login(self, username, password):
        if self._sender is None:
            self._sender = username
        self.smtp.starttls()
        self.smtp.login(username, password)

    def send_sms(self, number:Number, text:str):
        return self.smtp.sendmail(self._sender, number.sms_address, text)

    def send_mms(self, number:Number, *, text=None, file_bytes=None):
        send_to = number.mms_address
        msg = MIMEMultipart()
        msg['From'] = self._sender
        msg['To'] = send_to

        if text is not None:
            msg.attach(MIMEText(text))

        if file_bytes is not None:
            attachment = MIMEApplication(
                file_bytes
            )
            attachment['Content-Disposition'] = 'attachment'
            msg.attach(attachment)

        return self.smtp.send_message(msg, self._sender, send_to)

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, value):
        self._sender = value


class SMSReceiver:

    def __init__(self, host, port):
        self.imap = IMAP4(host, port)

    def login(self, username, password):
        self.imap.starttls()



class SMSClient:

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver



