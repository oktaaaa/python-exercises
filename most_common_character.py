# Write your solution here
def most_common_character(strings):
    max_str = {}
    for i in strings:
        if i in max_str:
            max_str[i] += 1
        else:
            max_str[i] = 1
    return max(max_str, key=max_str.get)

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
