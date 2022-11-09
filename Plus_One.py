n=int(input())
l=list(map(int,input().split()))
s="".join(map(str,l))
s=int(s)+1
s=str(s)
s=list(s)
print(*s)