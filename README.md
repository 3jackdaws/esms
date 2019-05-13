# Email SMS Gateway
Send and Receive SMS and MMS messages with only an email address.

# How it works
Many US cell carriers implement a way to send SMS and MMS messages to their subscribers by sending an email to a carrier specific email address.  For example, if you send the text `Hello World` to `1234567890@vtext.com` from `you@example.com` if the phone number `1234567890` corresponds to a Verizon subscriber, they will receive the text "Hello World" and it will be from `you@example.com`.  Each carrier has a different email address you must send messages to, but the basics are the same. 

# Features
|  Feature | Implimented |
| -------- | ----------- |
| Send SMS Messages | YES  | 
| Send Pictures via MMS | YES |
| Receive SMS Messages | Planned |
| Wait for a message from a specific number | Planned |



# Usage

### Send SMS and MMS messages
```python
from esms import Number, SMSSender

sender = SMSSender(
    host="mail.example.com",
    port="587"
)

sender.login("test@example.com", "password")

# Endpoints depend on carrier so you must specify
number = Number("9715556666", "verizon")

sender.send_sms(number, "Hello, World!")

with open("./picture.jpg", "rb") as picture:
    sender.send_mms(
        number, 
        file_bytes=picture.read()
    )
```

# Bugs & Issues
Please report all bugs and issues via the GitHub Issues tab and include thge following:
* OS
* Python version
* Exact code that causes the issue
* esms version (`pip show esms`)

Reporting issues will make this package better.  Thanks!

