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

def sort_chars(chars): 
    sorted_list = []
    def sort_on(dict):
        return dict["Number"]
    for char in chars:
        sorting_dict = {}
        sorting_dict["Letter"] = char
        sorting_dict["Number"] = chars[char]
        sorted_list.append(sorting_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
