"""
A program that takes movement commands and reflects those commands in Turtle

file: navigate2.py

author: Donovan Griego

Date: 9-15-2021

assignment: Lab 4
"""
import turtle


def main():
    # grabs commands until "stop" is read
    queue = ["start"]
    while queue[len(queue) - 1] != "stop":
        cmd = input("Please enter a direction: ")
        queue.append(cmd)
        if cmd == "right" or cmd == "left":
            queue.append(float(input("How many degrees? ")))
    window = turtle.Screen()
    t1 = turtle.Turtle()
    i = 0
    print("Running...")
    # goes through queue and runs the stored commands until "stop" is read
    while i < len(queue):
        if queue[i] == "start":
            t1.pendown()
            i += 1
        elif queue[i] == "forward":
            t1.forward(50)
            i += 1
        elif queue[i] == "right":
            t1.right(float(queue[i + 1]))
            i += 2
        elif queue[i] == "left":
            t1.left(float(queue[i + 1]))
            i += 2
        elif queue[i] == "stop":
            print("Done.")
            window.mainloop()
            exit(0)
        else:
            print("Invalid commad '{}'; ignoring".format(queue[i]))
            i += 1


if __name__ == "__main__":
    main()
