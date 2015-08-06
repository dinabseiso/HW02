#!/usr/bin/env python
# HW02_ex05_02

# Write a function called do_n that takes a function object and a number, n, as 
# arguments, and that calls the given function n times.

################################################################################
# Write your functions below:
# Body

#############
### Way 1 ###
#############


def do_n(f, n):
	x = 1
	while x <= n :
		f()
		x = x + 1


#############
### Way 2 ###
#############

def do_nother(f, n):
    if n <= 0:
        return
    f()
    do_nother(f, n-1)



# Write your functions above:
def print_hello():
    print("Hello World")
################################################################################
def main():
    """Call your function within this function.
    When complete have one function call in this function:
    do_n(print_hello, 10)
    """
    do_n(print_hello, 10) # replace this with do_n(print_hello, 10)
    do_nother(print_hello, 10) # replace this with do_n(print_hello, 10)



if __name__ == "__main__":
    main()