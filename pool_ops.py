#!/usr/bin/env python
#  pool_ops.py
#
# Calculates the output shape and operation count of an average pooling layer
#
# Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: none
#
# Parameters:
#    c_in                input channel count
#    h_in                input height count
#    w_in                input width count
#    h_pool              average pooling kernel height count
#    W_pool              average pooling kernel width count
#    s                   stride of average pooling kernel
#    p                   amount of padding on each of the four input map sides
#
# Output:
#    Print output values to screen, including the output channel count,
#    height count, width count, number of additions performed, number of
#    multiplications performed, and number of divisions performed
#
# Revision history:
#    10/22/2024          Script created
#
###############################################################################

#Import relevant modules
import sys
from math import floor

#Define constants
const1 = 0

#User-defined functions
def user_function(param1, param2):
   return param1 + param2

#Pre-initialize input parameters
c_in = float('nan') #Input channel count
h_in = float('nan') #Input height count
w_in = float('nan') #Input width count
h_pool = float('nan') #Average pooling kernel height count
w_pool = float('nan') #Average pooling kernel width count
s = float('nan') #Stride of average pooling kernel
p = float('nan') #Amount of padding on each of the four input map sides

#Arguments are strings by default
if len(sys.argv) == 8:
   c_in = float(sys.argv[1])
   h_in = float(sys.argv[2])
   w_in = float(sys.argv[3])
   h_pool = float(sys.argv[4])
   w_pool = float(sys.argv[5])
   s = float(sys.argv[6])
   p = float(sys.argv[7])
else:
   print('Usage: python3 pool_ops.py c_in h_in w_in h_pool w_pool s p')
   sys.exit()

#Main body of script

#Calculate the number of output channels
c_out = c_in

#Calculate the height and width of the output map
h_out = floor(((h_in + 2 * p - h_pool) / s) + 1)
w_out = floor(((w_in + 2 * p - w_pool) / s) + 1)

#Calculate total number of additions, multiplications, and divisions
muls = 0 #Zero for standard convolutions
adds = c_in * h_out * w_out * (h_pool * w_pool - 1)
divs = c_in * h_out * w_out

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
