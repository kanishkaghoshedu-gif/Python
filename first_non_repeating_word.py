# def non_repeating_words(l):
#     st=''
#     dict = {i:l.count(i) for i in l }
#     print(dict)
#     st=" ".join([i for i in dict if dict.get(i) == 1])
#     return st
    

# st = "java python java c python sql c"
# l = st.split()
# print(non_repeating_words(l))

def non_repeating_words(l):
    d = {}

    for word in l:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    st = " ".join([word for word in d if d[word] == 1])
    return st


st = "java python java c python sql c"
l = st.split()

print(non_repeating_words(l))