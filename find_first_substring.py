# Write your solution here
word = input('Please type in a word: ')
char = input('Please type in a character: ')
index = word.find(char)
index_word = index+3
if index >= 0 and index <= 3:
    print(f'{word[index:index_word]}')
