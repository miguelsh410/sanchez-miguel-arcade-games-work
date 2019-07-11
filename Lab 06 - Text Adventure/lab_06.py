def main():
    room_list = []
    room = ["You are in the living room. To the the north\nthe dinning room and to the east the south hall.\n", 3, None,
            1, None]
    room_list.append(room)

    room = ["You are in the south hall. To the north\nthe north hall, to the east the restroom, \nand to the west "
            "the living room.\n", 4, None, 2, 0]
    room_list.append(room)

    room = ["You are in the restroom. To the north\nthe bedroom, and to the west the south hall.\n", 5, None, None, 1]
    room_list.append(room)

    room = ["You are in the dinning room. To the north\nthe kitchen, to the south the living room, \nand to the east "
            "the North Hall.\n", 6, 0, 4, None]
    room_list.append(room)

    room = ["You are in the north hall. To the south\nthe south hall, to the east the bedroom, and \nto the west the "
            "dinning room.\n",None, 1, 5, 3]
    room_list.append(room)

    room = ["You are in the bedroom. To the south\nthe restroom, and to the west the north hall.\n", None, 2, None, 4]
    room_list.append(room)

    room = ["You are in the Kitchen. To the south\nthe Dinning Room.\n", None, 3, None, None]
    room_list.append(room)

    # Start in the living room.
    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room][0])
        user_input = input("Where do you want to go? ")

        # 1 is north.
        if user_input.lower() == "n" or user_input.lower() == "north":
            next_room = room_list[current_room][1]
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # 2 is south.
        elif user_input.lower() == "s" or user_input.lower() == "south":
            next_room = room_list[current_room][2]
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # 3 is east.
        elif user_input.lower() == "e" or user_input.lower() == "east":
            next_room = room_list[current_room][3]
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # 4 is west.
        elif user_input.lower() == "w" or user_input.lower() == "west":
            next_room = room_list[current_room][4]
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "q" or user_input.lower() == "quit":
            done = True
            print("You quit the game.")

        else:
            print("I don't understand!")


main()

