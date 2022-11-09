n=int(input())
c=0
l=list(map(int,input().split()))
for i in l:
  if l.count(i)>c:
      c=l.count(i)
      b=i
print(b)