# Bitwise left shift operator (<<)      # For +ve number

                    # This operation effectively multiplies the number by 2^n, where n is the number of positions shifted.
# result = a << n     # a is the number to shift.
                    # n is the number of positions to shift to the left.

a = 5       # In binary: 0101
n = 1       # Shift left by 1 position
            # converts to 8 bit => 000000101  Shifting 000000101 one position to the left gives 00001010, which is 10 in decimal
print(5<<1)  # Output: 10

a = 3       # In binary: 0011
n = 2       # Shift left by 2 positions
result = a << n
print(3<<2)  # Output: 12     

# Bitwise left shift operator (>>)      # For -ve number 

a = 5       # In binary: 0101
n = 1       # IShift Left by 1 position
            # converts to 8 bit => 000000101
            invert the bit: 111111010   # 1st complemet

a = -10 
print(a<<1)