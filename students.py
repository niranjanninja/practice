students = [
    {
        "name": "Alice",
        "grades": [85, 90, 92],
        "activities": ["chess", "math club"]
    },
    {
        "name": "Bob",
        "grades": [78, 81, 74],
        "activities": ["football", "music band"]
    },
    {
        "name": "Charlie",
        "grades": [88, 85, 91],
        "activities": ["science fair", "robotics"]
    }
]
'''
Expected output
Student: Alice
  Grade: 85
  Grade: 90
  Grade: 92
  Average: 89.0
  Activities:
    - chess
    - math club

Student: Bob
  Grade: 78
  Grade: 81
  Grade: 74
  Average: 77.66666666666667
  Activities:
    - football
    - music band

Student: Charlie
  Grade: 88
  Grade: 85
  Grade: 91
  Average: 88.0
  Activities:
    - science fair
    - robotics
'''

for data in students:
    print(f'Student : {data["name"]}')
    total=0
    count=0
    for grades in data["grades"]:
        print(f'Grade : {grades}')
        total=total+grades
        count=count+1
        average=total/count
    print(f"Average : {average}")
    print("activities")
for activity in data['activities']:
    print(f'  -{activity}')



