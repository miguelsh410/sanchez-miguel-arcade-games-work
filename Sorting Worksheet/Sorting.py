import random
# 1. Write code to swap the values 25 and 40.
my_list_1 = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]
temp_1 = my_list_1[6]
my_list_1[6] = my_list_1[7]
my_list_1[7] = temp_1
print(my_list_1)

# 2. Write code to swap the values 2 and 27.
my_list_1 = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]
temp_1 = my_list_1[0]
my_list_1[0] = my_list_1[3]
my_list_1[3] = temp_1
print(my_list_1)

# 3. Why does the following code not work? Explain it, don't just list working code.
my_list_1 = [70, 32, 98, 88, 92, 36, 81, 83, 87, 66]
temp_1 = my_list_1[0]
my_list_1[1] = my_list_1[0]
my_list_1[0] = temp_1
"""The code doesn't work as expected because after creating the temp variable we need to change the value 
of the position that we put in the temp, otherwise, both positions will have the same value 
instead of swapping them """

# 4. Show how the following numbers can be sorted using the selection sort.
# Show the numbers after each iteration of the outer loop, similar to what is shown in the book.
# I am NOT looking for a copy of the code to do the sort.
# If you include any code for problems 4-7 you are doing it wrong.
"""97, 74, 8, 98, 47, 62, 12, 11, 0, 60"""
"""0, 74, 8, 98, 47, 62, 12, 11, 97, 60"""
"""0, 8, 74, 98, 47, 62, 12, 11, 97, 60"""
"""0, 8, 11, 98, 47, 62, 12, 74, 97, 60"""
"""0, 8, 11, 12, 47, 62, 98, 74, 97, 60"""
"""0, 8, 11, 12, 47, 62, 98, 74, 97, 60"""
"""0, 8, 11, 12, 47, 60, 98, 74, 97, 62"""
"""0, 8, 11, 12, 47, 60, 62, 74, 97, 98"""
"""0, 8, 11, 12, 47, 60, 62, 74, 97, 98"""
"""0, 8, 11, 12, 47, 60, 62, 74, 97, 98"""
"""0, 8, 11, 12, 47, 60, 62, 74, 97, 98"""

# 5. Show how the following numbers can be sorted using the selection sort:
"""74, 92, 18, 47, 40, 58, 0, 36, 29, 25"""
"""0, 92, 18, 47, 40, 58, 74, 36, 29, 25"""
"""0, 18, 92, 47, 40, 58, 74, 36, 29, 25"""
"""0, 18, 25, 47, 40, 58, 74, 36, 29, 92"""
"""0, 18, 25, 29, 40, 58, 74, 36, 47, 92"""
"""0, 18, 25, 29, 36, 58, 74, 40, 47, 92"""
"""0, 18, 25, 29, 36, 40, 74, 58, 47, 92"""
"""0, 18, 25, 29, 36, 40, 47, 58, 74, 92"""
"""0, 18, 25, 29, 36, 40, 47, 58, 74, 92"""
"""0, 18, 25, 29, 36, 40, 47, 58, 74, 92"""
"""0, 18, 25, 29, 36, 40, 47, 58, 74, 92"""

# 6. Show how the following numbers can be sorted using the INSERTION sort.
# (Note: If you think the 0 gets immediately sorted into position, you are doing it wrong.
# Go back and re-read how this sort works.)
"""74, 92, 18, 47, 40, 58, 0, 36, 29, 25"""
"""74, 92, 18, 47, 40, 58, 0, 36, 29, 25"""
"""18, 74, 92, 47, 40, 58, 0, 36, 29, 25"""
"""18, 47, 74, 92, 40, 58, 0, 36, 29, 25"""
"""18, 40, 47, 74, 92, 58, 0, 36, 29, 25"""
"""18, 40, 47, 58, 74, 92, 0, 36, 29, 25"""
"""0, 18, 40, 47, 58, 74, 92, 36, 29, 25"""
"""0, 18, 36, 40, 47, 58, 74, 92, 29, 25"""
"""0, 18, 29, 36, 40, 47, 58, 74, 92, 25"""
"""0, 18, 25, 29, 36, 40, 47, 58, 74, 92"""

# 7. Show how the following numbers can be sorted using the insertion sort:
"""37, 11, 14, 50, 24, 7, 17, 88, 99, 9"""
"""11, 37, 14, 50, 24, 7, 17, 88, 99, 9"""
"""11, 14, 37, 50, 24, 7, 17, 88, 99, 9"""
"""11, 14, 37, 50, 24, 7, 17, 88, 99, 9"""
"""11, 14, 24, 37, 50, 7, 17, 88, 99, 9"""
"""7, 11, 14, 24, 37, 50, 17, 88, 99, 9"""
"""7, 11, 14, 17, 24, 37, 50, 88, 99, 9"""
"""7, 11, 14, 17, 24, 37, 50, 88, 99, 9"""
"""7, 9, 11, 14, 17, 24, 37, 50, 88, 99"""

# 8. Explain what min_pos does in the selection sort.
"""min_pos is used to stay in a position and compare each number after that position in the list to see
which number is smaller. If the number compared to min_pos is lower than min_pos, min_pos will take the value
of the lowest number."""

# 9. Explain what cur_pos does in the selection sort.
"""cur_pos is a variable that changes every time the outer loop runs. It is used to set a position in a list
and later it will store the next lowest value."""

# 10. Explain what scan_pos does in the selection sort.
"""scan_pos is a variable that changes every time the inner loop runs. It is used to iterate through each
position in a list and compare it to the min_pos. If scan_pos is lower than min_pos, min_pos will
take the value of scan_pos"""

# 11. Explain what key_pos and key_value are in the insertion sort.
"""key_pos is a variable that changes by 1 every time the outer loop runs. It is used to point a position 
inside a list. key_value is a variable that stores the number in the position pointed by key_pos."""

# 12. Explain scan_pos in the insertion sort.
"""scan_pos is variable that is equal to one or more numbers before key_value, it is compared to key_value 
and if it happens to be greater than it, they swap positions."""

# 13. Look at the example sort program. Modify the sorts to print the number of times the inside loop is run,
# and the number of times the outside loop is run. Modify the program to work with a list of 100.
# Paste the code you used here. Run the program and list the numbers you got here.
# (DON'T FORGET TO INCLUDE THE RESULTS!) Inside loop for selection sort should be about 5,000, and insertion sort 2,500.
# Double-check if you don't get numbers close to these. ﻿


def selection_sort(my_list):
    """ Sort a list using the selection sort """
    inside_loop = 0
    outside_loop = 0
    # Loop through the entire array
    for cur_pos in range(len(my_list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos
        outside_loop += 1
        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(my_list)):
            inside_loop += 1
            # Is this position smallest?
            if my_list[scan_pos] < my_list[min_pos]:
                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp
    print("The outside loop ran", outside_loop, "times.")
    print("The inside loop ran", inside_loop, "times.")


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """
    inside_loop = 0
    outside_loop = 0
    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(my_list)):

        # Get the value of the element to insert
        key_value = my_list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1
        outside_loop += 1
        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
            inside_loop += 1
        # Everything's been moved out of the way, insert
        # the key into the correct location
        my_list[scan_pos + 1] = key_value
    print("The outside loop ran", outside_loop, "times.")
    print("The inside loop ran", inside_loop, "times.")


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)

    # Use the insertion sort and print the result
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()
