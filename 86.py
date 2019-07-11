xx=list(input())
yy=[]
for j in xx:
   if j not in yy:
      yy.append(j)
if xx==yy:
   print("Yes")
else:
   print("No")
