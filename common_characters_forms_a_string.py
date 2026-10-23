s1 = 'Chinese'
s2 = 'Checkers'
s = ''
a=set(s1)
b=set(s2)

'''for i in a:
    for j in b:
        if i==j:
            s=s+i'''
s = ''.join([i for i in a for j in b if i == j])
#s = ''.join([i for i in a if i in b])
print(s)