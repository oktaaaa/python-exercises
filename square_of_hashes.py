# Write your solution here
def hash_square(length):
    width = ('#' * length)
    
    for x in range(length):
        print(width)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)