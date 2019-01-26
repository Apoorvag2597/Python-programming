stringcount=input("enter the string:")
digits=0
words=0
letters=0
for i in stringcount:
    if i.isdigit():
        digits=digits+1
    if i.isalpha():
        letters=letters+1
print("digits count:",digits)
print("letters count:",letters)
print("words count:",len(stringcount.split()))