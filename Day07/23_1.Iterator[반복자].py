###############################################################
# # 반복 가능한 클래스
# # 요소가 열거되어있는 (n개 이상의 요소를 가지고 있는)
# # 자료형 구조 에서 순차적으로 요소를 추출 할 수 있는 기능이 포함된 클래스
# # . next() -> __next__()

# # 데이터를 순차적으로 반환하는 반복 가능한 클래스 만들기
# class MyList:
#     def __init__(self,*data):
#         self.data = data
#         self.index = -1  # 추출하는 요소의 index를 나타내는 인.변
#     def __next__(self) :
#         # 요소를 하나씩 추출하여 반환하는 메서드
#         self.index += 1
#         if self.index == len(self.data) :
#             # 요소의 끝 가지 모두 반환을 다 한 상태라면
#             # while을 종료하는 시그널을 보내주어야 하는데
#             # return -1 : 실제 요소의 값이 -1이라면 정상적인 요소추출을 할 수 없다.
#             raise Exception
#         return self.data[self.index]

# lists = MyList(10,20,30,40,50,60)
# while True:
#     # result : 추출한 요소를 담을 변수
#     try :  
#         result = next(lists)
#         if result == -1 :
#             break
#         print(result)
#     except Exception :
#         break


############### 위의 MyList 를 For에 적용 오류 !!!!!!!!!!
# class MyList:
#     def __init__(self,*data):
#         self.data = data
#         self.index = -1  # 추출하는 요소의 index를 나타내는 인.변
#     def __next__(self) :
#         # 요소를 하나씩 추출하여 반환하는 메서드
#         self.index += 1
#         if self.index == len(self.data) :
#             # 요소의 끝 가지 모두 반환을 다 한 상태라면
#             # while을 종료하는 시그널을 보내주어야 하는데
#             # return -1 : 실제 요소의 값이 -1이라면 정상적인 요소추출을 할 수 없다.
#             raise Exception
#         return self.data[self.index]
# lists = MyList(10,20,30,40,50,60)

# list 클래스는 반복적으로 처리하는 구문이 포함되어 있지만
# For 문법이 구동 할 수 있는 Iterator(반복자) 상태가 아니다.



####### For문이 인식할 수 있는 반복자로 만들기
# # For문에서 필요한 반복자의 조건 : 아래의 내용이 구현 되어 있어서 일치시켜주어야 한다.
# # 1.__Iter__ 특수 메서드를 호출할 수 있도록 해야한다.
# # 2. 요소추출이 종료 되었을 경우 예외상황을 StopIteration을 발생시켜야 한다.
# class MyList:
#     def __init__(self,*data):
#         self.data = data
#         self.index = -1  # 추출하는 요소의 index를 나타내는 인.변
#     def __iter__(self) : # FOR문이 호출하여 반복자 임을 확인하는 __Iter메서드
#         return self 
#     def __next__(self) :
#         # 요소를 하나씩 추출하여 반환하는 메서드
#         self.index += 1
#         if self.index == len(self.data) :
#             # 요소의 끝 가지 모두 반환을 다 한 상태라면
#             # while을 종료하는 시그널을 보내주어야 하는데
#             # return -1 : 실제 요소의 값이 -1이라면 정상적인 요소추출을 할 수 없다.
#             raise StopIteration # 요소 추출이 끝났음을 알리는 예외 클래스
#         return self.data[self.index]
# lists = MyList(10,20,30,40,50,60)

# for value in lists :
#     print(value)
# list 클래스는 반복적으로 처리하는 구문이 포함되어 있지만
# For 문법이 구동 할 수 있는 Iterator(반복자) 상태가 아니다.

