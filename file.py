s = input("Enter a string: ")
i = 0
c = 0
while i < len(s):
    if s[i].lower() in "bcdfghjklmnpqrstvwxyz":
        c = c + 1
    i = i + 1
print("The number of consonants in the string is:", c)