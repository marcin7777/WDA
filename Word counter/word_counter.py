import re

words_list = {}

file = open("Pan Tadeusz - tekst.txt", "r", encoding = "utf-8")
for line in file:
    line = line.split(" ")
    for word in line:
        word = re.sub('[\W_]+', '', word.lower())

        if len(word) >= 5 and word != "" and word != None:
            if word in words_list: words_list[word] += 1
            else: words_list[word] = 0
        #end if
    #end for
#end for
file.close()

words_list_sorted = sorted(words_list, key = words_list.get, reverse = True)
for word in words_list_sorted[0: 20]:
    print(word, " - ", words_list[word])
