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

# 전역변수로 선언된 배열의 경우 오류 없이 호출 가능
array = [1,2,3,4,5]

def func():
    array.append(6)
    print(array)

#함수 안에 선언된 지역변수가 우선
def func2():
    array = [3,4,5]
    array.append(6)
    print(array)

func()
func2()
print(array)

array = [1,2,3,4,5]
def func3():
    global array
    array = [3,4,5] #전역변수 array가 변경됨
    array.append(6)

func3()
print(array)

# 파이썬에서 함수는 여러 개의 반환 값을 가질 수 있습니다.
def operator(a,b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7,3)
print(a,b,c,d)

#람다 표현식
#특정한 기능을 수행하는 함수를 한 줄에 작성
def add(a,b):
    return a + b

#일반적인 add() 메서드 사용
print(add(3,7))

#람다 표현식으로 구현한 add() 메서드
print((lambda a,b: a + b)(3,7))

#람다 표현식 예시
#내장 함수에서 자주 사용되는 람다 함수

#점수 순으로
array = [('홍길동',50),('이순신',32),('아무개',74)]
def my_key(x):
    return x[1]

print(sorted(array, key=my_key))#내장함수 sorted : key 속성으로 함수를 넣어서 정렬기준을 명시할 수 있다.

print(sorted(array,key=lambda x : x[1]))

#람다 표현식 예시: 여러 개의 리스트에 적용
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

#map함수 : 각각의 원소에 어떠한 함수를 적용시키고자 할 때 사용
# map(int, list)
# map(함수, 리스트)
result = map(lambda a, b: a + b, list1, list2)
print(list(result))


