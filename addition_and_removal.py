# Write your solution here
lst = []
num = 1

while True:
    print(f'The list is now {lst}')
    choice = input('a(d)d, (r)emove or e(x)it: ')
    
    if choice == 'd':
        lst.append(num)
        num+=1
    elif choice == 'r':
        lst.pop(-1)
        num-=1
    elif choice == 'x':
        break
print('Bye!')
