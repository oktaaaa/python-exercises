# Write your solution here
the_item = []

while True:
    item = int(input('New item: '))
    if item == 0:
        break
    the_item.append(item)
    
    ordered_list = sorted(the_item)
    print(f'The list now: {the_item}')
    print(f'The list in order: {ordered_list}')
    
print('Bye!')
    