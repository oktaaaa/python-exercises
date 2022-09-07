# Write your solution here

word = []
count = 0

while True:
    w = input('Word: ')
    
    count +=1
    if w in word:
        count -=1
        break
    word.append(w)
print(f'You typed in {count} different words')