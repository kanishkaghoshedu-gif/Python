def swap(l,i,j):
    t=l[i]
    l[i]=l[j]
    l[j]=t
    
l=[4,3,7,8,6,2,1]

flag=True
for i in range(len(l)-1):
    if(flag):
        if(l[i]>l[i+1]):
            swap(l,i,i+1)
    elif(l[i]<l[i+1]):
        swap(l,i,i+1)
    flag=not flag
print(l)        