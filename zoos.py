s=input()
if(len(s)<20):
    Zc=s.count('z')
    Oc=s.count('o')
    if(Zc*2==Oc):
        print('Yes')
    else:
        print('No')