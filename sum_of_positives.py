# Write your solution here
def sum_of_positives(the_list: list):
    post = []
    for num in the_list:
        if num >= 0:
            post.append(num)
    return sum(post)

if __name__ == "__main__": 
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)