friends = ["Jim", "Karen", "Kevin"]
for index in range(3, 10):#It will print numbers between 3 and 10, you can also just wright only one number so it will print numbers between that number and zero
    print(index)          #NOTE:The number at the second position, here 10, will not be printed also when a single number is only there
    
len(friends)                                   #This will give the length of the array or more specifically number of elements in the array

for index in range(len(friends)):              #This will print number of elements in the for loop
    print(friends[index])                      #This will access each individual friend's names and print it
    
for index in range(len(friends)):              #This will print the index numbers of the elements in the array 
    print(index) 
    
for index in range(5):
    if index == 0:
        print("It is the first value")
    else: