# Write your solution here

# num = 2
# n = 1
# n2 = 0
# while n2 <= num:
#     n2+=1 
#     print(f'{n} x {n2} = {(n*n2)}')
#     if n2 == num:
#         n+=1
# n2-=num
# for i in range(1,num+1):
    
#     n+=1
#     print(f'{i} x {n} = {(i) * n}')

# 10.16 - 10.49
i = 1

# while i <= num:
#     j = 1
#     print(f"{i} x {j} = {i*j}")   
#     while i <= num:
#         j += 1 
#         print(f"{i} x {j} = {i*j}")
#         i += 1
#     j -= 1

num = int(input('Please type in a number: '))
j = 1

while j <= num:
    i = 1
    while i <= num:
        print(f"{j} x {i} = {i*j}")  
        i+=1
    j += 1
        
        


