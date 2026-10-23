s = 'banana'

l = [s[i:j] for i in range(len(s))
     for j in range(i + 1, len(s) + 1)]

d = {i: l.count(i) for i in l}

maxlen = 0
frq = 0
st = ''

for i in d:
    if len(i) > maxlen and d.get(i) > 1:
        maxlen = len(i)
        frq = d.get(i)
        st = i

print("Length =", maxlen)
print("Frequency =", frq)
print("Longest duplicate substring =", st)