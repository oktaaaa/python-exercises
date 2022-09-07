# Write your solution here
point = int(input('How many points [0-100]: '))
grade = ''

if point < 0 or point > 100:
    grade = 'impossible!'
elif point < 50:
    grade = 'fail'
elif point < 60:
    grade = '1'
elif point < 70:
    grade = '2'
elif point < 80:
    grade = '3'
elif point < 90:
    grade = '4'
else:
    grade = '5'  

print(f'Grade: {grade}')     