g11,g22=input().split()
n1=abs(len(g22)-len(g11))
for i in range(len(g11)):
 if(len(g22)==1 and g22[i] in g11):
  break
 if(g11[i]!=g22[i]):
  n1=n1+1
print(n1)
