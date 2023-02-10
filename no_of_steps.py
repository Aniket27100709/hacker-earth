n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
if(len(a)!=len(b)):
    print(-1)
else:
    n=len(a)
    least=min(a)
    count=0

    for i in range(n):
        while a[i]>least:
            a[i]=a[i]-b[i]
            count=count+1
        if a[i]<least:
            least=a[i]
            i=i-1
        elif a[i]<0:
            break
    flag=True
    for i in range(n-1):
        if(a[i]!=a[i+1]):
            flag=False
            break
    if(flag):
        print(count)
    else:
        print(-1)