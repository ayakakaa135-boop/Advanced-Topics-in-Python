import re

#search

txt = "my name is aya"

search = re.search("[A-z]" , txt)
print(search)
print(search.span())
print(dir(search))
print(search.group())

test = "Call me at 210-999-3333  tomorrow. 334-344-4444 is my office"
search = re.search(r'\d{3}-\d{3}-\d{4}',test)
print(search)
print(search.groups())
print(search.string)