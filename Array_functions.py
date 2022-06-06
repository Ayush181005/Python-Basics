num = [2, 4, 18, 10, 21, 12, 3]
#      0, 1,  2,  3,  4,  5,  6
#      -7,-6,-5, -4, -3, -2, -1
friends = ["Jaimit", "Maanit", "Shrey", "Aarsh", "Ayush", "Kevin"]

friends.extend(num)
print(friends)                                                   #Function to extend the array  
          
friends.append("ASD")
print(friends)                                                   #Function to add one more element in the array in the end

friends.insert(2, "ILD")                                         #Function to add one more element anywhere in the array
print(friends)

friends.remove("Aarsh")                                          #Function to remove any element from the array
print(friends)

friends.clear()                                                  #Function to clear all tha elements of the array
print(friends)

num.pop()                                                        #Function to remove the last element of the array
print(num)

arr2 = ["a","b","c","d", "i", "j", "x", "y", "z", "abc"]

print(arr2.index("d"))                                        #Function to print the index of any element of the array, it can also be used to find that it is or not

print(arr.count("abc")                                       #Function to count how many similar elements are there in the list

love.sort()                                                       #Function to put in alphabetical order
print(love)

num.sort()                                                        #Function to put in ascending order
print(num)

num.reverse()                                                     #Function to reverse the list of array
print(num)

friends2 = friends.copy()                                         #Function to copy all the array elements to another array
print(friends2)
