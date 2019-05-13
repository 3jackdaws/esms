from smtplib import SMTP
from imaplib import IMAP4
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import email
from datetime import datetime
from . import endpoints
import time

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


class Message:

    def __init__(self, number:Number, content, date:datetime, is_mms=False, id=None):
        self.number = number
        self.content = content
        self.received_at = date
        self.is_mms = is_mms
        self.id = int(id)


    def __repr__(self):
        return 'Message("{}", from={}, at={})'.format(
            self.content[0:20],
            self.number.number,
            self.received_at
        )

    def __eq__(self, other):
        return type(other) is Message and other.id == self.id

    def __hash__(self):
        return self.id

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
        self.imap.login(username, password)


    def get_messages_from(self, number:Number):
        self.imap.select("Inbox")
        code, results = self.imap.search(None, "FROM", "{}".format(number.number))
        email_ids = [i for i in results[0].decode().split(" ") if i]

        messages = []
        for id in email_ids:
            code, data = self.imap.fetch(id, '(RFC822)')
            msg = email.message_from_string(data[0][1].decode())
            from_addr = msg['From']
            date_tuple = email.utils.parsedate_tz(msg['Date'])
            local_date = None
            if date_tuple:
                local_date = datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            content = msg.get_payload().strip()
            messages.append(
                Message(
                    number,
                    content,
                    local_date,
                    id=id
                )
            )
            # print("ID {}: '{}' Received at: {}".format(id, content, local_date))
        return messages

    def await_messages_from(self, number:Number, timeout=0, poll=5) -> [Message]:
        cycles = 1
        if timeout > 0:
            poll = timeout if timeout < poll else poll  # set poll frequency to timeout value if timeout is less than poll
            cycles = timeout // poll
        messages = set(self.get_messages_from(number))
        while cycles > 0:

            if timeout > 0:
                cycles -= 1

            time.sleep(poll)
            new_messages = set(self.get_messages_from(number)).difference(messages)

            if len(new_messages) > 0:
                return list(new_messages)

        return []





class SMSClient:

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver



