# Write your solution here

p1 = input('Password: ')
while True:
    
    p2 = input('Repeat password: ')

    if(p1 == p2):
        break
    print('They do not match!')
print('User account created!')