# Python uses type inferencing so that it is not necessary to specify the type of a variable when defining it

# 
# Strings
# 


# Example of how to use a string. This is referencing the variable name to the memory location where the string is located.
message = "Section 2.1"
print(message)

# Example of updating a string. This actually dereferences the variable and references the new memory location of the new value
next_message = "Section 2.2"
print(next_message)
next_message = "Section 2.2!"
print(next_message)

# The title method of a string object converts each word to title case
name = "ada lovelace"
print(name.title())
print("test string".title())

# A multi-line string can be created by using three ''' in a row
names = '''Name 1
Name 2
Name 3'''
print(names)

# Other useful methods of string objects are upper() and lower()
print("StRiNg".upper())
print("StRiNg".lower())

# To insert variable values in strings, use a 'format string'
# Format strings were introduced in Python 3.5. Previously the format() function was used
first_name = "bucket"
last_name = "head"
full_name = f"{first_name} {last_name}" # Create a format string by typing f before the quotes in a string, and surrounding each variable with curly braces
print(full_name)
greeting = f"Hey there, {full_name.title()}!"
print(greeting)

# Whitespace formatting in strings can be used via \n (new line) and \t (tab character)
display_message = "My favorite musicians are:\n\tBuckethead\n\tAngel Vivaldi\n\tLudovico Einaudi"
print(display_message)

# Removing whitespace from a string can be achieved using the strip, rstrip, and lstrip methods
right_whitespace = "extra space to the right!                        "
left_whitespace = "                    more space to the left!"
both_whitespace = "            this string is in the middle              "
print(right_whitespace.rstrip()) # rstrip removes whitespace from the right of the string
print(left_whitespace.lstrip()) # lstrip removes whitespace from the left of the string
print(both_whitespace.strip()) # strip removes whitepace from both sides of the string


# 
# Integers
# 

a = 2
b = 3

print("Integer examples:")
print(f"Addition example {a} + {b} = {a + b}")
print(f"Subtraction example {a} - {b} = {a - b}")
print(f"Multiplication example {a} * {b} = {a * b}")
print(f"Division example {a} / {b} = {a / b} <-- note that the result will be a floating point number")
print(f"Floor division example {a} // {b} = {a // b}")
print(f"Exponent example {a} ** {b} = {a ** b}")


# 
# Floats
# 

# Floating point numbers behave the way you expect
c = .1
d = .2

print("Float examples:")
print(f"Addition example {c} + {d} = {c + d}")
print(f"Subtraction example {c} - {d} = {c - d}")
print(f"Multiplication example {c} * {d} = {c * d}")
print(f"Division example {c} / {d} = {c / d}")
print(f"Floor division example {c} // {d} = {c // d}")
print(f"Exponent example {c} ** {d} = {c ** d}")

# Sometimes there may be unexpected values in the result due to the way the floating point numbers are stored in memory
print("Unexpected values when working with floating point numbers:")
print(f"Addition example {c} + {d} = {c + d} <-- the '0000000000000004' is not expected in this result")
print(f"Addition example 3 * {d} = {3 * d} <-- the '0000000000000001' is not expected in this result")

# If you mix an integer and a float in any operation the type of the result will be a float
int_float = a + c
print(f"The result of the equasion {a} + {c} = {int_float} and the type of the result is {type(int_float)}")

# You can make large numbers more readable by adding underscores to them
# The underscores will not be read by python, so 1000 is the same as 1_000
paycheck = 57_000_000_000
print(f"The value of paycheck is {paycheck}, notice that there are no underscores.")

# Comments in code (like the one you are reading now!) help other developers, as well as yourself, understand the code
# Comments are made by putting a hack mark (#) in the code followed by a space and any text. Any text that follows the hash and space
# will be ignored by python's interpreter. Comments can be placed at the beginning of a line or anywhere else, but anything that follows 
# the hash and space will be ignored.


# Here is some code that will initialize a list of strings and iterate over them to display some principals from Tim Peters' Zen of Python book
# The formatting of this code is tightly coupled with the core logic, but it is fine for a trivial example

maxims = ["Maxims from The Zen of Python, by Tim Peters", "Beutiful is better than ugly.", "Simple is better than complex.", "Complex is better than complicated.", "Readability counts.", "There should be one -- and preferably one -- obvious way to do it.", "Now is better than never."]

first_line = True 
for maxim in maxims :               # Loop over each string in the list of maxims
    if(first_line == True) :        # If we are at the first line we need to print a newline character and the first maxim
        print("")
        print(maxim)
        first_line = False          # Set our flag to know if we are at the first line or not
    elif(first_line == False) :     # If we are not at the first line we should print a tab and the maxim
        print(f"\t{maxim}")
first_line = True