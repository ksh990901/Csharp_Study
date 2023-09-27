#######################################################################
# # 가변 인자(가변 인수)
# # ~ N 개의 인수를 유동적으로 받아서 처리하기
#############################################################
# # *ints 라는 가변인자 변수를 설정하여 intsum 을 함수를 호출 할때 N개의 
# # 힌수를 전달하는 예시
# def intsum(*ints) :
#     sum = 0
#     for num in ints :
#         sum += num
#     return sum

# print(intsum(1,2,3))




# 인수 인자 데이터 형식에 구애 받지 않고 모두 수용하여 처리.
# def intsum(*ints) :
#     sum = 100
#     return sum

# print(intsum(1,True,10.2,'안녕하세요'))

# # 가변인자는 튜블 형태이며 임의로 수정할 수 없다.
# def intsum(*ints) :
#     ints[0] = 10
#     return ints[0]

# print(intsum(1,True,10.2,'안녕하세요.'))

#############################################################
# # 가변 인자의 위치 
# # 반드시 인자 배열의 마지막 위치에 등록 되어야 한다.
#############################################################
# # 담을 범위가 모호해 지므로 가변 인자는 인자의 앞쪽이나 중간에 올 수 없다.
# def intsum(*svalue, *svalue2) :
#     print('안녕하세요.')
# intsum(1,2,3,4,5,6,7,8,9)


# # 가변인자는 앞에 위치 할 수 없다.
# def intsum(*svalue, svalue2) :
#     print("안녕하세요.")

# intsum(1,2,3,4,5,6,7,8,9)


# # 파이썬은 오버로딩 기능을 지원하지 않는다.
# # 오버로딩
# # . 같은 이름의 메서드(함수)를 인자의 구성에 따라서 여러개 만들수 있도록 하는 기능
# def intsum(svalue, *values) :
#     print(svalue, "첫번재 함수")

# def intsum(svalue) :
#     print(svalue, "두번째 함수")

# intsum("1")
# intsum("1",1,2,3,4)

##############################################################
# # 선택적 인수
# # 인자의 기본값을 주는 기능.
# # 코드의 유지보수성을 향상시키기 위하여 사용
#############################################################
# # 선택적 인수 기능을 통하여 기존에 사용하던 로직은 수정하지 않고 유연하게
# # 프로젝트를 유지보수 할 수 있다.
