

def no_vowels(my_string):
    a = ['a', 'i', 'u', 'e', 'o']
    clean_str = ''
    for i in range(len(my_string)):
        if my_string[i] not in a:
            clean_str += my_string[i]

    return clean_str

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))