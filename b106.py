x1,y2=map(int,input().split())
lm=input().split()
a=[]
for i in lm:
  if (int(i)%2!=0):
    a.append(i)
print(a[y2-1])
