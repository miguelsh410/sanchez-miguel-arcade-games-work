from random import randint as rdm


def selection_sort(a_list):
    """Function that sorts a list using selection sort algorithm."""
    for cur_pos in range(len(a_list)):
        min_pos = cur_pos

        # Find smallest value.
        for scan_pos in range(cur_pos + 1, len(a_list)):
            if a_list[scan_pos] < a_list[min_pos]:
                min_pos = scan_pos

        # Swap minimum value into position.
        temp = a_list[min_pos]
        a_list[min_pos] = a_list[cur_pos]
        a_list[cur_pos] = temp


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

print(my_list)
selection_sort(my_list)
print(my_list)

print("""--- Multiple random lists ---""")


def random_list():
    """Function that returns a 15 item list with random numbers."""
    list_of_numbers = []
    for i in range(16):
        random_number = rdm(0, 151)
        list_of_numbers.append(random_number)
    return list_of_numbers


list_1 = random_list()
list_2 = random_list()
list_3 = random_list()

print("\nGiven list:", list_1)
selection_sort(list_1)
print("Sorted list:", list_1)
print("\nGiven list:", list_2)
selection_sort(list_2)
print("Sorted list:", list_2)
print("\nGiven list:", list_3)
selection_sort(list_3)
print("Sorted list:", list_3)
