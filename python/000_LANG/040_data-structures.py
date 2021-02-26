a = [5, 1.0, True, "hello", [1, 2, 3]] # list in python contains multiple values of any type, order doesn't change, mutable (changeable)
print(a)
b = a[1] # get 0-indexed item in list
print(b)
a[1] = 2 # assign 0-indexed item in list
a[1] *= 2
print(a[1])
print(a[4][1]) # nested list
print(len(a)) # get list length
a.append("bye") # add to end of list
print(a.index(5)) # get index of item
print(True in a) # check for item membership
a.pop() # remove last item
a.insert(3, "test") # insert value at given index
print(a)
a.clear()
print(a)

e = (34, True, "female") # tuple is fixed length, ordered and immutable (unchangeable) collection
# supports same operations as above except for functions that change the length of items
print(e)

i = {3, "test", False, 3} # set is variable length, unordered and immultable collection without dupplicates
# supports same operations as list except for getting or changing items by index (since pop and append are for last item, also don't work)
print(i)
print(i.union({1, 2, 3})) # returns combined sets
print(i.issubset({3, "test", False, 10, True})) # check if i is subset of given set
print(i.difference({3, "test", True, 12})) # returns what of i is not in given set
print(i.intersection({3, "test", False, 10, True})) # returns common items
i.add(5)
i.add(5)
i.remove(3)
print(i)

n = {"key": "value", ("test", 3): 1.0, "age": 20} # dictionaries are a collection of key-value pairs, keys must be immutable like string or set, variable length, ordered and mutable with unique keys
print(n)
print(n["key"]) # get value by key
print(n.get("key2", None)) # alternative, won't crash if key not found but instead return None
n["key"] = "value"
print(a.keys()) # returns all keys
print(a.values()) # returns all values
print(a.items()) # returns all keys and values
# len and clear also supported