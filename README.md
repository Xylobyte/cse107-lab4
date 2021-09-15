# CSE107 - Lab 3

This lab builds on the idea of making functions and modules that
can be referenced in other files

## Purpose

### fizzbuzz.py

This program prints out "Fizz" for multiples of 3, "Buzz" for
multiples of 5, and "FizzBuzz" for both.

### collatz.py

This program finds the collatz segence length given a starting number.

### longgest_collatz.py

This program uses collatz.py to find the longest chain with a start under 1000000.

### navigate.py

This program takes in multiple commands from the user and then translates 
those commands into movement via the Turtle library.

## Conclusion

* In this lab I practiced referencing other modules and fnctions that
  I made in order to provide more funcitonailty to my programs while 
  also making them cleaner and more efficient.
* Pair programming aided in giving me an outside look at my code
and allowed me to ask questions and give help to my partner when
it was needed.
* I did not work with my buddy on the lab.
* I had a problem in [navigate.py](#navigatepy) getting the initial way
  I wanted to go from written string commands to actual turtle commands.
  I was originally going to map those values to the turtle commands directly 
  via a dictionary with the strings as keys but when running the commands it
  wasn't running correctly. After messing with the implementation for about
  an hour I scrapped it and settled on a chain of if/else statements.
* I think I could improve [navigate.py](#navigatepy) by getting my first 
  idea to work. It would save a lot more space and work more efficiently.