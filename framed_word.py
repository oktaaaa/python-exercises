# Write your solution here

word = input("Word: ")
center = 28 - len(word)
left = center // 2
right = center // 2
total_lines = left + right + len(word)

frame = 30*'*'
even_words = '*' + ' ' * left + word + ' ' * right+ '*'
odd_words = '* ' + ' ' * left + word + ' ' * right+ '*'


print(frame)
if total_lines % 2 == 0:
    print(even_words)
elif total_lines % 2 != 0:
    print(odd_words)
print(frame)