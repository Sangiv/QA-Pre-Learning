def vowel_swapper(string):
    # ==============
    # Your code here

    # turn string into a list of chars for easy reassignment of vowels
    b = [char for char in string]

    vowels = ['a', 'e', 'i', 'o', 'u']
    new_chars = [4, 3, '!', 'ooo', '|_|']
    count = []

    # replace vowels in list b with appropriate symbol
    for i, j in enumerate(vowels):
        for k, l in enumerate(b):
            if j == l.lower() and count.count(j) == 1 and l == 'O':
                b[k] = '000'
                count.append(j)
            elif j == l.lower() and count.count(j) == 1:
                b[k] = str(new_chars[i])
                count.append(j)
            elif j == l.lower():
                count.append(j)

    # convert the new list b back to string
    ans = ""

    for char in b:
        ans += char

    return ans

    # ==============

print(vowel_swapper("aAa eEe iIi oOo uUu")) # Should print "a/\a e3e i!i o000o u\/u" to the console
print(vowel_swapper("Hello World")) # Should print "Hello Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "Ev3rything's Av/\!lable" to the console
