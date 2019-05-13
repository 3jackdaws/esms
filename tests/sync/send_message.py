import pytest
from esms import SMSSender, Number
import os



@pytest.fixture
def sender():
    HOST = os.environ.get("SMTP_HOST")
    PORT = os.environ.get("SMTP_PORT")
    USER = os.environ.get("SMTP_USER")
    PASS = os.environ.get("SMTP_PASS")

    sender = SMSSender(HOST, PORT)
    sender.login(USER, PASS)
    return sender

@pytest.fixture
def test_number():
    TEST_NUMBER = os.environ.get("TEST_NUMBER")
    TEST_CARRIER = os.environ.get("TEST_CARRIER")
    return Number(TEST_NUMBER, TEST_CARRIER)

def test_send_message(sender: SMSSender):

    sender.send_sms(
        "Testing 1 2 3",
        test_number
    )

def test_send_picture(sender:SMSSender, test_number:Number):
    PICTURE_PATH = "./tests/resources/doge.jpg"
    with open(PICTURE_PATH, "rb") as fp:
        sender.send_mms(
            test_number,
            file_bytes=fp.read()
        )