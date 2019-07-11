x1,y2=map(int,input().split())
if(x1>y2):
  great=x1
else:
  great=y2
while(True):
  if((great%x1) == 0 and (great%y2) == 0):
    lcm=great
    break
  great=great+1
print(lcm)
