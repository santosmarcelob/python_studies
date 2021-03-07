#!/bin/python3

import math
import os
import random
import re
import sys


class comp():
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def add(self, other):
        sum_real = self.real + other.real
        sum_img = self.img + other.img
        return(f'Sum of the two Complex numbers :{sum_real}+{sum_img}i')

    def sub(self, other):
        sub_real = self.real - other.real
        sub_img = self.img - other.img
        return(f'Substraction of the two Complex numbers :{sub_real}+{sub_img}i')
#
#Write your code here

if __name__ == '__main__':
    
    real1 = int(input().strip())
    img1 = int(input().strip())
    
    real2 = int(input().strip())
    img2 = int(input().strip())
    
    p1 = comp(real1,img1)
    p2 = comp(real2,img2)

    p1.add(p2)
    p1.sub(p2)
