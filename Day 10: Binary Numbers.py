#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    binary = str(bin(n))
    #print binary
    tot=0
    tmp=0
    for i in binary:
        if i=='1':
            tmp+=1
        else:
            tot=max(tot,tmp)
            tmp=0
    tot=max(tot,tmp)
    print tot
