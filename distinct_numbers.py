# Write your solution here

def distinct_numbers(my_list: list):
    diff = []
    for i in my_list:
        if i not in diff:
            diff.append(i)
    return sorted(diff)

if __name__ == "__main__": 
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))