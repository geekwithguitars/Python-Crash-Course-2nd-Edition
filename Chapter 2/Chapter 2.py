# 2-1
message = "Section 2.1"
print(message)

# 2-2
next_message = "Section 2.2"
print(next_message)
next_message = "Section 2.2!"
print(next_message)

# The title method of a string object converts each word to title case
name = "ada lovelace"
print(name.title())
print("test string".title())

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

