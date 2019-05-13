# Email SMS Gateway
Send and Receive SMS and MMS messages with only an email address.

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

# Endpoints depend on carrier so you must specify
number = Number("9715556666", "verizon")

sender.send_sms(number, "Hello, World!")

with open("./picture.jpg", "rb") as picture:
    sender.send_mms(
        number, 
        file_bytes=picture.read()
    )
```