#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    out = "NO"
    
    if (x1 != x2):
        if(x1 < x2):
            if(v1 > v2):
                fast_pos = x1
                slow_pos = x2
                print("I am here")
                while(fast_pos <= slow_pos):
                    if (fast_pos == slow_pos):
                        out = "YES"
                        break
                    fast_pos += v1
                    slow_pos += v2
                
        elif (x1 > x2):
            if(v1 < v2):
                fast_pos = x2
                slow_pos = x1
                while(fast_pos <= slow_pos):
                    if (fast_pos == slow_pos):
                        out = "YES"
                        break
                    fast_pos =+ v2
                    slow_pos =+ v1
    else:
        out = "YES"

    return out


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = [0, 3, 4, 2]

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    print (result)
    # fptr.write(result + '\n')

    # fptr.close()
