def works_on_list(list1: list, list2: list) -> list:
    set_of_merged_lists = set([*list1, *list2])
    return [x**3 for x in set_of_merged_lists]
