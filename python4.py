data = {
    "students": [
        {
            "name": "Alice",
            "scores": {"math": 90, "science": 85},
            "hobbies": ["reading", "chess"]
        },
        {
            "name": "Bob",
            "scores": {"math": 78, "science": 82},
            "hobbies": ["football", "gaming"],
            "certifications": {"Python", "AWS"}
        }
    ],
    "teachers": {
        "math": {
            "name": "Mr. Smith",
            "experience": 10,
            "subjects": ["algebra", "geometry"]
        },
        "science": {
            "name": "Ms. Jane",
            "experience": 8,
            "subjects": {"physics", "chemistry"}
        }
    },
    "admin": {
        "principal": "Dr. Brown",
        "offices": ["main office", "admin block"]
    } 
}
'''
Loop through students:

Print their name.

Print their subject scores.

Print their hobbies.

If they have certifications, print them too.

Loop through teachers:

Print each subject’s teacher name.

Print their experience.

Print the subjects they teach.

Print the Principal’s name and all office locations.

Student: Alice
  Math Score: 90
  Science Score: 85
  Hobbies: reading, chess

Student: Bob
  Math Score: 78
  Science Score: 82
  Hobbies: football, gaming
  Certifications: Python, AWS

Teacher of math:
  Name: Mr. Smith
  Experience: 10 years
  Subjects:
    - algebra
    - geometry

Teacher of science:
  Name: Ms. Jane
  Experience: 8 years
  Subjects:
    - physics
    - chemistry

Principal: Dr. Brown
Offices: main office, admin block
'''
for a in data["students"]:
    print(f"Student : {a['name']}")
    for b,c in a["scores"].items():
        print(f"{b} score : {c}")
    for d in a["hobbies"]:
        print(f"Hobbies : {d}")
    if "certifications" in a:
        for e in a["certifications"]:
            print(f"certifications : {e}")
for f,g in data["teachers"].items():
    print(f"teacher of {f}")
    print(f"Name : {g['name']}")
    print(f"Experience : {g['experience']}")
    print("Subjects")
    for h in g["subjects"]:
        print(f'-{h}')
print(f'Principal : {data["admin"]["principal"]}')
print(f'Offices : {data["admin"]["offices"][0]},{data["admin"]["offices"][1]}')   
num1=21
num2=31
num3=num1+num2
print(num3)

        

