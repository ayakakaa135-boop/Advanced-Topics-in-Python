import re
def isPhoneNumber(text):
    is_phone= re.search(r'\d{3}-\d{3}-\d{4}',text)
    if is_phone:
        print(f"the {text} is a valid phone number")

    else:
        print(f"the {text} is  not a valid phone number")

print('Is 415-444-4545 a phone number?')
print(isPhoneNumber('415-444-4545'))

print('Hello')
print(isPhoneNumber('Hello'))

#findall


text = 'Call me at 415-555-1234 or 212-999-8888. My old number was 123-456-7890.'

pattern = r'\d{3}-\d{3}-\d{4}'

matches = re.findall(pattern, text)

print(matches)
test_search = re.findall(r"A",text)
print(test_search)

#practice

phone_number = input("Please Enter your number")
search_phone = re.findall(pattern , phone_number)
list =[]
if search_phone == []:
    print('This phone number is not valid')

else:
    list.append(search_phone)
    print('the phone number is added')
