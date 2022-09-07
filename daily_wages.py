# Write your solution here

wage_perhour = float(input('Hourly wage: '))
work_hour = int(input('Hours worked: '))
day_week = input('Day of the week: ')
daily_wage = 0

if day_week == 'Sunday' or  day_week == 'sunday':
    daily_wage = 2 * (wage_perhour * work_hour)
else:
    daily_wage = wage_perhour * work_hour

print(f'Daily wages: {daily_wage} euros')
 
