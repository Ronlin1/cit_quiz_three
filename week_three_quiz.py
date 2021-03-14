"""
WEEK THREE QUIZ AS AT 13 MARCH 2020 ___PYTHON-BLOCKCHAIN-AWS-CIT-CLASS 2021___
"""
# WELCOME SCREEN
print('------------------------- WEEK THREE QUIZ --------------------------')

# TODO: QUIZ ANSWERS
# Global variable --->End of question separator in the ---- terminal ----
end_of_answer = '------------------------------------------------------------------'

# 1 --> print out the word (num) amount of times

# Using a for loop
num_1 = int(input("Enter a Number : "))
for _ in range(num_1):
    print(f'Here is your number \'{num_1}\' being printed --{num_1}-- times!')
print(end_of_answer)

# Using a while loop
num_2 = int(input("Enter a Number : "))
counter = 1
while counter <= num_2:
    print(f'And here is your number \'{num_2}\' again being printed --{num_2}-- times!')
    counter += 1
print(end_of_answer)

# 2 --> (Friday Main Challenge): print stars hills and diamonds

# BASIC CHALLENGE
# Using a for loop
num_3 = int(input("Enter a Number : "))

for idx_1 in range(num_3):
    for idx_2 in range(idx_1):
        # The end helps us to print on one line
        print("*", end="")
    # This print keeps us in a loop to achieve this
    print()

for idx_1 in range(num_3, 0, -1):
    for idx_2 in range(idx_1):
        print("*", end="")
    print()

print(end_of_answer)

# Using a while loop -- BASIC
num_3 = int(input("Enter a Number : "))
counter = 0

# The upper part
while counter < num_3:
    print(counter * "*")
    counter += 1

# The Down part
counter_ = num_3 - 2
while counter_ > 0:
    print(counter_ * "*")
    counter_ = counter_ - 1

print(end_of_answer)

#ADVANCED CHALLENGE --> Printing a diamond from stars
num_ = int(input("Enter a Number : "))

# if input --> 5 consider the shape below
"""
     *
   * * *
 * * * * *
   * * *
     *

     For input greater than 5> , just tweaking the range (start, stop , step) gives the perfect diamond

"""

# Implementation
for i in range(1, num_, 2):
    print((num_ - i) * " " + (i * " *"))

# Reverse printing the other half
for i in range(num_, 0, -2):
    print((num_ - i) * " " + (i * " *"))

print(end_of_answer)

# Using a while loop for the ADVANCED CHALLENGE
number = int(input("Kindly Enter any number: "))

# Variables for first while loop
spaces = int((number - 1) / 2)
stars = 1

# Variables for second while loop
spaces_ = 1
stars_ = number - 3

# Implementation
while stars <= number:
    # Since spaces decrease, as stars increase
    print(' ' * spaces + '*' * stars + ' ' * spaces)
    spaces = spaces - 1
    stars = stars + 2

while stars_ >= 0:
    # Since spaces increase as stars decrease to simulate a diamond
    print(' ' * spaces_ + '*' * stars_ + ' ' * spaces_)
    spaces_ = spaces_ + 1
    stars_ = stars_ - 2

print(end_of_answer)