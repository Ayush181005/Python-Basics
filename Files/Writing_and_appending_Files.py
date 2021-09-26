#This code is for appending a file:-
'''
file = open("Writing and appending_Files.txt", "r")
print(file.read())
file.close()

file = open("Writing and appending_Files.txt", "a")
file.write(input("Enter a line to add in the file:")) #Function for writing in the file
file.close()

file = open("Writing and appending_Files.txt", "r")
print(file.read())
file.close()
'''
#This code is for overwriting the whole file:-
'''
file = open("Writing and appending_Files.txt", "r")
print(file.read())
file.close()

file = open("Writing and appending_Files.txt", "w")
file.write(input("Enter a line to overwrite the file:"))
file.close()

file = open("Writing and appending_Files.txt", "r")
print(file.read())
file.close()
'''
#This code is for writing a new file:-
'''
file = open("Writing and appending_Files2.txt", "w")
file.write(input("Enter a line to write the file:"))
file.close()

file = open("Writing and appending_Files2.txt", "r")
print(file.read())
file.close()
'''
#Like this you can make any type of file for eg. webpage:-

file = open("Sample.html", "w")
file.write("<html><title>I M AYUSH</title><body><h1><i>Hello</i> <del>World</del>!!!</h1><hr><br><br><p>This is <b><u>HTML</u></b> file.</p></body></html>")
file.close()

file = open("Sample.html", "r")
print(file.read())
file.close()