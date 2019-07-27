c1,b2=map(int,input().split())
intg=list(map(int,input().split()[:b2]))
a=[]
for i in intg:
   if(i<=i+1):
     a.append(i)
print(a[b2-1]) 
