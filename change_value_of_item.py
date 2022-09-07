# Write your solution here
the_list = [1, 2, 3, 4, 5]
while True:
    index = int(input('Index: '))
    if index == -1:
        break
    new_val = int(input('New Value: '))
    the_list[index] = new_val
    
    print(the_list)