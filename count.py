"""
a=[1,2,3,4,3,1]
output={
        1:2}
"""

a=[1,2,3,4,3,1]
one=0
two=0
three=0
four=0
for i in a:
    if i==1:
        one=one+1
    if i==2:
        two=two+1
    if i==3:
        three=three+1
    if i==4:
        four=four+1
dict={1:one,2:two,3:three,4:four}
print(dict)

