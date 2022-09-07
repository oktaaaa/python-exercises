# Write your solution here

word = input('Please type in a string: ')
vowel = ['a', 'e', 'o']

for i in vowel:
    if i in word:
        print(f'{i} found')
    else:
        print(f'{i} not found')