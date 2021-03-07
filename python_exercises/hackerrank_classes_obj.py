#!/bin/python3

import math
import os
import random
import re
import sys


class Movie:
    def __init__(self, name, n, cost):
        self.name = name
        self.n = n
        self.cost = cost
    
    def __str__(self):
        return(f'Movie : {name}\nNumber of Tickets : {n}\nTotal Cost : {cost}')


if __name__ == '__main__':
    name = input()
    n = int(input().strip())
    cost = int(input().strip())
    
    p1 = Movie(name,n,cost)
    print(p1)



