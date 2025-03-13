def power(a, b):
    result = 1
    base = a  # First extra variable
    exponent = b  # Second extra variable

    while exponent > 0:
        result *= base
        exponent -= 1

    return result
a = 8
b = 5
print(power(a, b))  
