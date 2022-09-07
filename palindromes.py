def palindromes(word: str):
    word_reverse = word[::-1]
    if word == word_reverse:
        return True
    return False
        
def input_word():
    
    while True:
        word = input('Please type in a palindrome: ')
        if palindromes(word):
            print(f'{word} is a palindrome!')
            break
        else:
            print('that wasn\'t a palindrome')
            
input_word()