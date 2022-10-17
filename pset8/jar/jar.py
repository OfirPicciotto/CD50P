class Jar:
    def __init__(self, capacity=12, size = 0):
        self.capacity = capacity
        self.size = size


    def __str__(self):
        num_cookies = self.size *  "🍪"
        return num_cookies


    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many Cookies")
        else:
            self.size += n


    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Too few Cookies")
        else:
            self.size -= n


    @property
    def capacity(self):
        return self._capacity


    @capacity.setter
    def capacity(self, amnt):
        if int(amnt) >= 0:
            self._capacity = amnt
        else:
            raise ValueError("Invalid Value")


    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, amnt):
        if int(amnt) >= 0:
            self._size = amnt
        else:
            raise ValueError("Invalid Value")