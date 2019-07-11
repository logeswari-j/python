s=list(input())
if len(s)%2==0:
    s[int(len(s)/2)]='*'
    s[int(len(s)/2)-1]='*'
else:
    s[int(len(s)/2)]='*'
for i in range(len(s)):
    print(s[i],end='')
