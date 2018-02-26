class MathDojo(object):
    def __init__(self):
        self.value = 0

    def add(self, *number):
        mod = 0
        for val in number:
            if isinstance(val, list):
                for num in range(0, len(val)):
                    mod+=val[num]
            elif isinstance(val, tuple):
                for num in val:
                    mod+=num
            else:
                mod+= val
            # print mod
        self.value += mod
        return self

    def subtract(self, *number):
        mod = 0
        for val in number:
            if isinstance(val, list):
                for num in range(0, len(val)):
                    mod+=val[num]
            elif isinstance(val, tuple):
                for num in val:
                    mod+=num
            else:
                mod+= val
            # print mod
        self.value -= mod
        return self

    def result(self):
        print self.value

md = MathDojo()
md.add([1], 3,4).add([3,5,7,8], (2,4.3,1.25)).subtract(2, [2,3], [1.1,2.3]).result()