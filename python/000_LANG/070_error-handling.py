try: # code-block that might crash
  print(10 / 0) # throws ZeroDivisionError
  print("never printed")
except: # catch all errors
  pass # do nothing, necessary because keywords like except, try, for, if, while, ... expect intended block
finally: # optional, block below always executed, regardless of fail or success, even if return statement in try or except block or if nested try-blocks
  print("always printed")

def exception_demo(n):
  try:
    print(10 / n)
    assert 10 == n # assert throws error if statement not True, useful for debugging
  except ZeroDivisionError:
    print("0 is not allowed!")
  except TypeError: # store error in variable
    print("only numeric parameters!")
  except Exception as e: # store exception in variables
    print("exception thrown of type {}".format(type(e)))
exception_demo(0)
exception_demo("test")
exception_demo(2)
exception_demo(10)

def throw_exception():
  raise ValueError("title", "body") # throw exception
  raise OSError()

try:
  throw_exception()
except (ValueError, OSError):
  print("multiple exception types catch")

throw_exception() # uncaught exception will stop the execution

print("never printed")