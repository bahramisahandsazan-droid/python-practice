word =input('give me your word : ')
new_word = ''
for i in range(0,len(word)) :
    if word[i] == 'z':
        new_word = new_word + 'a'
    else:
        b = ord(word[i])+1
        new_word = new_word + chr(b)
print(new_word)
