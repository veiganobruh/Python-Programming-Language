l = [5,9,13]
x= 0
for e in l:
    print("[%d] %d"%(x,e))
    x=x+1


print()
print()
print()

for x, e in enumerate(l):
    print("[%d] %d "%(x,e))