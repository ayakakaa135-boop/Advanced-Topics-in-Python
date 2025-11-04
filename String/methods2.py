text = "Python is fun"
print(text.startswith("Py"))   # True
print(text.startswith("py"))   # False (لانها case sensitive)
print(text.endswith("fun"))
print(text.startswith("P"))
print(text.startswith("n"))
print(text.startswith('p',3,11))

text = "   hello world   "
print(text.strip())

text = "xxxhello worldxxx"
print(text.strip("x"))

text = "   hello world   "
print(text.lstrip())


text = "   hello world   "
print(text.rstrip())

num = "42"
print(num.zfill(5))

hours = "5"
minutes = "7"
seconds = "3"

time = f"{hours.zfill(2)}:{minutes.zfill(2)}:{seconds.zfill(2)}"
print(time)


hours = "5"
minutes = "17"
seconds = "13"

time = f"{hours.zfill(2)}:{minutes.zfill(1)}:{seconds.zfill(1)}"
print(time)
