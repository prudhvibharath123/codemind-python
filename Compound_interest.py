P,R,T=map(int,input().split())
M=P*(pow((1+R/100),T))
print("{:.2f}".format(M))