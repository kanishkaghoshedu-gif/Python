n = int(input("Enter size: "))
lst = [input() for _ in range(n)]
print(lst)
l=[]
l = [sum(int(x) for x in i.split()) for i in lst]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            t=l[i]
            l[i]=l[j]
            l[j]=t
            k=lst[i]
            lst[i]=lst[j]
            lst[j]=k
for i in range(len(l)):
      print(lst[i], l[i])                     