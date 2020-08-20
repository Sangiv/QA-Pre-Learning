def factors(number):
    # ==============
    # Your code here

    factors = []

    # checks for factors and appends to list 'factors'
    for i in range(2, number):
        if number % i == 0:
            factors.append(i)

    if len(factors) > 0:
        return factors
    else:
        return f"{number} is a prime number"

    # ==============

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “13 is a prime number”
