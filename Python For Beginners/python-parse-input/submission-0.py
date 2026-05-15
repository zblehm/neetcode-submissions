from typing import List

def read_integers() -> List[int]:
    list_of_input = input().split(',')
    list_of_ints = [int(x) for x in list_of_input]
    return list_of_ints


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
