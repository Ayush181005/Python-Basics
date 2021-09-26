#This will just open the file :-
'''
open("reading and basics_Files.txt", "r")
#here, 'r' is for reading files we can write 'w' if we need to write in the file
#We can also write 'a'. It stands for 'append', means you can't change any information of the file but you can add information in the end
#There is one more that is 'r+'. This means read and write. 
'''
#By this we will store the value in a boolean variable and it could only print true or false:-
'''
file = open("reading and basics_Files.txt", "r")

print(file.readable()) #readable is a function in python and it will return a boolyean value, checking that the file is readable or not         
#This will print only true or false(here true) as stored as boolean
#If I put it as 'w' for write mode, it will show false because readable will be false 

file.close() #We have a function/method to close the file, we make sure to also close the file
'''
#By this we will print all the information of the file:-
'''
file = open("reading and basics_Files.txt", "r")

print(file.read()) 

file.close()
'''
#By this we can read individual lines from the files:-
'''
file = open("reading and basics_Files.txt", "r")

print(file.readline()) #First line 
#if we write numbers in the brackets, it will specifically proint that much letters from that line
#For example here if we write 'print(file.readline(3))', so from the first line 'reading and basics_Files' only 'hel' will be printed
print(file.readline())  #printing the second line 

file.close()
'''
#By this we can print all the lines of the file in a form of an array:-
'''
file = open("reading and basics_Files.txt", "r")

print(file.readlines()) #readlines will convert all the lines in an array

file.close()
'''
#By this you can print any particular index of the line converted to the array
'''
file = open("reading and basics_Files.txt", "r")

print(file.readlines()[1]) #readlines will convert all the lines in an array and the index of the array is printed

file.close()
'''
#By this you can print the lines in the file by a for loop:-

file = open("reading and basics_Files.txt", "r")
for line in file.readlines():
    print(line)

file.close()