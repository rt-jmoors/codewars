def find_missing_letter(chars):
    for i, char in enumerate(chars[:-1]):
        if ord(char)+1 != ord(chars[i+1]):
            return chr(ord(char)+1)
