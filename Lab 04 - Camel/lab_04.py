import random


def main():

    print("""\n \tSoon you will have a final exam, 
    you need to study in order to
    escape from the bad grades, 
    do whatever you consider necessary to learn everything.
    \n To win you need to study at least 24 hours.
    """)

    study_time = 0
    nap_time = 0
    facebook_time = 0
    lose_game = False
    bad_grades_hours = 20
    boreness_level = 0
    fortnite_time = 0

    while not lose_game:

        sleep_random = random.randrange(1, 5)
        long_random_number = random.randrange(1, 5)
        study_short_random = random.random() * 2
        short_random_number = random.randrange(1, 4)
        extralarge_random_number = random.randrange(3, 8)

        print("A. Take a nap." +
              "\nB. Study for a long time. " +
              "\nC. Study for a short time. " +
              "\nD. Go to facebook." +
              "\nE. General Status." +
              "\nF. Play Fortnite." +
              "\nQ. Quit. \n")
        user_letter_choice = input("Your choice? \n")

        if user_letter_choice.lower() == "a":
            nap_time += sleep_random
            boreness_level -= 3
            bad_grades_hours -= sleep_random
            print("\nYou slept " + str(sleep_random) + " hour(s). \n")
            if nap_time >= 17:
                print("You slept too much.")
            elif nap_time > 11:
                print("If you sleep too much, bad grades will get you. \n")

        elif user_letter_choice.lower() == "b":
            study_time += long_random_number
            boreness_level += 4
            bad_grades_hours += long_random_number
            print("\nYou studied for " + str(long_random_number) + " hours \n")

        elif user_letter_choice.lower() == "c":
            study_time += study_short_random
            boreness_level += 2
            bad_grades_hours += study_short_random
            print("\nYou studied for " + str(study_short_random) + " hours. \n")

        elif user_letter_choice.lower() == "d":
            facebook_time += short_random_number
            boreness_level -= 1
            bad_grades_hours -= short_random_number
            print("\nYou were in Facebook for " + str(short_random_number) + " hours \n")
            if facebook_time >= 10:
                print("Too much Facebook.")
            elif facebook_time > 6:
                print("Being too much time in Facebook could make you lose.")

        elif user_letter_choice.lower() == "e":
            print("\nYou total nap time is: " + str(nap_time) + " hours.")
            print("You had studied for " + str(study_time) + " hours.")
            print("You have been in Facebook for " + str(facebook_time) + " hours")
            print("Bad grades are " + str(bad_grades_hours) + " hours away from you.")
            print("You had played Fortnite for " + str(fortnite_time) + " hours. \n")

        elif user_letter_choice.lower() == "f":
            print("\nAre you sure you want to play? This could be dangerous.")
            fortnite_choice = input("Y. Yes \nN. No \n")
            if fortnite_choice.lower() == "y":
                print("\nX. Xbox \nP. PLay Station \n")
                xbox_playstation = input("Choice: ")
                if xbox_playstation.lower() == "x":
                    print("\nNice. You won the match. \n")
                elif xbox_playstation.lower() == "p":
                    print("\nOh man! You lost the Fortnite match. \n")
                else:
                    print("\nI do not know that console. \n")

                fortnite_time += extralarge_random_number
                boreness_level -= 4
                bad_grades_hours -= extralarge_random_number
                print("You were playing fortnite for " + str(extralarge_random_number) + " hours. \n")
            elif fortnite_choice.lower() == "n":
                print("You are such a good student! \n")
            else:
                print("Not a valid answer. \n")

        elif user_letter_choice.lower() == "q":
            lose_game = True

        else:
            print("\nNot a valid answer. \n")

        if user_letter_choice.lower() != "e":
            if study_time >= 24:
                print("\nCongratulations, you successfully studied for " + str(study_time) + " hours, you won!")
                print("You got the best grades ever.")
                break

            if bad_grades_hours <= 0 or boreness_level < -10 or boreness_level > 10 or nap_time > 17 or facebook_time > 10:
                print("\nOh no, bad grades got you.")
                lose_game = True
                print("You lost.")

            elif boreness_level >= 7:
                nap_time += sleep_random
                bad_grades_hours -= 14
                boreness_level -= 3
                print("You will take a mandatory nap for " + str(sleep_random) + " hours because you are bored.")
                print("You should try doing something else before studying. \n")

            elif boreness_level >= 5 and boreness_level < 7:
                print("""You need to do something else than studying, you are bored and bad grades will get you faster. 
                      tip: if you study many times in a row, you will be forced to take a nap. \n""")

            elif boreness_level < -1:
                print("You should study.\n")


main()
