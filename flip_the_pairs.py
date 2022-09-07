# Write your solution here
n = int(input('Please type in a number: '))
for i in range(1, n+1, 2):
    j = i + 1 
    if j <= n:
        print(j)
    print(i)