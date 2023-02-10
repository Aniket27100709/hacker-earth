N = int(raw_input())
data = [int(x) for x in raw_input().split()]
for i in range(N):
    last=data[i]%10
if(last%10==0):
    print("Yes")
else:
    print("No")