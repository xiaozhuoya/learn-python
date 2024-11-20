#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Jie Zhuo'

import sys

def test():
    args = sys.argv
    
    if len(args) == 1:
        # ['hello.py']
        print('Hello, world!')
        
    elif len(args) == 2:
        # ['hello.py', 'Zhuo']
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
        