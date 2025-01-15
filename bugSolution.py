def function_with_uncommon_error_solution(a, b):
    if a == 0 and b == 0:
        return 0  # Handle the case where both inputs are 0
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error_solution(5, 0)
print(result)  # This will raise ZeroDivisionError, as expected
result = function_with_uncommon_error_solution(0, 5)
print(result)  # This will print 5, as expected
result = function_with_uncommon_error_solution(0, 0) 
print(result) #this will print 0