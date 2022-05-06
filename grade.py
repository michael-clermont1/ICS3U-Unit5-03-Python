#!/usr/bin/env python3

# Created by: Michael Clermont
# Created on: May 2022
# This program uses user defined functions


def grade_percentage(grade):
    # calculate percentage

    if grade == "R":
        percentage = 30
    elif grade == "1-":
        percentage = 51
    elif grade == "1":
        percentage = 55
    elif grade == "1+":
        percentage = 58
    elif grade == "2-":
        percentage = 61
    elif grade == "2":
        percentage = 65
    elif grade == "2+":
        percentage = 68
    elif grade == "3-":
        percentage = 71
    elif grade == "3":
        percentage = 75
    elif grade == "3+":
        percentage = 78
    elif grade == "4-":
        percentage = 83
    elif grade == "4":
        percentage = 91
    elif grade == "4+":
        percentage = 97
    else:
        percentage = "-1"

    return percentage


def main():
    # this function gets the grade percentage

    # input
    grade_level = input("Enter the level you want converted to a percentage: ")
    print("")

    # call functions
    calculated_percentage = grade_percentage(grade_level)

    print(
        "Level {0} has a middle percentage of {1}.".format(
            grade_level, calculated_percentage
        )
    )
    print("\nDone.")


if __name__ == "__main__":
    main()
