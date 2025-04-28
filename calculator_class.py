'''
Question - 2
c = Calculator(5, 10)
print(c())   # 15
'''
class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __call__(self):
        c=self.a+self.b
        return c

c=Calculator(5,10)
print(c())


