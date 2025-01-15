def function_with_uncommon_error(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error(5, 0)
print(result)  # This will raise ZeroDivisionError, as expected
result = function_with_uncommon_error(0, 5)
print(result)  # This will print 5, as expected
result = function_with_uncommon_error(0, 0) 
print(result) #this will print 0, as expected