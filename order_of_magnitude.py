# Write your solution here
num = int(input('Please type in a number: '))
less_10 = 'This number is smaller than 10'
less_100 = 'This number is smaller than 100'
less_1000 = 'This number is smaller than 1000'
if num < 1000:
    print(less_1000)  
if num < 100:
    print(less_100) 
if num < 10:
    print(less_10)
    
print('Thank you!')
