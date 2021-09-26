monthkeys = {               #Dictionary
    "Jan": "January",   #Keys can also be numbers for eg. 0: "January", or 11: "January", etc.
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

month = input("Enter any name of month to get full name:")
print("You entered "+monthkeys[month])

#Other way:-(Better)
print("You entered "+monthkeys.get(month))         

print("You entered "+monthkeys.get(month, "Value not found in the dictionary!!!"))   #if we use this like this, a default value can be given for invalid values

