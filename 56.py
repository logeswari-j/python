log=input()
for i in range(0,len(log)):
   if(log[i].isalpha() and log[i].isdigit()):
    print("No")
else:
  print("Yes")
