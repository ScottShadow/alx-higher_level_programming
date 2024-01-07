#!/usr/bin/python3
def text_indentation(text):
    replace_chars = ['.', '?', ':']
    for char in replace_chars:
        text = text.replace(f'{char} ', f'{char}')
    for char in replace_chars:
        text = text.replace(f'{char}', f'{char}\n\n')
    print(text, end="")
