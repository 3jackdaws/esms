# Email SMS Gateway
Send and Receive SMS and MMS messages with only an email address.

# How it works
Many US cell carriers implement a way to send SMS and MMS messages to their subscribers by sending an email to a carrier specific email address.  For example, if you send the text `Hello World` to `1234567890@vtext.com` from `you@example.com` if the phone number `1234567890` corresponds to a Verizon subscriber, they will receive the text "Hello World" and it will be from `you@example.com`.  Each carrier has a different email address you must send messages to, but the basics are the same. 

# Features
|  Feature | Implemented (Sync) | Implemented (Async) | 
| -------- | ----------- | ------- |
| Send SMS Messages | YES  | PLANNED |
| Send Pictures via MMS | YES | PLANNED |
| Receive SMS Messages | TECHNICALLY | PLANNED |
| Wait for a message from a specific number | POORLY | PLANNED | 
| Get all messages | SURPRISINGLY, NO, BUT PLANNED | PLANNED
| Event based message handling | WON'T HAPPEN | PLANNED



# Usage

### Send SMS and MMS messages
```python
from esms import Number, SMSSender

client = SMSSender(
    host="mail.example.com",
    port="587"
)

client.login("test@example.com", "password")

# Endpoints depend on carrier so you must specify
number = Number("9715556666", "verizon")

client.send_sms(number, "Hello, World!")

with open("./picture.jpg", "rb") as picture:
    client.send_mms(
        number, 
        file_bytes=picture.read()
    )
```

### Receive SMS from a specific Number
```python
from esms import SMSReceiver, Message, Number

client = SMSReceiver(
    host="mail.example.com",
    port="587"
)

client.login("test@example.com", "password")

# Endpoints depend on carrier so you must specify
number = Number("9715556666", "verizon")

# Get all messages from a number
messages = client.get_messages_from(number)  # type: [Messages]

# OR

# wait for a message from [number] for up to 60 seconds, poll every 5 seconds
messages = client.await_messages_from(number, timeout=60, poll=5)
```

# Bugs & Issues
Please report all bugs and issues via the GitHub Issues tab and include thge following:
* OS
* Python version
* Exact code that causes the issue
* esms version (`pip show esms`)

Reporting issues will make this package better.  Thanks!

