M=int(input())
N=int(input())
l1=[]
sum=0
for i in range(M):
    l=list(map(int,input().split()))
    l1.append(l)
for i in range(M):
    for j in range(N):
        sum=sum+l1[i][j]
print(sum)
        