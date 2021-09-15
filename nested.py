"""
A program that takes movement commands and reflects those commands in Turtle

file: navigate2.py

author: Donovan Griego

Date: 9-15-2021

assignment: Lab 4
"""

# Fill in a correct implementation for each function.
# Define other functions if you think they make the
# assigned function easier to write or easier to read.


def all_have_value(lst):
    """
    This function returns True if all list elements have a value other
    than '-', False otherwise.

    lst: list to process.
    """
    all_values = True
    for e in lst:
        if e == "-":
            all_values = False
    return all_values


def all_equal(lst):
    """
    This function returns True if all list elements have the same value 
    that is not '-', false otherwise.

    lst: list to process.
    """
    value = lst[0]
    for e in lst:
        if e != value or e == "-":
            return False
    return True


def select_row(array, index):
    """
    This function returns the elements in a given row.

    array: list of lists (sometimes).
    index: row to return.
    """
    return array[index]


def select_col(array, index):
    """
    This function returns the elements in a given column.

    array: list of lists (sometimes).
    index: column to return.
    """
    lst = []
    try:
        for e in array:
            lst.append(e[index])
    except TypeError:
        lst.append(array[index])
    return lst


def run_tests():
    """This function tests each function defined in this module."""

    # A single test is a tuple containing the function
    # which is being tested, a sample input, and the correct output.
    # Tests should be written using the unittest or pytest modules,
    # but, hopefully, this code is easier to understand.
    tests = [
        # This test will be used to check if `sum([1, 2, 3])` is `6`.
        (all_have_value, [1, 2, 3, 4, 5], True),
        (all_have_value, ['c', 'a', 't'], True),
        (all_have_value, ['-', '-'], False),
        (all_equal, [1, 1, 1, 1, 1], True),
        (all_equal, ['-', '-'], False),
        (all_equal, ['python', 'python'], True),
        (select_row, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [4, 5, 6]),
        (select_row, [[1, 1, 3], [1, 1, 4]], 0, [1, 1, 3]),
        (select_row, [[1], [2], [3], [4]], 3, [4]),
        (select_col, [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, [1, 4, 7]),
        (select_col, [[1, 1, 3], [1, 1, 3]], 2, [3, 3]),
        (select_col, [5, 4, 3, 2, 1], 3, [2])

    ]

    passed = 0
    failed = 0

    # Test each function.
    # Print a detailed error message whenever a function fails a test.
    for test in tests:
        if len(test) == 4:
            f = (test[0])
            result = f(test[1], test[2])
            expected = test[3]
            if result == expected:
                passed += 1
            else:
                failed += 1

                # f.__name__ is the function's name
                # for example, select_row.__name__ is the string "select_row"
                print("Function '{}' given arguments {}, {}".format(
                    f.__name__, test[1], test[2]))
                print("Expected {}, but returned {}".format(expected, result))
        else:
            f = (test[0])
            result = f(test[1])
            expected = test[2]
            if result == expected:
                passed += 1
            else:
                failed += 1

                # f.__name__ is the function's name
                # for example, select_row.__name__ is the string "select_row"
                print("Function '{}' given argument {}".format(
                    f.__name__, test[1]))
                print("Expected {}, but returned {}".format(expected, result))
    print("\nPassed {} out of {} tests.".format(passed, passed + failed))


if __name__ == "__main__":
    run_tests()
