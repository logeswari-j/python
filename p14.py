bob,cat=map(int,input().split())
l=list(map(int,input().split()[:bob]))
bob=[]
l.insert(0,0)
for i in range(cat):
    arr=[]
    lxor=0
    wall,pop=map(int,input().split())
    for j in range(wall,pop+1):
        lxor^=l[j]
    bob.append(lxor)
for i in bob:
	print(i)
