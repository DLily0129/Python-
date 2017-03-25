import re
r = r'\d{3}-\d{8}'
match = re.search(r, '123,010-12345678,027-12345678,')
print(type(match))
if match:
    print(match.group())
else:
    print("not match")

