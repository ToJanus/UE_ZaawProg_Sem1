def multiply_by_two(numbers):
    return [n * 2 for n in numbers]

def multiply_by_two_in_for(numbers):
    list_to_return = []
    for n in numbers:
        list_to_return.append(n * 2)
    return list_to_return


list_of_numbers = [4, 12, 1, 6, 22]
print(f"Przed: {list_of_numbers}")
print(f"Po (lista składana): {multiply_by_two(list_of_numbers)}")
print(f"Po (pętla for): {multiply_by_two_in_for(list_of_numbers)}")
