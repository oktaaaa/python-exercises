limit = int(input('Limit: '))
num = 1
base = 0
sum = 'The consecutive sum: '
while base < limit:
    sum += f'{num} + '
    base += num
    num +=1
sum+= f'= {base}'
print(sum)