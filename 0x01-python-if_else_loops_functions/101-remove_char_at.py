def remove_char_at(str, n):
    if 0 <= n < len(str):
        newWord = str[:n] + str[n+1:]
        return newWord
    else:
        return str
