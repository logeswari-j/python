rgv7,rgv2=map(int,input().split())
mrk=list(map(int,input().split()[:rgv7]))
rk=0
for i in mrk:
   if(i==rgv2):
      rk=rk+1
print(rk)
