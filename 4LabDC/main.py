dictionary_full = open('dict1.txt').read()
text = open('brain267.txt').read()
j = 0

text = text.replace(",", " ")
text = text.replace(")", " ")
text = text.replace("!", " ")
text = text.replace("—", " ")
text = text.replace("?", " ")
text = text.replace(".", " ")
text = text.replace("(", " ")
text = text.replace("«", " ")
text = text.replace("»", " ")


dictionary_full = dictionary_full.split()
dictionary = []
i = 0
while i < len(dictionary_full):
    dictionary.append(dictionary_full[i])
    i = i + 2

text = text.lower()
text = text.split()
print(text)

print("Количество словоформ: " + str(len(text)))

different_words = []

for i in text:
    if different_words.count(i) == 0:
        different_words.append(i)

print("Количество разных словоформ: " + str(len(different_words)))

num_of_exist_words = 0
num_of_unexist_words = 0

for i in different_words:
    if dictionary.count(i) != 0:
        num_of_exist_words += 1
    else:
        num_of_unexist_words += 1

print("количество слов, присутствующих в словаре: " + str(num_of_exist_words) +
      "\nКоличество слов, которых нет в словаре: "
      + str(num_of_unexist_words))
k = 0
incorrect_words = []

for i in different_words:
    if dictionary.count(i) == 0:
        min_dist = 3
        correct = 0
        for j in dictionary:
            dist = 0
            if abs(len(i) - len(j) <= 2):
                k = 0
                z = 0
                while (k < len(i)) & (z < len(j)):
                    if i[k] == j[z]:
                        k += 1
                        z += 1
                    else:
                        z += 1
                        dist += 1
                if dist < min_dist:
                    min_dist = dist
                    correct = j
        if min_dist < 3:
            incorrect_words.append(["найдено", 0, i, correct, min_dist])
        else:
            incorrect_words.append((["не найдено", 0, i]))

text = open('brain267.txt').read()
for i in incorrect_words:
    i[1] = text.count(i[2])

incorrect_words.sort(key=lambda incorrect_words: incorrect_words[1])
incorrect_words.sort(key=lambda incorrect_words: incorrect_words[0])

print(incorrect_words)

text = open('brain267.txt').read()

for i in incorrect_words:
    if i[0] != "не найдено":
        text = text.replace(i[2], i[3])

print(text)

text = text.replace(",", " ")
text = text.replace(")", " ")
text = text.replace("!", " ")
text = text.replace("—", " ")
text = text.replace("?", " ")
text = text.replace(".", " ")
text = text.replace("(", " ")
text = text.replace("«", " ")
text = text.replace("»", " ")
text = text.lower()
text = text.split()
print("Количество словоформ: " + str(len(text)))
different_words.clear()
for i in text:
    if different_words.count(i) == 0:
        different_words.append(i)
print("Количество разных словоформ: " + str(len(different_words)))
num_of_exist_words = 0
num_of_unexist_words = 0
for i in different_words:
    if dictionary.count(i) != 0:
        num_of_exist_words += 1
    else:
        num_of_unexist_words += 1

print("количество слов, присутствующих в словаре: " + str(num_of_exist_words) +
      "\nКоличество слов, которых нет в словаре: "
      + str(num_of_unexist_words))
