school = {
    "Grade 6": {
        "Alice": {"Math": 88, "Science": 92, "English": 85},
        "Bob": {"Math": 75, "Science": 80, "English": 78}
    },
    "Grade 7": {
        "Charlie": {"Math": 90, "Science": 85, "English": 87},
        "Diana": {"Math": 95, "Science": 91, "English": 89}
    }
}
'''
Grade: Grade 6
  Student: Alice
    Subject: Math, Score: 88
    Subject: Science, Score: 92
    Subject: English, Score: 85
  Student: Bob
    Subject: Math, Score: 75
    Subject: Science, Score: 80
    Subject: English, Score: 78

Grade: Grade 7
  Student: Charlie
    Subject: Math, Score: 90
    Subject: Science, Score: 85
    Subject: English, Score: 87
  Student: Diana
    Subject: Math, Score: 95
    Subject: Science, Score: 91
    Subject: English, Score: 89
'''
'''
for grade,data in school.items():
    print(f'\nGrade: {grade}')
    for name,subs in data.items():
        print(f' Student: {name}')
        for sub,mark in subs.items():
            print(f'  Subject:{sub}, Score: {mark}')
'''
def schools(school_data : dict)->None:
    for grade,data in school.items():
        print(f'\nGrade: {grade}')
        for name,subs in data.items():
            print(f' Student: {name}')
            for sub,mark in subs.items():
                print(f'  Subject:{sub}, Score: {mark}')

schools(school)


