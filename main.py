# main.py
# goal: program a summation calculator
# secondary goal: program summation rules
# I think I need to program a simple additive program first?

# v 1.1 code below

# variable seeds
N = 5;
j = 1;
funct_x = "x";
summ = 0.0;
summ_iter_var = 0;

# function defs

def summ_calc():
"""Program adds N-j quantities of f(x) together, incrementing f(x) by 1 each loop"""
	if N >= j and N > 0:
		summ_iter_var = N - j
		while summ_iter_var > 0:
			

def summ_x_to_first():
"""Program optimization which uses (N(N+1))/2 rule only when f(x)= Kx + C"""
	print("summ_x_to_first test")

def summ_x_to_second():
"""Program optimization which uses (N(N+1)(2N+1))/6 rule only when f(x) = Kx^{2} + C"""
	print("summ_x_to_second test")

def summ_x_to_third():
"""Program optimization which uses [forgot this rule lol] only when f(x) = Kx^{3} + C"""
	print("summ_x_to_third test")

def funct_in_con():
"""Function translates user inputs into arithmatic meaning"""
	
	# print("funct_in_con() test")

# user instructions
"""Hello, welcome to the Summation Calculator v. 1.1
______ N= 5 (default)
\     \
 \      f(x) = x (default)
 /
/_____/
      j= 1 (default)
With this program, you can overwrite values in the summation.
"""
)

# summation variable inputs
N = int(input("N = __"))
j = int(input("j = __"))
funct_x = input("f(x) = ______")

# v 1 code below
print(
"""Hello, welcome to the Summation Calculator v. 1
Please enter the lower number you want to add:

"""
)

a = float(input())
print(
"""Please enter the higher number you want to add:

"""
)

b = float(input())

def add_toget(a, b):
	return a + b

print(a, "plus", b, "equals", add_together(a, b))
# Should be enough to add a and b- untested tho
