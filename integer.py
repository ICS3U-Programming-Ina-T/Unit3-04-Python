#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Dec. 10, 2021
# This program determines the type of
# number a user has entered.

# accepts input from user
user_number = float(input("Enter a number: "))
print("")


# this function checks if the user has
# entered the correct number
def main():

    # process & output
    if user_number > 0:
        print("{} is a positive number.". format(user_number))
    elif user_number < 0:
        print("{} is a negative number.". format(user_number))
    else:
        print("{} is just zero.". format(user_number))


if __name__ == "__main__":
    main()
