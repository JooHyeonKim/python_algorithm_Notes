# def 함수명(매개변수):
#     실행할 소스코드
#     return 반환 값

def add(a,b):
    return a+b

def subtract(a,b):
    return a - b

result = add(3,7)
print(result)

result = subtract(3,7)
print(result)

def add(a,b):
    print('함수의 결과:',a+b)
add(b=3, a=7)

#global 키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조하게 됩니다.
a=0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)