# Write your solution here
f_degree = int(input('Please type in a temperature (F): '))

celcius = float((f_degree - 32) * 5/9)
print(f'{f_degree} degrees Fahrenheit equals {celcius} degrees Celsius')
if celcius < 0:
    print(f'Brr! It\'s cold in here!')
