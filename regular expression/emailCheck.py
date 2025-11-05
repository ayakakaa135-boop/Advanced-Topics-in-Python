import re

def isEmail(email):
    is_email = re .search( r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.(com|net|org|edu)$',email)

    if is_email:
        print(f'the {email} is a valid Email')

    else:
        print(f'the {email} is not a valid Email')



print('Is hsoub.academy@gmail.com a email')

isEmail('hsoub.academy@gmail.com')

print('Is hsoub.academy@gmail a email')
isEmail(' hsoub.academy@gmail')
