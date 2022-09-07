# Write your solution here

post_int = int(input('Please type in a positive integer: '))

'''for num in range(post_int, -post_int):
    print(num)'''

for i in range(-post_int,post_int+1,1):
    if i == 0:
        continue
    print(i)