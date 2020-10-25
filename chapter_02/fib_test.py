from collections.abc import Iterable

class Fibs:
    """
    初始化
    """
    def __init__(self):
        self.a = 0
        self.b = 1

    """
    命名迭代器
    """

    def __next__(self):

    #    self.b = self.a+self.b
    #    self.a = self.b
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


fibs = Fibs()
print(isinstance(fibs, Iterable))

for i in fibs:
    if i > 1000:
        print(i)
        break
