is_male = True #Boolean
is_tall = True

if is_male or is_tall:
    print("You are a male or you are tall or both")
    
if is_male and is_tall:
    print("You are both male and tall")
    
elif is_male and not(is_tall):
    print("You are a short male")
    
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
    
else:
    print("You are neither male nor tall")