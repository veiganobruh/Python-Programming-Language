
string1 = input("String1: ")
string2 = input("String2: ")
string3 = ""

for letra in string1:
    if ( letra not in string2 and  letra not in string3):
        string3 +=letra
for letra in string2:
    if ( letra not in string1 and letra not in string3):
        string3 +=letra
print(string3)