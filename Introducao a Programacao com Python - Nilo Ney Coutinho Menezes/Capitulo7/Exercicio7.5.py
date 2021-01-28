string1 = input("String1:")
string2 = input("String2:")
string3 = ""

for letra in string1:
    if ( letra not in string2):
        string3 +=letra

print(string3)