god,great=input().split()
cost=abs(len(great)-len(god))
for i in range(len(god)):
    if(len(great)==1 and great[g] in god):
        break
    if (god[g]!=great[g]):
        cost=cost+1
print(cost)
