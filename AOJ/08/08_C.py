import sys

texts = sys.stdin.read()
texts = texts.lower()
list_count = []
small = [chr(j) for j in range(97, 123)]

for i in range(26):
    list_count.append(texts.count(small[i]))

for m in range(26):
    print(small[m] + " : " + str(list_count[m]))
