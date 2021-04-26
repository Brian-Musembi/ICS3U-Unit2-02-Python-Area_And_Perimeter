#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 26 April 2021
# This program calculates the area and perimeter of a circle

import math


def main():
    radius_of_circle = int(input("Enter the radius of the circle: "))
    print("Its area is: {}" .format(math.pi * radius_of_circle ** 2))
    print("")
    print("Its perimeter is: {}" .format(2 * (math.pi * radius_of_circle)))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
