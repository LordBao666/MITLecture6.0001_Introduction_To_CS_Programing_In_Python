"""
@Author  : Lord_Bao
@Date    : 2021/3/3

"""

"""
Finger exercise: Write a program that asks the user to input 10 integers, and then
prints the largest odd number that was entered. If no odd number was entered, it
should print a message to that effect.
"""

print("input 10 integers\n")

largest_odd = -1
count = 0
confirm_the_current_largest_odd_yet = False
while count < 10:
    num = int(input("input  integer " + str((count + 1)) + " :"))
    if num % 2 != 0:
        if not confirm_the_current_largest_odd_yet:
            largest_odd = num
            confirm_the_current_largest_odd_yet = True
        else:
            if largest_odd < num:
                largest_odd = num

    count += 1

if not confirm_the_current_largest_odd_yet:
    print("\nno odd integer")
else:
    print("\nthe largest odd integer is " + str(largest_odd))
