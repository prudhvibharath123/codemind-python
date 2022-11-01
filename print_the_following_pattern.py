n=int(input())
for i in range(n):
    c=0
    for j in range(n-i):
        c+=1
        print(c,end='')
    print()