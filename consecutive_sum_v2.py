limit = int(input('Limit: '))
num = 1
base = 1
sum = 'The consecutive sum: 1'
while base < limit:
    num +=1
    base += num
    sum += f' + {num}'
    
    

print(f'{sum} = {base}')