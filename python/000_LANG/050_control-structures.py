if True: # if expects boolean value 
  print("inside if-statement") # only executed if statement after "if" evaluates to True
  pass # pass does nothing, whole body must be intended by equal amount of tabs and spaces
else: # if-statement and its intended body must precede
  print("inside else-statement")

a = 8
if a == 10:
  print("equal")
elif a > 10: # else if, only attemtped if first if evaluates to False
  print("bigger")
else:
  print("smaller")

if (a > 0) and (a < 10): # use paranthesis to group conditions
  print("between 0 and 10")

iterList = [1, 2, "dog", "cat"]
for elem in iterList: # iterList is the name list to iterate over, elem is the name of element of the current iteration to be used in the function body
  print(elem)

for i in range(10): # range generates a list from 1 through 10-1
  print(i ** 2)

j = 0
while j < 10: # repeats body as long as statement is True
  print(j ** 2) # same result as previous block
  j += 1

k = -1
while True: # endless loop
  k += 1
  if k % 2 != 0: # check if k not divisble by 2, i.e. if it's odd
    continue # skip the rest of the body and start from top, can be used in for-loops as well
  print(k // 2)

  if k >= 10:
    break # breaks the loop and continues executing the statements after the loop, can also be used in for-loops

print("outside endless loop")