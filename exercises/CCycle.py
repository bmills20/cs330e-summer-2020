#!/usr/bin/env python3

from itertools import cycle

# ------
# CCycle.py
# ------

# cycle(p): iterates through a given iterable indefinitely until explicitly broken
class cycle_class() :
    def __init__(self, s):
        self.s = iter(s)
        self.t = s
        self.exhausted = False
        try:
            self.next_item = next(self.s)
        except StopIteration:
            self.exhausted = True
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.exhausted:
            raise StopIteration
        else :
           i = self.next_item
           try:
               self.next_item = next(self.s)
           except StopIteration:
               self.s = iter(self.t)
               self.next_item = next(self.s)
           return i




'''
class cycle_class() :
   def __init__(self, s) :
      self.s = s
      self.i = 0
      self.size = len(s)
   
   def __iter__(self) :
      return self
      
   def __next__(self) :
      if self.size == 0 :
         raise StopIteration() 
      else :          
         j = self.i
         self.i += 1
         if self.i == self.size : 
            self.i = 0
         return self.s[j]
 '''
