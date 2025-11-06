import re

def is_email(email: str):
    email = email.strip()

    pattern = r'''
        ^([A-Za-z0-9](?!.*\.\.)
        [A-Za-z0-9._%+-]{0,63}
        [A-Za-z0-9])                 # ← المجموعة 1: اسم المستخدم
        @
        ((?!-)[A-Za-z0-9.-]+(?<!-))  # ← المجموعة 2: اسم النطاق
        \.([A-Za-z]{2,})$            # ← المجموعة 3: الامتداد
    '''

    match = re.fullmatch(pattern, email, re.VERBOSE | re.I)
    if match:
        return {
            "username": match.group(1),
            "domain": match.group(2),
            "tld": match.group(3)
        }
    else:
        return None


user_email = input("Enter your email: ")

result = is_email(user_email)
if result:
    print(f"✅ '{user_email.strip()}' is a valid email.")
    print(result)
else:
    print(f"❌ '{user_email.strip()}' is NOT a valid email.")
