book,bag=map(str,input().split())
for i in range(len(book)):
    if(book.count(book[i])==bag.count(bag[i])):
        print("yes")
        break
    else:
        print("no")
        break
