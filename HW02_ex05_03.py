#!/usr/bin/env python
# HW02_ex05_03

# Fermat's Last Theorem says that there are no positive integers a, b, and c 
# such that 
#        a^n + b^n = c^n 
# for any values of n greater than 2.

# (1) Write a function named check_fermat that takes four parameters-a, b, c and 
# n-and that checks to see if Fermat's theorem holds. If n is greater than 2 
# and it turns out to be true that
#        a^n + b^n = c^n 
# the program should print, "Holy smokes, Fermat was wrong!"" 
# Otherwise the program should print, "No, that doesn't work."

# (2) Write a function named check_fermat_ints that prompts the user to input 
# values for a, b, c and n, converts them to integers, and uses check_fermat
# to check whether they violate Fermat's theorem.

################################################################################
# Write your functions below:
# Body

##############
### Part 1 ###
##############

def check_fermat(a,b,c,n):
	if n > 2:
		if (a**n + b**n == c**n):
			print ("Holy smokes, Fetmat was wrong!")
		else:
			print ("No, that doesn't work.")
	else:
		print "n is less than 2. Please try again." 


check_fermat(1, 2, 3, 4)


##############
### Part 2 ###
##############

def check_fermat_ints():
	prompt = "Please enter a number:"
	a = raw_input(prompt)
	b = raw_input(prompt)
	c = raw_input(prompt)
	n = raw_input(prompt)
	a = int(a)
	b = int(b)
	c = int(c)
	n = int(n)
	check_fermat(a, b, c, n)


check_fermat_ints() # discovered cannot ask for prompts in Sublime

# Write your functions above:
################################################################################
def main():
    """Call your function within this function.
    When complete have one function call in this function:
    check_fermat_ints(1,2,3,4)
    and two functions defined in the body:
    check_fermat_ints()
    check_fermat()
    """
    print("Hello World!")

##    check_fermat_ints(1, 2, 3, 4) ## Unsure about this instruction,
# as it seeks user input as a function.

check_fermat(1, 2, 3, 4)
check_fermat_ints()



if __name__ == "__main__":
    main()