N=int(input())
K=ord("A")
for i in range(N):
    K=ord("A")+i
    for j in range(N):
        print(chr(K),end=" ")
    print()
    