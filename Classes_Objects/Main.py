from Student import Student                   # Its telling to import Student class from Student file

Student1 = Student("Dhairya", 10, True)       # Here Student is just an Object
# We can create as many objects as we want like this(Here we can create as many students as we want)

# Like this each of the components of the object can be accessed: -
print("The name of the student is: "+Student1.name)
print("The student is in grade: "+str(Student1.standard))
print("The student is in board year or not: "+str(Student1.is_in_board_year))
