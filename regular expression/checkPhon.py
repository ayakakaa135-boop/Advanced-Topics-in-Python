"""def isPhoneNumber(text):
    if len(text) != 12:
        return False

    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False

    for i in range(4, 7):
        if not text[i].isdecimal():
            return False

    if text[7] != '-':
        return False

    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True


print('Is 415-444-4545 a phone number?')
print(isPhoneNumber('415-444-4545'))

print('Hello')
print(isPhoneNumber('Hello'))"""

import re

def isPhoneNumber(text):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, text))

print('Is 415-444-4545 a phone number?')
print(isPhoneNumber('415-444-4545'))


import re

def isPhoneNumber(text):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return bool(re.match(pattern, text))


# ✅ حالات صحيحة
assert isPhoneNumber('415-555-1234') == True
assert isPhoneNumber('123-456-7890') == True

# ❌ حالات خاطئة
assert isPhoneNumber('4155551234') == False      # بدون شرطات
assert isPhoneNumber('41-5555-1234') == False    # تنسيق غلط
assert isPhoneNumber('415-5555-123') == False    # عدد خانات غلط
assert isPhoneNumber('abc-def-ghij') == False    # أحرف بدل أرقام

print("All tests passed! ✅")
