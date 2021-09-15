# CSE107 - Lab 4

This lab builds on the idea of manipulating lists and nested lists.

## Purpose

### navigate2.py

This program takes in multiple commands from the user and then translates 
those commands into movement via the Turtle library.

### statistics107.py

This program finds values such as sum, ever other element, odd elements, 
etc. in a given list and tests these functions.

### nested.py

This program finds attributes like select column, all have vlues, etc. in
a given list and tests these functions.

## Conclusion

* In this lab I practiced writing functions that iterate and manipulate 
  lists to return the requested characteristics of the lists passed to them.
  I got to practice how lists are structured and function.
* Pair programming aided in giving me an outside look at my code
  and allowed me to ask questions and give help to my partner when
  it was needed.
* I did not work with my buddy on the lab.
* I had a small problem with [nested.py](#nestedpy) where the function is 
  expecting an array with lists nested inside of each element, but one test
  case did not have any nested lists so it broke my program when it tried to
  get an element from a type 'int'. I couln't find a solution to this problem
  without using a try/except block.
* I think I could improve [nested.py](#nestedpy) to handle that last tricky 
  test case without the use of a try/except block.