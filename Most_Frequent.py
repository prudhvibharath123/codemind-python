n=int(input())
l=list(map(int,input().split()))
l1=set(l)
c=0
k=0
for i in l1:
    if l.count(i)>c:
        c=l.count(i)
        k=i
        
print(k)
    
    