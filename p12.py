intg11,intg22=map(int,input().split())
l=list(map(int,input().split()[:intg1]))
arr=[]
for i in range(intg22):
	intg33,intg44=list(map(int,input().split()))
	arr.append(sum(l[intg33-1:intg44]))
for j in arr:
	print(j)
