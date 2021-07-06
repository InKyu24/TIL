# 사용자 정의 함수 생성 (실행함수) - x, y, z 3개의 인수를 가지는 함수로 z는 기본값으로 10이 입력된다.
def usr_fun1(x, y, z=10):
    tot = x + y + z
    print(f'x={x}, y={y}, z={z}, 합계={tot}')


# 사용자 정의 함수 생성 (계산 결과를 돌려는 함수)
def usr_fun2(x, y, z):
    # 전역변수로 선언된 tot 를 가져올 수 있도록 global 키워드 사용
    global tot

    # x, y, z, tot 변수는 usr_fun2 함수 안에서만 사용하는 지역 변수
    tot = x + y + z
    return tot


# def 정의된 함수 호출, z 값 생략하면 기본값 10 입력된다.
usr_fun1(10, 10)
# def 정의된 함수 호출, z값은 20
usr_fun1(20, 20, 20)

tot = 10
p_tot = usr_fun2(10, 10, 10)
print(f'tot={tot}, p_tot={p_tot}')