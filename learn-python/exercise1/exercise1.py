#!/usr/bin/python
# -*- coding: utf-8 -*- 

from __future__ import division
total_num = int(raw_input('How many numbers? '))
numbers = []
for i in range(1, total_num+1):
    numbers.append(int(raw_input('Enter number %d: ' % i)))
    print 'The largest number is ', max(numbers)
    print 'The smallest number is ', min(numbers)
    print 'The average is ', round((sum(numbers)/total_num), 2)

