aa1,bb1=map(str,input().split())
x=0
if len(aa1)>len(bb):
   aa1,bb1=bb1,aa1
s=0
while s<len(aa1):
   x+=(ord(bb1[s])-ord(aa1[s]))
   s+=1
for s in range(s,len(bb1)):
   x+=ord(bb1[s])-ord('a')+1
print(x)
