import sys

word = list(map(str, sys.stdin.readline().rstrip()))

# 1. 소문자를 다 소문자로 바꾼다.
for i, w in enumerate(word):
    order_num = ord(w) - 97
    if 97 <= ord(w) <= 122:
        w = chr(order_num + 65)
        word[i] = w


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