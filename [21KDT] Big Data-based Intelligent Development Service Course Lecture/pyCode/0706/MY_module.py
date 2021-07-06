import Modal_Class as MC
from Modal_Class import FourCal

# 클래스 상속
class FourCal_chr(FourCal):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def add_2(self):
        prn_number = self.result + self.number
        return prn_number


MC.Fun_cls.usr_fun1(20, 10, 10)

obj1 = FourCal()        # FourCal.result = 0
padd1 = obj1.add(8)     # FourCal.result = 0 + 8
padd2 = obj1.add(4)     # FourCal.result = 0 + 8 + 4
div1 = obj1.divi(2)     # FourCal.result = (0 + 8 + 4) / 2

obj2 = FourCal()        # FourCal.result = 0
print(obj2.add(20))     # FourCal.result = 20
print(obj2.add(30))     # FourCal.result = 50

obj3 = FourCal_chr(10)  # FourCal.result=0      FourCal_chr.number=10
obj3.add(1)             # FourCal.result=1      FourCal_chr.number=10
prn3 = obj3.add_2()     # FourCal.result=1      FourCal_chr.number=10   prn3 = 11

obj4 = FourCal_chr(1)   # FourCal.result=0      FourCal_chr.number=1
obj4.add(2)             # FourCal.result=2      FourCal_chr.number=1
prn4 = obj4.add_2()     # FourCal.result=2      FourCal_chr.number=1    prn4 = 3