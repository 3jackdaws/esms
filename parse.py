text = """

Alltel	[insert 10-digit number]@message.alltel.com	[insert 10-digit number]@mms.alltelwireless.com
AT&T	[insert 10-digit number]@txt.att.net	[insert 10-digit number]@mms.att.net
Boost Mobile	[insert 10-digit number]@myboostmobile.com	[insert 10-digit number]@myboostmobile.com
Cricket Wireless	[insert 10-digit number]@sms.cricketwireless.net	[insert 10-digit number]@mms.cricketwireless.net
Project Fi	[insert 10-digit number]@msg.fi.google.com	[insert 10-digit number]@msg.fi.google.com
Sprint	[insert 10-digit number]@messaging.sprintpcs.com	[insert 10-digit number]@pm.sprint.com
T-Mobile	[insert 10-digit number]@tmomail.net	[insert 10-digit number]@tmomail.net
U.S. Cellular	[insert 10-digit number]@email.uscc.net	[insert 10-digit number]@mms.uscc.net
Verizon	[insert 10-digit number]@vtext.com	[insert 10-digit number]@vzwpix.com
Virgin Mobile	[insert 10-digit number]@vmobl.com	[insert 10-digit number]@vmpix.com
Republic Wireless	[insert 10-digital number]@text.republicwireless.com

"""

import json
import re

ce = {}

for line in text.strip().split("\n"):
    matches = re.findall(
        r'^([A-Za-z-.& ]+)\t.*@([a-z.]+)\t.*@([a-z.]+)',
        line
    )
    try:
        matches = matches[0]
        ce[matches[0].lower()] = {
            "sms":matches[1],
            "mms":matches[2]
        }
    except:
        pass

print(json.dumps(ce, indent=2))