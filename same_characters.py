# Write your solution here
# You can test your function by calling it within the following block

def same_chars(word, ar1, ar2):
    if ar1 >= len(word) or ar2 >= len(word):
        return False
    return word[ar1] == word[ar2]
    

if __name__ == "__main__":
    print(same_chars("coder", 12, 1))
    print(same_chars("abc", 0, 3))