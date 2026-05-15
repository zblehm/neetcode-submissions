from typing import List

def contains_duplicate(words: List[str]) -> bool:
    # if the set has fewer elements then the list had duplicates
    return len(set(words)) < len(words)

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
