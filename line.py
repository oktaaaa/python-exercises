# Write your solution here
# You can test your function by calling it within the following block
def line(num, word):
    if word == '':
        print(num*'*')
    else:
        print (num*word[0])
if __name__ == "__main__":
    line(5, "xxx")
    line(3, "")