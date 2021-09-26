def exponent(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num   
    return result

print(exponent(2, 3))