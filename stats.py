def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    num_chars = {}
    for c in text:
        c_minsc = c.lower()
        if c_minsc in num_chars:
            num_chars[c_minsc] += 1
        else:
            num_chars[c_minsc] = 1
    return num_chars