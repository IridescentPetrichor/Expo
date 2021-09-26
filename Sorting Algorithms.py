class SortList():
    def __init__(self, li):
        self.li = li
        self.accesses = 0
        self.swaps = 0

    def swap(self, i1, i2):
        try:
            self.li[i1], self.li[i2] = self.li[i2], self.li[i1]
        except IndexError:
            return
        else:
            self.swaps += 1

    def read(self, i):
        out = None
        try:
            out = self.li[i]
        except IndexError:
            return
        else:
            self.accesses += 1