vowels=["A","E","I","O","U","Y"]
s=input()
if s[2] in vowels:
    print("invalid")
    exit(0)
for i in range(len(s)-1):
    if(s[i].isnumeric() and s[i+1].isnumeric()):
        if((int(s[i])+int(s[i+1]))%2!=0):
            print("invalid")
            exit(0)
print("valid")