sentence = input('give me yours sentence : ')
no_space = sentence.replace(' ','')
letter_counter = len(no_space)
print(letter_counter)
words = sentence.split()
print(words)
words_count = len(words)
print(words_count)
letter_freq ={}
for letter in no_space :
    if letter in letter_freq :
        letter_freq[letter]=letter_freq[letter]+1
    else :
        letter_freq[letter] = 1
print(letter_freq)
longest_word =words[0]
for word in words :
    if len(word) > len(longest_word) :
        longest_word = word
print(longest_word)
