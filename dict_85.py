grades = {"Alice": 85, "Bob": 92, "Charlie": 85, "Diana": 90}
# Task: Write code to find all students who got the score 85.
# Output: ["Alice", "Charlie"]

a=[]
for name,mark in grades.items():
    if mark == 85:
        a.append(name)
print(a)
 
