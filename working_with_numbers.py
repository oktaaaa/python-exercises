# Write your solution here
print('Please type in integer numbers. Type in 0 to finish.')
attempts = 0
all_num = []
positive_num = 0
negative_num = 0
while True:
    num = int(input('Number: '))
    all_num.append(num)
    attempts+= 1
    
    if num > 0:
        positive_num += 1
    elif num < 0:
        negative_num += 1
    if num == 0:
        attempts-=1
        all_num.remove(0)
        print('... the program asks for numbers')
        print(f'Numbers typed in {attempts}')
        sum_num = sum(all_num)
        mean_num = sum_num/len(all_num)
        print(f'The sum of the numbers is {sum_num}')
        print(f'The mean of the numbers is {mean_num}')
        print(f'Positive numbers {positive_num}')
        print(f'Negative numbers {negative_num}')
        break
    
    

        
