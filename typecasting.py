# Write your solution here
import math
num = float(input('Please type in a number: '))
num_int = int(num)
decimal = math.modf(num)
print(f'Integer part: {num_int}')
print(f'Decimal part: {decimal}')