import pytest
from esms import SMSReceiver, Number, Message
import os



@pytest.fixture
def receiver():
    HOST = os.environ.get("SMTP_HOST")
    PORT = os.environ.get("IMAP_PORT")
    USER = os.environ.get("SMTP_USER")
    PASS = os.environ.get("SMTP_PASS")

    receiver = SMSReceiver(HOST, PORT)
    receiver.login(USER, PASS)
    return receiver

@pytest.fixture
def test_number():
    TEST_NUMBER = os.environ.get("TEST_NUMBER")
    TEST_CARRIER = os.environ.get("TEST_CARRIER")
    return Number(TEST_NUMBER, TEST_CARRIER)




def test_get_messages(receiver:SMSReceiver, test_number):

    msgs = receiver.get_messages_from()
    print(msgs)