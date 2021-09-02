'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# First Approach
#   Attempt to find the multiples between every combination from 1-20 then check those multiples to see if they have a remainder for any
    # number up to 20. If there is no remainder then it is a canadite and can be added to a list to check for the minimum at the end.

# for i in range(1, 21):
#     for j in range(1, 21):
#         check_number = i * j
#         print(i, "x", j, "=", i*j)

# The above does not work

# What abour brute force...

# init_i_val has to be even and non-zero
# check_to is the 10 or 20 number
def smallestPureDivisionNum(init_i_val, check_to):
    canidate = True
    while True: # This will keep going checking each next number until the feature is found
        canidate = True
        i = 1
        while canidate and (i < check_to + 1): # This will check numbers [1, check_to] while init_i_value is still a canadate
            if init_i_val % i != 0:
                canidate = False    # Exiting the loop and trying the next number

            i = i + 1

        if canidate: # If canadate is still true then we have found our number
            return init_i_val

        init_i_val = init_i_val + 2 # Try the next even number

print(smallestPureDivisionNum(360360, 20))

'''
Congratulations, the answer you gave to problem 5 is correct.

The public tables currently show that this problem has been solved by 493226 members.
8/19/2021
'''
