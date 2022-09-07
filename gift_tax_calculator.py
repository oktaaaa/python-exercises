# Write your solution here
val_gift = int(input('Value of gift: '))
tax = float(0)
if val_gift < 5000:
    print('No tax!')
elif val_gift <= 25000:
    tax = 100 + (val_gift - 5000) * 0.08
    print(f'Amount of tax: {tax} euros')
elif val_gift <= 55000:
    tax = 1700 + (val_gift - 25000) * 0.1
    print(f'Amount of tax: {tax} euros')
elif val_gift <= 200000:
     tax =4700 + (val_gift - 55000) * 0.12
     print(f'Amount of tax: {tax} euros')
elif val_gift <= 1000000: 
    tax = 22100 + (val_gift - 200000) * 0.15
    print(f'Amount of tax: {tax} euros')
else:
    tax =142100 + (val_gift - 1000000) * 0.17
    print(f'Amount of tax: {tax} euros')


