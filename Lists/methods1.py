# قائمة الموظفين
employees = ["Ali", "Sara", "Omar", "Aya"]
employees.append("Lina")
print(employees)

employees.insert(3,'sara')
print(employees)

oldEmployees = ['osama' , 'Alaaa' ]
employees.append(oldEmployees)
print(employees)
print(employees[6])
print(employees[6][0])

employees = ["Ali", "Sara", "Omar", "Aya"]
oldEmployees = ['osama' , 'Alaaa' ]
employees.extend(oldEmployees)
print(employees)

#remove
employees.remove('Ali')
print(employees)

employees = ["Ali", "Sara", "Omar", "Aya","Aya"]
employees.remove('Aya')
print( employees)

#del

del employees[0]
print(employees)

#sort

numbers = [1,2,3,4,5,8,9,0]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)


employees = ["Ali", "Sara", "Omar", "Aya","Aya"]
employees.sort()
print(employees)
employees.sort(reverse=True)
print(employees)


employees = ["Ali", "Sara", "Omar", "Aya","Aya"]
employees.reverse()
print( employees)