g1,g2=map(int,input().split())
for g in range(g1+1,g2):
 sum=0
 temp=g
 while temp>0:
  digit=temp%10
  sum+=digit**3
  temp//=10
 if g==sum:
    print(g,end=" ")
