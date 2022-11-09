a,b=map(int,input().split())
l1=[]
for i in range(a):
    l=list(map(int,input().split()))
    l1.append(l)
for i in range(a):
    c=0
    for j in range(b):
        if c < l1[j][i]:
            c=l1[j][i]
    print(c)
