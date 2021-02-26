n = -10 # variable assignment
print(n) # using variable, print function can take other types
print("{} is of type {}".format(n, type(n))) # format string with variables or values, get type function

f = 5.3 # floating point number
print("{1} is of type {0}".format(type(f), f)) # formatting based on parameter index

b = True # boolean value, either True or False
print("{value} is of type {type}".format(value = b, type = type(b))) # formatting based on keyword

txt = "\"hi!\"" # string, text enclosed by single or double quotes, use \ to escape quotes and use them in a string
txtFormat = "{} is of type {}"
print(txtFormat.format(txt, type(txt))) # text to format is now first put in variable