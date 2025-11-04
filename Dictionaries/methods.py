sam = {
    "name": "Sam",
    "salary": 2500,
    "phone": "0791234567",
    "skills": ["Python", "SQL", "Git"]
}

print("The salary is " + str(sam.get("salary", "no salary")))

# setdefault example
sam.setdefault("birthday", "1998-05-14")
print(sam)

if 'language ' not  in sam:
    sam['language'] ='Css'

print(sam)

#update

student = {
    "name": "Aya",
    "age": 21,
    "major": "Computer Science"
}

print("Before update:")
print(student)

# تحديث قيمة وإضافة مفتاح جديد
student.update({"age": 22, "university": "Damascus University"})

print("\nAfter update:")
print(student)

sam.clear()
print(sam)

