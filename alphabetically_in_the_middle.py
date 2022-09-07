# Write your solution here

first_char = input('1st letter: ')
second_char = input('2nd letter: ')
third_char = input('3rd letter: ')

chars = [first_char, second_char, third_char]
sorted_char = sorted(chars)
middle_char = sorted_char[1]
print(f'The letter in the middle is {middle_char}')

