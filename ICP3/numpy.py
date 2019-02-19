students_python = input("enter list of python students: ")
print(students_python)
students_webapplication = input("enter list of Web Application students: ")
print(students_webapplication)
for item in students_python:
    for item1 in students_webapplication:
        if item == item1:
            print("item")
        else:
            print("No match")
