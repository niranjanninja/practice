data = {
    "Alice": {"Math": 80, "Science": 90},
    "Bob": {"Math": 75, "Science": 85}
}

# Task: Calculate total of all scores.
# Output: 330

temp=0
for name,info in data.items():
    for sub,mark in info.items():
        temp=temp+mark
print(temp)

