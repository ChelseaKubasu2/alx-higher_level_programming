#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers
    Args:
        my_list: list
        x: integer rep. number of elements to print
    Return: actual number of elements printed
    """
    i = 0
    count = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            pass
        else:
            count += 1
        finally:
            i += 1

    print()
    return count
