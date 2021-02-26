def say_hello(): # define function without parameters
  print("hello")
  # no return value
say_hello() # call function
say_hello() # can be reused

def double_num(n): # function with 1 parameter
  return n * 2 # return value
print(double_num(10)) # print return value

def fibonacci(n): # recursive function
  if n == 0: # stop condition
    return 1
  elif n == 1: # stop condition
    return 0 
  return fibonacci(n - 1) + fibonacci(n - 2) # recursive function call, memory expensive
print(fibonacci(20))
print(fibonacci(25))

def concat_str(*strings): # variable amount of parameters denoted with *, all parameters in list
  return_str = ""
  for string in strings:
    return_str += string
  return return_str
print(concat_str("Hel", "lo", "!"))