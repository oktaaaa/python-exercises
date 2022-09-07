word = input("Please type in a word: ")
char = input("Please type in a character: ") 
index = word.find(char)
while index!=-1:
    if len(word)>=index+3:
        print(word[index:index+3])
    index = word.find(char,index+1)