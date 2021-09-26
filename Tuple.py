coordinates = (4, 5)            #Its like an array(value of 1st element is 0 and value of 2nd element is 1) and cannot be changed once declared

print(coordinates[1])

#NOTE:THE MAIN DIFFERENCES BETWEEN TUPLE AND LISTS(ARRAY) IN PYTHON IS THAT
#     1) WE USE [] IN A LIST NOT () LIKE A TUPLE FOR DECLARATION
#     2) WE CAN CHANGE THE VALUE AFTERWARDS IN A LIST BUT NOT IN A TUPLE 

coordinates2 = [(4, 5), (6, 7), (2, 18)]            #List of tuples
print(coordinates2)