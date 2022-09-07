# Write your solution here
age = int(input('What is your age? '))
age_str = str(age)
if(age >= 5):
    print(f'Ok, you\'re {age_str} years old')
elif(age < 0):
    print('That must be a mistake')
else: 
    print('I suspect you can\'t write quite yet...')