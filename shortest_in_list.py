# Write your solution here

def shortest(my_list: list):
    the_shortest = 100
    the_word = ''
    for a in range(len(my_list)):
        len_str = len(my_list[a])
        if len_str < the_shortest:
            the_shortest = len_str
            the_word = my_list[a]
    return the_word

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)