from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    word_count_dict = {}
    
    for char in word:
        # increment the count if the character is already a key
        if char in word_count_dict:
            word_count_dict[char] += 1
        # if char is not a key, add it with a count of 1
        else:
            word_count_dict[char] = 1
    
    return word_count_dict




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
