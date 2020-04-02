class Test:
    def prt(self):
        print(self)
        print(self.__class__)
        print(self.__class__.__name__)

t=Test()
t.prt()
print(id(t))
print(hex(id(t)))
print(t.__class__)