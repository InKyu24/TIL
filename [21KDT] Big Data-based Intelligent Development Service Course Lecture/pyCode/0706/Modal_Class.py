class Fun_cls:
    # 사용자 정의 함수 생성 (실행함수) - x, y, z 3개의 인수를 가지는 함수로 z는 기본값으로 10이 입력된다.
    def usr_fun1(x, y, z=10):
        tot = x + y + z
        print(f'x={x}, y={y}, z={z}, 합계={tot}')

    # 사용자 정의 함수 생성 (계산 결과를 돌려는 함수)
    def usr_fun2(x, y, z):
        # x, y, z, tot 변수는 usr_fun2 함수 안에서만 사용하는 지역 변수
        tot = x + y + z
        p_tot = tot * 10
        return tot, p_tot

# print(Fun_cls.usr_fun1(10, 10, 10))
# Fun_cls.usr_fun1(10, 10, 10)
# print(Fun_cls.usr_fun2(10, 10, 10))

# 사칙연산
class FourCal:
    # 생성자
    def __init__(self):
        self.result = 0

    # 함수=인스턴스=메서드
    def add(self, num1):
        self.result += num1
        return self.result

    def sub(self, num1):
        self.result -= num1
        return self.result

    def mul(self, num1):
        self.result *= num1
        return self.result

    def divi(self, num1):
        self.result /= num1
        return self.result


# # FourCal 클래스를 이용해 fcal1 객체 생성
# fcal1 = FourCal()
# print('Fourcal 클래스 result=', fcal1.result)
# fcal1.add(10)
# print('Fourcal add 계산 후 result=', fcal1.result)
# fcal1.sub(5)
# print('Fourcal sub 계산 후 result=', fcal1.result)
#
# fcal1 = FourCal()
# fcal2 = FourCal()
#
# fcal1.add(10)
# print('Fourcal 클래스 result=', fcal1.result)
# print('Fourcal 클래스 result=', fcal2.result)