intg1=int(input())
nums=list(map(int,input().split()))
o=0
for i in range(0,intg1-2):
	for j in range(1,intg1-1):
		for k in range(2,intg1):
			if(nums[i]<nums[j] and nums[j]<nums[k]):
				o+=1
print(o)
