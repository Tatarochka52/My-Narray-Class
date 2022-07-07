import ctypes


class Narray:
    """docstring"""


    def __init__(self, size):
        """Constructor"""
        self._size = size
        self._last_index = 0
        self._capacity = 8
        self._narray = (self._size * ctypes.py_object)()
        

    def append(self, item):
        """Add object in array"""
        if self._last_index < self._size:
            self._narray[self._last_index] = item
            self._last_index += 1
        elif self._last_index < self._capacity:
            pass
        else: 
            pass


    def getitem(self, index):
        """Get object from array"""
        return self._narray[index]


    def setitem(self, index, item):
        """Set object in array with index"""
        pass


    def getarray(self):
        """Get all array"""
        pass


    def resize(self):
        """Resize array"""
        newarray = ((self._narray.size() + 1) * ctypes.py_object)()
        newarray = self._narray
        


    def size(self):
        """Get size of array"""
        pass

