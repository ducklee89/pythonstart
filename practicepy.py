class Mynumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 100:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)