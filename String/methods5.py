text = "I love Python"
print(text.find("love"))
print(text.find("l"))
print(text.find("love",0,4))

try:
    print(text.index('world' ,0,5))

except ValueError:
    print('-1')


text = "banana"
print(text.find("a", 2))  # يبدأ البحث من index 2

text = "I love Python"
print(text.replace("Python", "Java"))

text = "apple apple apple"
print(text.replace("apple", "orange", 2))
