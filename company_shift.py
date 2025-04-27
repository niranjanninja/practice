company = {
    "Engineering": {
        "Alice": [("Monday", "Morning"), ("Wednesday", "Evening")],
        "Bob": [("Tuesday", "Evening")]
    },
    "Marketing": {
        "Charlie": [("Monday", "Evening"), ("Friday", "Morning")],
        "Diana": [("Thursday", "Morning")]
    }
}
'''
Department: Engineering
  Employee: Alice
    Day: Monday, Shift: Morning
    Day: Wednesday, Shift: Evening
  Employee: Bob
    Day: Tuesday, Shift: Evening

Department: Marketing
  Employee: Charlie
    Day: Monday, Shift: Evening
    Day: Friday, Shift: Morning
  Employee: Diana
    Day: Thursday, Shift: Morning

for sub,data in company.items():
    print(f'\nDepartment : {sub}')
    for name,day in data.items():
        print(f" Employee : {name}")
        print(f'  Day: {day[0][0]}, Shift : {day[0][1]}')
        if (name == "Alice"):
            print(f'  Day : {day[1][0]}, Shift : {day[1][1]}')
        elif (name == "Charlies"):
            print(f'  Day : {day[1][0]}, Shift : {day[1][1]}')
        else:
            print("Else reached")
'''

for dept,data in company.items():
    print(f'\nDepartment : {dept}')
    for name,detail in data.items():
        print(f"Employee : {name}")
        for day,shift in detail:
            print(f'Day : {day}, Shift : {shift}')

