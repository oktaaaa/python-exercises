n = int(input('Please type in a number: '))
 
index = 1
while index <= n:
    if n == index:
        break
    print(index)
    print(n)
    index += 1
    n -= 1
 
if index <= n:
    print(index)