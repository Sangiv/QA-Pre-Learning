def vowel_swapper(string):
    # ==============
    # Your code here

    # turn string into a list of chars for easy reassignment of vowels
    b = [char for char in string]

    vowels = ['a', 'e', 'i', 'o', 'u']
    new_chars = [4, 3, '!', 'ooo', '|_|']

    # replace vowels in list b with appropriate symbol
    for i, j in enumerate(vowels):
        for k, l in enumerate(b):
            if j == l.lower():
                b[k] = str(new_chars[i])
            elif l == "O":
                b[k] = "000"

    # convert the new list b back to string
    ans = ""

    for char in b:
        ans += char

    return ans

    # ==============


print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console
