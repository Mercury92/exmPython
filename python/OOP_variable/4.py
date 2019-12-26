class C:
    def __init__(self, v):
        self.__value = v

    def show(self):
        print(self.__value)
    #
    # def getValue(self):
    #     return self.value
    #
    # def setValue(self, v):
    #     self.value = v

# 인스턴스 변수 사용되지 않게 하려면 __를 붙여주면 된다.
c1 = C(10)
print(c1.__value)
# print(c1.value)
#
# c1.value = 20
# print(c1.value)
# c1.show()
#
# print(c1.getValue())
# c1.setValue(60)
# print(c1.getValue())
# #sdsdf
