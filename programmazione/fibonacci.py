class MyFibo:
    def __init__ (self, max):
        self.max = max

    def __iter__ (self):
        self.n = 0
        self.n0 = 0
        self.n1 = 1
        return self
    
    def __next__ (self):
        if self.n < self.max:
            if self.n ==0:
                result = self.n0
            if self.n == 1:
                result = self.n1
            if self.n > 1:
                result = self.n0 + self.n1
                self.n0 = self.n1
                self.n1 = result
            self.n += 1
            return result
        else:
            raise StopIteration