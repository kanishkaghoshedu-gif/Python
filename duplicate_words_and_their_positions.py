def non_repeating_words(l):
    d = {}

    for word in l:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1

    st = [word for word in d if d[word] > 1]

    for word in st:
         lst = []

         for index, value in enumerate(l):
              if value == word:
                  lst.append(index)

         print(word, lst)

st = "java python java c python sql c"
l = st.split()

non_repeating_words(l)