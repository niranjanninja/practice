employees = {
    "Alice": [("Monday", "Morning"), ("Wednesday", "Evening")],
    "Bob": [("Tuesday", "Evening"), ("Thursday", "Morning")],
    "Charlie": [("Monday", "Evening"), ("Friday", "Morning")]
}
'''
Expected output

Employee: Alice
  Day: Monday, Shift: Morning
  Day: Wednesday, Shift: Evening

Employee: Bob
  Day: Tuesday, Shift: Evening
  Day: Thursday, Shift: Morning

Employee: Charlie
  Day: Monday, Shift: Evening
  Day: Friday, Shift: Morning

for name,data in employees.items():
    print(f'\nEmployee : {name}')
    print(f'  Day : {data[0][0]}, Shift:{data[0][1]}')
    print(f'  Day : {data[1][0]}, Shift:{data[1][1]}')
'''

for name,data in employees.items():
    print(f'\nEmployee: {name}')
    for day,shift in data:
        print(f'Day : {day}, Shift: {shift}')
