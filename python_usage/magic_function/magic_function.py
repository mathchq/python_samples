# coding:utf-8

import os
from cached_property import cached_property

class queue:
    def __init__(self, vars=None):
        if vars is not None:
            self._data = list(vars)
        else:
            self._data = []
            self._x = None
            
    def __getitem__(self, i):
        return self._data[i]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return 'my queue'

    @cached_property
    def cached_x(self):
        print('called cached x')
        return 11


    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, src):
        if isinstance(src, int):
            self._x = src
        
    @x.deleter
    def x(self):
        del self._x

    
if __name__ == '__main__':
    A = queue(range(6))
    A.x = 5
    
    print(A[1])
    print(len(A))
    print(A.x)
    print(A.cached_x)
    print(A.cached_x)