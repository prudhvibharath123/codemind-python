n=int(input())
l=list(map(int,input().split()))
k=0
e=0
for i in l:
    if i%2==0:
        e=e+1
    else:
        k=k+1
print(e,k)