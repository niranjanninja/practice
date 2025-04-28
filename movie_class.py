'''
Question - 3
m = Movie("Inception", 2010)
print(m)

Movie: Inception (2010)
'''
class Movie:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return f"{self.a} ({self.b})"

m=Movie("Inception",2010)
print(m)
