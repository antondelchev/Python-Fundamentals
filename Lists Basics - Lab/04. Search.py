n = int(input())
word = input()

sentences_list = []
selected_list = []

for i in range(1, n + 1):
    sentence = input()
    sentences_list.append(sentence)

print(sentences_list)

for i in range(len(sentences_list)):
    if word in sentences_list[i]:
        selected_list.append(sentences_list[i])

print(selected_list)
