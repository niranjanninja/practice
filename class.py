'''
p = Person("Alice", 30)
print(p.greet())
Expected output
Hi, I am Alice and I am 30 years old.
'''

class person:
    def __init__(self,name,age):
        self.name=""
        self.age=""
        print(f'Hi, I am {name} and I am {age} years old')

print(person("Alice",30))

