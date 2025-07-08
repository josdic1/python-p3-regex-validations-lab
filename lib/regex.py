import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"([A-Z][a-zA-Z']*(?:-[A-Z][a-zA-Z']+)?)(\s[A-Z][a-zA-Z']*(?:-[A-Z][a-zA-Z']+)?)?"
name_regex = re.compile(name)

phone_number = r'^(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$'
phone_regex = re.compile(phone_number)

email_address = r'^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}$'
email_regex = re.compile(email_address)
