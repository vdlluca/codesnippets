print(5 + 5)
print(2 - 10)
print(5 * 7)
print(8 / 3) # results in floating point
print(8 // 3) # whole division
print(8 % 3) # moduli
print(3 ** 5) # power (3 ^ 5)

print(15 >> 3) # binary shift to right (0b1111 -> 0b001), equivalent to halving and rounding down n-times (here 3)
print(6 << 1) # binary shift to left (0b0110 -> 0b1100), equivalent to doubling n-times (here 1)

a = 5
a += 5 # shorthand for a = a + 5, possible with all operators
print(a)

print(2 + 2 * (5 - 3)) # operator precedence of math is respected

# boolean operators
print("hey" == "hi") # check if equal, != for unequal
print(10 < 20) # check if smaller than, <= for smaller than or equal to
print(5 >= 10) # check if bigger than or equal to, > for bigger than
print(True or False) # returns True if either values is True
print(not True) # inverts boolean
print(True and False) # returns True if both values are True
