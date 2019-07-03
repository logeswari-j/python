r1,r2=map(int,input().split())
for i in range(r1,r2):
 if r3>1:
  for i in range(2,r3):
   if(r3%i)==0:
    break
  else:
   print(r3,end=" ")
