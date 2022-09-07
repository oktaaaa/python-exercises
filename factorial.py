# Write your solution here
while True:
    num = int(input('Please type in a number: '))
    factorial = 1

    if num == 0 or num < 0:
        print('Thanks and bye!')
        break
    else:
        for i in range(1, num+1):
            factorial = factorial * i
        print(f'The factorial of the number {num} is {factorial}')