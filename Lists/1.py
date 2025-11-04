import random

employees = ["Ali", "Sara", "Omar", "Aya"]
print(employees)
print(employees[3])
print(employees[-1])
print(employees[1:3])
print(employees[:3])
print(employees[1:])
print(employees[1:3:1])
print(employees[::2])
employees[1] = 'maya'
print(employees)
employees[-1] = 'yara'
print(employees)
employees[0:2] = 'hadi' ,'Salma'
employees[0:2] = ''
print(employees)


employees = ["Ali", "Sara", "Omar", "Aya"]
for i in range(4):
    print(employees[i])


for i in range(len(employees)) :
    print(employees[i])


for i in range(len(employees)) :
    print(f'index {i} in employees is : {employees[i]}')


#enumerate
for index,item in enumerate(employees):
    print(f'index {index} in employees is : {item}')


# in and not in

print('Hadi'in employees )
print('hadi' not in employees)

# قائمة الموظفين
employees = ["Ali", "Sara", "Omar", "Aya", "Lina"]

# إدخال اسم الموظف من المستخدم
name = input("Enter employee name: ")

# التحقق من وجوده
if name.lower() in [emp.lower() for emp in employees]:
    print(f"{name} works in the company ✅")
else:
    print(f"{name} is not in the company ❌")

#random.choice() and random.shuflle
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))
random.shuffle(employees)
print(employees)
