studMarks = {}
for i in range(5):
    name = input("Enter the name:");
    mark = input("Enter the mark:");
    studMarks[name] = mark
print(max(studMarks))
