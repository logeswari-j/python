hh3,pp=input().strip().split()
pp=int(pp)
h=0
while h<len(hh3)-1 and pp:
 if(hh3[h]>hh3[h+1]):
  pp-=1
  hh3=hh3[:h]+hh3[h+1:]
  if(h!=0):
   h-=1
 else:
  h+=1
lk=hh3[:len(hh3)-pp]
print(lk)
