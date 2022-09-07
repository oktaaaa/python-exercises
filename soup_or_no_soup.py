# Write your solution here
name = input('Please tell me your name: ')

if name != 'Jerry':
    port = int(input('How many portions of soup? '))
    total = float(port*5.90)
    print(f'The total cost is {total}')
print('Next please!')