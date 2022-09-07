# Write your solution here
strings = input('Please type in a string: ')
len_str = len(strings)
for i in range(len_str):
    i-= len_str
    print(strings[-(i+1):])