gb=int(input())
for i in range(2,gb):
    if gb%i==0:
        print("yes")
        break
else:
    print("no")
