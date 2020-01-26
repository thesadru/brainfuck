ascii = ['', 'SOH', 'STX', 'ETX', 'EOT', 'ENQ', 'ACK', 'BEL', 'BS', 'HT', '\n', 'VT', 'FF', 'CR', 'SO', 'SI', 'DLE', 'DC1', 'DC2', 'DC3', 'DC4', 'NAK', 'SYN', 'ETB', 'CAN', 'EM', 'SUB', 'ESC', 'FS', 'GS', 'RS', 'US', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', 'BACKSLASH', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']
line= [0]*512
pos = 256
line[pos] += 8
# Set Cell #0 to 8
while line[pos] != 0:
    pos += 1
    line[pos] += 4
    # Add 4 to Cell #1; this will always set Cell #1 to 4
    while line[pos] != 0:
        # as the cell will be cleared by the loop
        pos += 1
        line[pos] += 2
        # Add 2 to Cell #2
        pos += 1
        line[pos] += 3
        # Add 3 to Cell #3
        pos += 1
        line[pos] += 3
        # Add 3 to Cell #4
        pos += 1
        line[pos] += 1
        # Add 1 to Cell #5
        pos -= 4
        line[pos] -= 1
        # Decrement the loop counter in Cell #1
    # Loop till Cell #1 is zero; number of iterations is 4
    pos += 1
    line[pos] += 1
    # Add 1 to Cell #2
    pos += 1
    line[pos] += 1
    # Add 1 to Cell #3
    pos += 1
    line[pos] -= 1
    # Subtract 1 from Cell #4
    pos += 2
    line[pos] += 1
    # Add 1 to Cell #6
    while line[pos] != 0:
        pos -= 1
    # Move back to the first zero cell you find; this will
    # be Cell #1 which was cleared by the previous loop
    pos -= 1
    line[pos] -= 1
    # Decrement the loop Counter in Cell #0
# Loop till Cell #0 is zero; number of iterations is 8
# The result of this is:
# Cell No :   0   1   2   3   4   5   6
# Contents:   0   0  72 104  88  32   8
# Pointer :   ^
pos += 2
print(ascii[line[pos]],end='')
# Cell #2 has value 72 which is 'H'
pos += 1
line[pos] -= 3
print(ascii[line[pos]],end='')
# Subtract 3 from Cell #3 to get 101 which is 'e'
line[pos] += 7
print(ascii[line[pos]],end='')
print(ascii[line[pos]],end='')
line[pos] += 3
print(ascii[line[pos]],end='')
# Likewise for 'llo' from Cell #3
pos += 2
print(ascii[line[pos]],end='')
# Cell #5 is 32 for the space
pos -= 1
line[pos] -= 1
print(ascii[line[pos]],end='')
# Subtract 1 from Cell #4 for 87 to give a 'W'
pos -= 1
print(ascii[line[pos]],end='')
# Cell #3 was set to 'o' from the end of 'Hello'
line[pos] += 3
print(ascii[line[pos]],end='')
line[pos] -= 6
print(ascii[line[pos]],end='')
line[pos] -= 8
print(ascii[line[pos]],end='')
# Cell #3 for 'rl' and 'd'
pos += 2
line[pos] += 1
print(ascii[line[pos]],end='')
# Add 1 to Cell #5 gives us an exclamation point
pos += 1
line[pos] += 2
print(ascii[line[pos]],end='')
# And finally a newline from Cell #6