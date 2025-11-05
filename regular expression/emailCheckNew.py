import re

def is_email(email: str) -> bool:
    email = email.strip()
    pattern = r'''
        ^[A-Za-z0-9](?!.*\.\.)
        [A-Za-z0-9._%+-]{0,63}
        [A-Za-z0-9]
        @
        (?!-)[A-Za-z0-9.-]+(?<!-)
        \.[A-Za-z]{2,}$
    '''
    return bool(re.fullmatch(pattern, email, re.VERBOSE))


user_email = input("Enter your email: ")

if is_email(user_email):
    print(f"✅ '{user_email.strip()}' is a valid email.")
else:
    print(f"❌ '{user_email.strip()}' is NOT a valid email.")
