x=int(input())
n=0
i=0
while(x>0):
    i=x%10
    n=n+i
    x=x//10
print(n)
