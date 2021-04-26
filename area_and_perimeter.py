#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 26 April 2021
# This program calculates the area and perimeter of a circle

import math


def main():
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    print("")
    print("Area is: {} mm²" .format(length * width))
    print("")
    print("Perimeter is: {} mm" .format(2 * (length + width)))
    print("")
    print("Done")


if __name__ == "__main__":
    main()
