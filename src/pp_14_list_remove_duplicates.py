import random
from typing import List

def create_random_list() -> List[int]:
    """creates random list

    Returns:
        list: sorted random list
    """
    random_list = []
    for _ in range(0, 13):
        n = random.randint(1, 20)
        random_list.append(n)
        random_list.sort()
    return random_list

rnd_list = create_random_list()
print(rnd_list)


def delete_duplicates_set(input_list: List[int]) -> List[int]:
    """deletes duplicates with set

    Args:
        input_list (list): input list with duplicates

    Returns:
        list: input list without duplicates
    """
    list_wo_duplicates = list(set(input_list))
    return list_wo_duplicates

no_duplicates_set = delete_duplicates_set(rnd_list)
print(no_duplicates_set)


def delete_duplicates_loop(input_list: List[int]) -> List[int]:
    """deletes duplicates with loop

    Args:
        input_list (list): input list with duplicates

    Returns:
        list: input list without duplicates
    """
    no_duplicate_list: List[int] = []
    for i in input_list:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
    return no_duplicate_list

no_duplicates_loop = delete_duplicates_loop(rnd_list)
print(no_duplicates_loop)
