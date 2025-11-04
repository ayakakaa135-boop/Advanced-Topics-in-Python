stringOne = 'This is string one'

#indexing
print(stringOne[0])
print(stringOne[-1])


#slicing [start :end :step ]
print(stringOne[5:14])
print(stringOne[:14])
print(stringOne[5:])
print(stringOne[:])
print(stringOne[:-4])
print(stringOne[-13:-4])


#steps

print(stringOne[0:7:1])
print(stringOne[::1])
print(stringOne[::2])
print(stringOne[::-1])