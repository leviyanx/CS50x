from cs50 import get_string
import re

# get the string
all_words = get_string("Text: ")

""" get the bumber of L, S """
words_list = list(all_words)

# letters, sentences, words in per hundred words
i = 0  # i'th hundred words
j = 0  # j'th letters in per hundred words
k = 0  # k'th words in per hundred words
s = 0  # s'th sentences in per hundred words
data_per_hundred_words = []
for m, char in enumerate(words_list):
    if re.search(r'[a-zA-Z]', char):
        # letter
        j += 1
    elif char == ' ':
        # word
        k += 1
    elif char == '.' or char == '!' or char == '?':
        # sentence
        s += 1
        # prevent the last word in sentence being not counted by space
        if (m+1) >= len(words_list):
            # this is the last sentence
            k += 1
        # else: exist ' ' after the end of this sentence, means that this is not the last sentence

    # enter a new hundred words
    if k >= 100:
        data = {'letters': j, 'sentences': s, 'words': k}
        data_per_hundred_words.append(data)
        j = 0
        s = 0
        k = 0
        i += 1

    # this is the last word
    if (m+1) >= len(words_list):
        data = {'letters': j, 'sentences': s, 'words': k}
        data_per_hundred_words.append(data)

# calculate L and S
sum_of_letter_per_hundred_words = 0
sum_of_sentence_per_hundred_words = 0
tmp_i = i
while(i > -1):
    sum_of_letter_per_hundred_words += data_per_hundred_words[i]['letters'] / \
        data_per_hundred_words[i]['words']
    sum_of_sentence_per_hundred_words += data_per_hundred_words[i]['sentences'] / \
        data_per_hundred_words[i]['words']
    i -= 1
L = sum_of_letter_per_hundred_words / (tmp_i + 1) * 100
S = sum_of_sentence_per_hundred_words / (tmp_i + 1) * 100

""" calculate the grade """
grade = 0
grade = 0.0588 * L - 0.296 * S - 15.8
# round to the nearest integer
if grade > (int(grade) + 0.5):
    grade_res = int(grade) + 1
else:
    grade_res = int(grade)

"""print the grade"""
if grade_res >= 16:
    print("Grade 16+")
elif grade_res < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade_res}")
