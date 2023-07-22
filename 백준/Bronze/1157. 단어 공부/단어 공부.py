import sys

word = list(map(str, sys.stdin.readline().rstrip().upper()))

word_count = {}
for w in word:
    word_count[w] = word_count.get(w, 0) + 1

len_list = []
for k, v in word_count.items():
    if max(word_count.values()) == v:
        len_list.append(k)

if len(len_list) == 1:
    print(len_list[0])
else:
    print('?')