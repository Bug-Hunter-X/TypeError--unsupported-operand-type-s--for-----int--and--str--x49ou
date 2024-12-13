def function(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    elif isinstance(a, int) and isinstance(b, str):
        return a + int(b)
    elif isinstance(a, str) and isinstance(b, int):
        return int(a) + b
    else:
        return "Error: unsupported types"

result = function(5, '10')
print(result)
result2 = function(5,10)
print(result2)
result3 = function('5','10')
print(result3)