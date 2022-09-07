# Write your solution here

itm = int(input('How many items: '))

saved_num = []
for x in range(itm):
    item_num = int(input(f'Item {x+1}: '))
    saved_num.append(item_num)
print(saved_num)