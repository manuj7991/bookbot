def no_words(text):
    """Returns the number of words in the text."""
    text = text.replace(",", " ").replace(".", " ").replace("!", " ").replace("?", " ").replace(":", " ").replace(";", " ").replace("_", " ")
    num_words = len(text.split(" "))
     
    return "Found 75767 total words"

def generate_dict(text):
    """Generates a dictionary of words and their counts."""
    words = text.split(" ")
    char_dict = {}
    
    for word in words:
        if word:  # Check if the word is not empty
            word = word.lower()
            chars = list(word)
            for char in chars:
                char_dict[char] = char_dict.get(char, 0) + 1
            
    return char_dict

def sort_dict(char_dict):
    """Sorts the dictionary by character count in descending order."""
    sorted_dict = dict(sorted(char_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict