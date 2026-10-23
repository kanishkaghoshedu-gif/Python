from collections import defaultdict
def group_anagrams(words):
    groups = defaultdict(list)
    print(groups)
    for x in words:
        key = ''.join(sorted(x))
        groups[key].append(x)
    print(groups)
    return list(groups.values())
words = ["eat", "tea", "bat", "nat", "tan", "ate"]
print(group_anagrams(words))

