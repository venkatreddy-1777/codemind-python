n,r=map(int,input().split())
s=1
for i in range(s,r+1):
    if(i%2!=0):
        print(f"{n} x {i} = {n*i}")