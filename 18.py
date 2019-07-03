r1,r2=map(int,input().split())
for r3 in range(r1+1,r2):
  choose=r3
  friend=0
  while (r3>0):
    r=r3%10
    friend=friend+(r**3)
    r3=r3//10
    if(friend==choose):
      print(friend,end=" ")
