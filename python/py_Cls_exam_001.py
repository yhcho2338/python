class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성".format(self.name))

    def __del__(self):
        print("{} - 파괴".format(self.name))

test = Test("A")             