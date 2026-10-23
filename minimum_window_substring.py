s = "ADOBECODEBANC"
t = "ABC"
lst=list(t)
l = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
print(l)
l1 = [i for i in l if all(x in i for x in t)]
print(sorted(l1,key=len)[0])
