# Write your solution here


def everything_reversed(words: list):
    rev = words[::-1]
    rev_list = []
    for word in rev:
        rev_list.append(word[::-1])
    return rev_list

if __name__ == "__main__":    
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)