# Write your solution here

def length_of_longest(my_list: list):
    the_longest = 0
    for a in range(len(my_list)):
        len_str = len(my_list[a])
        if len_str > the_longest:
            the_longest = len_str
    return the_longest
if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)