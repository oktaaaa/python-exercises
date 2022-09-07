# Write your solution here

def no_shouting(my_list: list):
    cleaned = []
    for i in range(len(my_list)):
        if my_list[i].isupper() == False:
            cleaned.append(my_list[i])
    return cleaned


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)