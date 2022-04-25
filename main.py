
new_word_list = []
file = open("dictionary_words.txt", "r")
words = file.readlines()
for word in words:
    new_word = word.split('\n')[0]
    new_word_list.append(new_word)

five_letter_words = [word for word in new_word_list if len(word)==5]
print(f'Out of {len(new_word_list)} words in the dictionary, there are {len(five_letter_words)} five letter words.')

###### USER INPUTS
wordle_char = input('CONDITION 1: what letters does the word have?    ')
doesnt_have = input('CONDITION 2: what characters arent in the word? (optional)    ')
doesnt_start = input('CONDITION 3: what characters doesnt start the word? (optional)    ')

### BASE CONDITION
correct_letters = list(wordle_char)
possible_words = [word for word in five_letter_words if all(letter.lower() in word for letter in correct_letters)]
print(f'BASE CONDITION: There are {len(possible_words)} possible words.')
print(possible_words)

### CONDITION 2
wrong_letters = list(doesnt_have)
more_accurate = [word for word in possible_words if all(letter.lower() not in word for letter in wrong_letters)]
print(f'CONDITION 2: There are {len(more_accurate)} words that fit this condition.')
print(more_accurate)

### CONDITION 3
most_accurate = []
notstart_letter = list(doesnt_start)
for letter in notstart_letter:
    for word in more_accurate:
        if not word.startswith(letter.lower()):
            most_accurate.append(word)
if most_accurate:
    print(f'CONDITION 3: There are {len(most_accurate)} words that fit this condition.')
    print(most_accurate)
if not most_accurate:
    print('CONDITION 3: No letters were provided.')

#### if you know a correct position of a letter in the word, you can further target the outcomes ### CONDITION 4
if most_accurate:
    x = [word for word in most_accurate if word[4] == 'e' and word[1]=='a']
    print(f'CONDITION 4: There are {len(x)} words that fit this condition.')
    print(x)
if not most_accurate:
    x = [word for word in more_accurate if word[4] == 'e' and word[1]=='a']
    print(f'CONDITION 4: There are {len(x)} words that fit this condition.')
    print(x)


