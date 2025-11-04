test = 'Hello world'
print(test.upper())
print(test.lower())

test = test.upper()
print(test)

print('how are you')
feeling = input("Enter something: ")
if feeling.lower() == 'greet':
    print('I am fine')
else:
    print("I don't understand you.")


text = "hello world"
print(text.islower())  # True

text2 = "Hello world"
print(text2.islower())  # False


text = "HELLO"
print(text.isupper())  # True

text2 = "Hello"
print(text2.isupper())  # False

#tittle

text = "hello world from python"
print(text.title())

#capitalize

text = "hello world from python"
print(text.capitalize())

#swapcase
text = "Hello World"
print(text.swapcase())
