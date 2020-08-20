def calculator(a, b, operator):
    # ==============
    # Your code here

    ans = 0

    # read operator and execute appropriate function
    if operator == "+":
        ans = int(a + b)
    elif operator == "-":
        ans = int(a - b)
    elif operator == "*":
        ans = int(a * b)
    elif operator == "/":
        ans = int(a / b)

    return bin(ans)[2:]

    # ==============

print(calculator(2, 4, "+")) # Should print 110 to the console
print(calculator(10, 3, "-")) # Should print 111 to the console
print(calculator(4, 7, "*")) # Should output 11100 to the console
print(calculator(100, 2, "/")) # Should print 110010 to the console
