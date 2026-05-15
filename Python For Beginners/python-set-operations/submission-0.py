from typing import List

def count_unique_words(words: List[str]) -> int:
    words_without_duplicates = set(words)
    return len(words_without_duplicates)

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
