class C:
    def __init__(self, v):
        self.value = v

    def show(self):
        print(self.value)

    def getValue(self):
        return self.value

    def setValue(self, v):
        self.value = v


c1 = C(10)
print(c1.value)

c1.value = 20
print(c1.value)
c1.show()

print(c1.getValue())
c1.setValue(60)
print(c1.getValue())
