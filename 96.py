a11,b22=map(str,input().split())
y=0
if len(a11)>len(b22):
	a11,b22=b22,a11
p=0
while p<len(a11):
	  y+=(ord(b22[p])-ord(a11[p]))
	  p+=1
for p in range(p,len(b22)):
	  y+=ord(b22[p])-ord('a')+1
print(y)
