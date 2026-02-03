character = input("Enter a character:")
if (character in 'aouie'or character in 'AIOUE'):
    print(f"{character} is vowel")
else:
    print(f"{character} is consonant")