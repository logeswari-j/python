dk=int(input())
ak1=[]
for i in range(0,dk):
 de=input()
 ak1.append(de)
nn=[]
for i in zip(*ak1):
 if(i.count(i[0])==len(i)):
  nn.append(i[0])
 else:
  break
print(''.join(nn))
© 2019 GitHub, Inc.
