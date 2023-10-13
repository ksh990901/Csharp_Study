##########################################################
# # 함수(메서드의 특징) 
# # 다른 변수에 대입할 수 있다.
# # 인수로 전달 할 수 있다.
# # 함수 자체를 리턴 할 수 있다.
# # 컬렉션에 저장 할 수 있다.


###### 함수를 변수에 대입
# def add(a,b) :
#     print(a+b)
# plus = add
# plus(1,2)


################ 함수를 인자로 전달
# def calc(op, a, b) :
#     op(a,b)

# def add(a,b) :
#     print(a+b)

# calc(add,1,2) # add 함수에 1,2를 전달하여 수행하는 대리자 calc


################## 지역함수
# 함수 내에서만 동작하는 함수
# 주요 로직이 있을 경우에는 외부에 노출 하지 않도록 해주어야하는데. 
# (접근제하자가 없으므로 기법으로 커버)
# 외부에 노출되는 상위 메서드(함수)가 
# 대신 주요 메서드(함수)를 수행하도록 하는 기법

# def calsum(n) :
#     # 지역 함수의 생성 및 용법
#     def add(a, b) :
#         return a + b
#     sum = 0
#     for i in range(n+1) :
#         sum = add(sum, i)
#     return sum
# calsum(10)

###### 지역 함수의 활용
# def makehello(message) :

#     def hello(name) :
#         print(message + ', ' + name)

#     return hello

# 지역함수 hello를 반환받아서 "GoodMorning" 이라는 문자열이 꾸며주는 결과를
# 실행 할 수 있도록 해주는 기능 (래핑)
# enh = makehello("Good Morning")
# enh("kim")
# enh("park")
    
# # message 는 makehello() 호출 이후 메모리에서 사라져야 하는 인자 이지만
# # 지역함수를 반환하는 특징 상 클로저(closer)라는 특수한 구조를 만들어서 유지하도록 한다.


###########################################################
# # 함수 데코레이터
# # . 함수의 장식을 붙이듯이 코드의 앞 뒤로 원하는 코드를 추가하는 방법
# # . 함수를 실행하기 전에 별도의 로직을 수행하거나 검증하는 로직을 구현하는 등
# #   일련의 연속적인 일을 정의 해 두고 간단하게 호출하여 사용 할 수 있도록 하는 문법
###########################################################

######## 함수 데코레이터를 이해하기 전에 
######## 함수를 래핑하는 기법부터 학습
# # 래핑 : 주요 코드를 가운데 두고 별도의 코드를 앞 뒤로 붙여서 반복적으로 수행 가능
# #        하도록 만드는 기법
# def inner1() :
#     print('결과 출력')

# def inner2() :
#     print('결과 출력')

# def inner3() :
#     print('결과 출력')

# def outer(func) :
#     print("-" * 20)
#     func()
#     print("-" * 20)

# outer(inner1)
# "결과출력" 을 표현하기 전에 print() 기능과 표현 후 print() 기능이 덧붙여진
# inner() 함수를 호출 한 결과가 도출
# 특정한 로직을 수행할때 반복적으로 수행해야하는 로직이 있을 경우
# 래핑 기법을 사용하여 일괄적으로 처리 할 수 있다.
# outer(inner2)
# outer(inner3)

# # 주요 코드는 inner 이지만
# # 마치 outer 함수를 실행하여 결과를 받는 것처럼 보여서 코드의 가독성을 낮출수가 있다.
# # inner 메서드를 호출하는 것처럼 보이지만 래퍼 기법이 적용된 기능을 구현하도록 하는 기법을
# # 래핑 기법(패턴)이라고 함
# def inner() :
#     print("결과를 출력합니다.")

# def outer(func) :
#     def wrapper() :
#         print("-" * 20)
#         func()
#         print("-" * 20)
#     return wrapper

# inner = outer(inner)
# inner() # outer를 실행한 결과를 inner 객체에 담아서 마치 
# #inner 함수를 직접 호출 하는 것처럼 보이게 하면 되지 않을까.....
# print(inner.__name__) # wrapper을 실행하고 있는 것을 확인 할 수 있다.


####### 데코레이터의 등장 및 사용 이유

# def outer(func) :
#     def wrapper() :
#         print("-" * 20)
#         func()
#         print("-" * 20)
#     return wrapper

# @ outer
# def inner() :
#     print("결과를 출력합니다.")

# inner()
# print(inner.__name__) # wrapper를 대신 수행하는 대리자 역할의 함수 호출 임을 확인 할 수 있다.

# # 아래처럼 outer에 inner를 전달하고 wrapper를 inner로 받아서 대신 호출하는
# # 구문이 굉장히 비효율적으로 보인다.
# inner = outer(inner)
# inner() 
# # 위의 호출부분을 간단히 처리 할 수 있도록 해주는 문법(데코레이터)


# # 데코레이터의 활용
# # 웹 페이지의 태크를 자동으로 생성해 주는 데코레이터

# def makeP(func) :
#     def wrap() :
#         return "<p>" + func() + "</p>"
#     return wrap

# def makeDiv(func) :
#     def wrap() :
#         return "<div>" + func() + "</div>"
#     return wrap

# @makeDiv
# @makeP
# def printTag() :
#     return "김범수"

# print(printTag())



######### 인자를 받는 데코레이터를 생성하는 방법

# def makeP(func) :
#     def wrap(*name,**param) :
#         return "<p>" + func(*name,**param) + "</p>"
#     return wrap

# @makeP
# def printTag(name,age,job,place) :
#     return name + str(age) + job + place
# @makeP
# def printTag(prod,price) :
#     return prod + str(price)

# print(printTag("김범수", 39, "가수", "서울"))
# print(printTag("키보드" ,60000))



#########################################################
# # 클래스 데코레이터
# #  - 클래스의 객체를 호출 전, 호출 후로 수행하는 로직을 
# #    작성해 두는 기능.
# #    . 메인 함수의 클래스 래핑.
class outer : 
    def __init__(self, func) :
       self.func = func

    def __call__(self) :
       print("****")
       self.func()
       print("****")
@ outer
def inner() :
   print("결과를 출력합니다.")

inner = outer(inner)
inner()
