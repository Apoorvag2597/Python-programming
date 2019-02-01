x=int(input("enter 1st number"))
y=int(input("enter second number"))
final=[]
for i in range(x,y):
     s=str(i)
     if (int(s[0]) % 2 != 0) and (int(s[1]) % 2 != 0) and (int(s[2]) % 2 != 0):
        final.append(s)

print(final)
