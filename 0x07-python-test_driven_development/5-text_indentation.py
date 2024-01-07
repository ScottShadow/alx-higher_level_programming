#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    replace_chars = ['.', '?', ':']
    for char in replace_chars:
        text = text.replace(f'{char} ', f'{char}')
    for char in replace_chars:
        text = text.replace(f'{char}', f'{char}\n\n')
    print(text, end="")
