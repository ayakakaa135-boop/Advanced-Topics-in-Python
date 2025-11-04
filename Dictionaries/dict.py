employees = {
    "Omar": {
        "salary": 2500,
        "phone": "0791234567",
        "skills": ["Python", "SQL", "Git"]
    },
    "Lina": {
        "salary": 3000,
        "phone": "0789876543",
        "skills": ["JavaScript", "HTML", "CSS"]
    },
    "Hadi": {
        "salary": 2800,
        "phone": "0771122334",
        "skills": ["Java", "Spring", "Docker"]
    }
}
print(employees)
print(employees["Omar"]["skills"])
lists = ['1' ,'2' ,'3']
my_lists = ['3' ,'2' ,'1']
print(list == my_lists)
print(lists[0])

print(my_lists[0])


dict = {'1', '2', '3'}
my_dict = {'3', '2', '1'}
print(dict == my_dict)

students = {
    "Ali": {"age": 20, "grade": "B"},
    "Lina": {"age": 22, "grade": "A"},
}

print(students["Lina"]["grade"])  # A
"""
birthdays = {
    "Aya": "2002-04-12",
    "Omar": "1998-05-14",
    "Lina": "1996-10-30",
    "Hadi": "1999-02-18"
}
while True:
    print('Enter a name :(blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + 'is the birthday of ' + name )

    else :
        print('I do not have birthday information for '+ name)
        print('what is their birthdays')
        b_day = input()
        birthdays[name] = b_day
        print('birthday database updated')
"""

Omar = {
    "salary": 2500,
    "phone": "0791234567",
    "skills": ["Python", "SQL", "Git"]
}
print(Omar.keys())
print(Omar.values())
print(Omar.items())


students = {
    "Ali": {"age": 20, "grade": "B"},
    "Lina": {"age": 22, "grade": "A"},
}

print(students["Lina"]["grade"])  # A
