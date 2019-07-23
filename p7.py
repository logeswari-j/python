nop3=int(input())
ger=[]
pow=0
for i in range (0,nop3+1):
    pow=abs((2**i)-nop3)
    ger.append(pow)
print(min(ger))
