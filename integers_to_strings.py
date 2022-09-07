# Write your solution here

def formatted(my_list: list):
    numies = []
    for num in my_list:
        numies.append(f'{num:.2f}')
    return numies

if __name__ == "__main__":
    my_list = [1.234, 0.3333, 0.11111, 3.446]
    new_list = formatted(my_list)
    print(new_list)