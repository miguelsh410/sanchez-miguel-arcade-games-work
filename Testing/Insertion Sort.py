from random import randint as rdm


def insertion_sort(my_list):
    """Function that sorts a list using insertion sort algorithm."""
    for key_pos in range(1, len(my_list)):

        key_value = my_list[key_pos]
        scan_pos = key_pos - 1

        while scan_pos >= 0 and my_list[scan_pos] > key_value:
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos -= 1

        my_list[scan_pos + 1] = key_value


x = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

print(x)
insertion_sort(x)
print(x)

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
insertion_sort(list_1)
print("Sorted list:", list_1)
print("\nGiven list:", list_2)
insertion_sort(list_2)
print("Sorted list:", list_2)
print("\nGiven list:", list_3)
insertion_sort(list_3)
print("Sorted list:", list_3)
