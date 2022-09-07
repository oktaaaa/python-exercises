# Write your solution here

words = ''
prev_word = ''

while True:
    word = input('Please type in a word: ')
    
    if word != 'end' and word != prev_word:
        prev_word = word
        words += word + ' '  
    else:
        break
print(words)

