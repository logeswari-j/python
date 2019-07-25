a11,b22,c33=map(int,input().split())
aps=0
for i in range(0,c33):
   aps=aps+a11
   a11=a11+b22
print(aps)
