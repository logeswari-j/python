strg11,strg22=list(map(str,input().split()))
count=0
for i in range(0,len(strg22)):
    if(strg11[i]!=strg22[i]):
        count+=1
if(count==1):
    print('yes')
else:
    print('no')
