import re


text = 'Call me at 415-555-1234 or 212-999-8888.'

pattern = r'\d{3}-\d{3}-\d{4}'

# استبدال أرقام الهواتف بنص عام
result = re.sub(  pattern, '111 222 2222', text,1)

print(result)

text = "T am a student at Hsuoub Academy "
pattern = r"\s"
#result = re.sub(pattern,"-",text,2)
result = re.sub(r"Hsoub Academy" ,"Hsoub-Academy",text)
print(result)


#split


text = "Python is awesome, easy-to-learn, and powerful!"
pattern = r"[\s,!-]+"

result = re.split(pattern, text)
print(result)

text= "https://academy.hsoub.com/courses/python-application-development/python-apps/regular-expressions/06-%D8%A7%D8%B3%D8%AA%D8%A8%D8%AF%D8%A7%D9%84-%D9%88%D8%AA%D9%82%D8%B7%D9%8A%D8%B9-%D8%A7%D9%84%D9%86%D8%B5%D9%88%D8%B5-%D8%B9%D8%A8%D8%B1-%D8%AF%D9%88%D8%A7%D9%84-%D8%A7%D9%84%D9%88%D8%AD%D8%AF%D8%A9-re-r3789/"
pattern = "-"
result = re.sub(pattern ," ", text)
print(result)


result = re.split(r"-" ,text)
print(result)