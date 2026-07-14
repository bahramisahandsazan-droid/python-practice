word = input(' give me one word :')
def is_palindrome(word) :
    if word == word[::-1] :
        return True
    else :
        return False
a = is_palindrome(word)
print(a)
