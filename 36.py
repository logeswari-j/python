str=input()
s1=0
for i in range(len(str)):
  if(str[i].isdigit() or str[i].isalpha() or str[i]==(" ")):
    continue
  else:
   s1+=1
print(s1)
