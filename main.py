# main.py
# goal: program a summation calculator
# secondary goal: program summation rules
# I think I need to program a simple additive program first?

# variable seeds
N = 5;
j = 1;
funct_x = "x";
funct_ele = [];
summ = 0.0;
summ_iter_var = 0;

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
