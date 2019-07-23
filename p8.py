import math
n11,n22=map(int,input().split())
a=[]
l=list(map(int,input().split()))
for i in range(0,n22):
        a1,b1=map(int,input().split())
        a.append([a1,b1])
for i in a:
        x=i[0]-1
        y=i[1]-1
        print(math.gcd(l[x],l[y]))
