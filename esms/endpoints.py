from .exceptions import UnsupportedCarrier

CARRIERS = {
  "alltel": {
    "sms": "message.alltel.com",
    "mms": "mms.alltelwireless.com"
  },
  "att": {
    "sms": "txt.att.net",
    "mms": "mms.att.net"
  },
  "boost": {
    "sms": "myboostmobile.com",
    "mms": "myboostmobile.com"
  },
  "cricket": {
    "sms": "sms.cricketwireless.net",
    "mms": "mms.cricketwireless.net"
  },
  "fi": {
    "sms": "msg.fi.google.com",
    "mms": "msg.fi.google.com"
  },
  "sprint": {
    "sms": "messaging.sprintpcs.com",
    "mms": "pm.sprint.com"
  },
  "tmobile": {
    "sms": "tmomail.net",
    "mms": "tmomail.net"
  },
  "us-cellular": {
    "sms": "email.uscc.net",
    "mms": "mms.uscc.net"
  },
  "verizon": {
    "sms": "vtext.com",
    "mms": "vzwpix.com"
  },
  "virgin": {
    "sms": "vmobl.com",
    "mms": "vmpix.com"
  }
}

def get_carrier(carrier):
    carrier = CARRIERS.get(carrier)
    if carrier is None:
        raise UnsupportedCarrier("{} does not map to a supported carrier".format(carrier))
    return carrier

def get_sms_address(carrier:str, number:str):
    carrier = get_carrier(carrier)
    return "{}@{}".format(
        number,
        carrier.get("sms")
    )

def get_mms_address(carrier, number):
    carrier = get_carrier(carrier)
    return "{}@{}".format(
        number,
        carrier.get("mms")
    )

