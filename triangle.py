# Copy here code of line function from previous exercise
def line(num, word):
    if word == '':
        print(num*'*')
    print (num*word[0])

def triangle(size):
    # You should call function line here with proper parameters
    for x in range(size):
        line(x+1, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
