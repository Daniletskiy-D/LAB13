#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def garmonic_mean(*args):
    if args:
        values = [float(arg) for arg in args]

        reciprocal_sum = sum(1 / arg for arg in values)
        return len(args) / reciprocal_sum
    
    else: 
        return None


def main():
    user_values = [float(value) for value in input("Числа: ").split()]
    print(garmonic_mean(*user_values))


if __name__ == "__main__":
    main()