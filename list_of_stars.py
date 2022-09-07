# Write your solution here
def list_of_stars(my_list: list):
    for star in my_list:
        print(star*'*')

if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])