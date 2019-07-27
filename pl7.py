odd=input()
len=len(odd)
arr=[]
for i in range(0,len,2):
    arr.append(odd[i:i+2][::-1])
print(''.join(arr))
