def get_num_words(text):
    """
    Counts the number of words in the text.
    """
    num_words = len(text.split())
    return num_words

def get_char_count(text):
    """
    Counts the frequency of each character in the text.
    Returns a dictionary mapping characters to their counts.
    All characters are converted to lowercase.
    """
    char_count = {}
    for char in text.lower():
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

def get_sorted_char_counts(char_count_dict):
    """
    Takes a dictionary of character counts and returns a sorted list of dictionaries.
    Each dictionary contains the character and its count.
    The list is sorted from highest count to lowest count.
    """
    char_list = []
    for char, count in char_count_dict.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list


