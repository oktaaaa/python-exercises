# Write your solution here
while True:
    editor = input('Editor: ')
    editor_lower = editor.lower()
    if editor_lower == 'visual studio code':
        print('an excellent choice!')
        break
    elif editor_lower == 'word' or editor_lower == 'notepad':
        print('awful')
    else:
        print('not good')

    
    