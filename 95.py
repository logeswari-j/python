ad,sd=input().split()
ss1=abs(len(sd)-len(ad))
for i in range(len(ad)):
  if(len(sd)==1 and sd[i] in ad):
    break
  if(ad[i]!=sd[i]):
    ss1=ss1+1
print(ss1)
