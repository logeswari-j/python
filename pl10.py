log,vel=list(map(str,input().split()))
count=0
for i in range(0,len(vel)):
    if(log[i]!=vel[i]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
