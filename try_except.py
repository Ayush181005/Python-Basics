#For all errors :-

'''                                                                                 
try:
    num = int(input("Enter an integer: "))
    print("You entered {0}".format(num))
except:
    print("INVALID VALUE!!!")
'''

#For specific types of errors :-

'''
try:
    value = 10/0 #This will give the error of dividing by zero -- If this line of code not there, so other things will happen like invalid value on wrong no. and correct on right
    num = int(input("Enter an integer: "))
    print("You entered {0}".format(num))
except ZeroDivisionError:
    print("DIVIDED BY ZERO!!!")
    
except ValueError:
    print("INVALID VALUE!!!")
'''

#For using the error as a variable

try:
    value = 10/0 
    num = int(input("Enter an integer: "))
    print("You entered {0}".format(num))
except ZeroDivisionError as err:      #Using the error as a variable
    print(err)           #Printing actual error
    
except ValueError:
    print("INVALID VALUE!!!")