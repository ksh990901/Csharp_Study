#############################################################
# # 문자열 (문자가 열거된 형태)
# # . 문자들을 일렬로 나열시켜 순서에 맞게 index를 부여한 형태
############################################################
# svalue = 'Python' 
# print(svalue[2])
# print(svalue[-2])

# for char in svalue :
#     print(char, end="")

# # 문자열을 나타내는 범위를 지정하여 문자를 추출
# # len() : 열거형 데이터의 개수를 구할 수 있는 함수.
# for index in range(1,len(svalue)) :
#     print(svalue[index], end='')

# # 문자열의 index로 문자를 변경할 수 없습니다.
# svalue[1] = 'p'

#############################################################
# # 불변 객체 (immuteable)
# # 데이터를 새로 갱신하여 재 배치 하는 프로세스 보다 메모리 손실을
# # 감안 하더라도 새로운 메모리 영역에 데이터를 할당하는것이
# # 더 효율적이기 때문에 사용
#############################################################
# svalue = "안녕하세요." # 안녕하세요 메모리 등록
# svalue += "반갑습니다." # 안녕하세요 반갑습니다. 메모리 등록
# print(svalue)

# # stringIO 모듈
# # 불법객체인 str의 메모리 손실을 효율적으로 등작할수 있도록 해주는 모듈
# # 다소 코딩이 복잡하지만 대용량의 데이터를 관리할때는 필수(중요)
# from io import StringIO
# bf = StringIO()
# bf.write("안녕하세요.")
# bf.write("반갑습니다.")
# result = bf.getvalue()
# bf.close()
# print(result)

#############################################################
# # 문자열 슬라이스 (범위 지정)
#############################################################
svalue = 'Python.py'
# print(svalue[2:5]) #  2 ~ 4 인덱스 문자 추출 tho
# print(svalue[3:]) # 3 ~ 마지막 까지 hon.py
# print(svalue[:4]) # 0 ~ 3 index 까지
# print(svalue[2:-3]) # 2 ~ ( -3 -1 ) = -4 index 까지표현 
# print(svalue[-3:]) # 0 -3 문자열 부터 끝까지 표현 (확장자 추출) .py 

# # 건너뛰면서 문자를 추출하는 기능
# print(svalue[::2]) # 0부터 2step : Pto.y
# print(svalue[::-2]) # 마지막 index 부터 -2칸씩 들여서 표현
# print(svalue[2::2]) # 2부터 2step
# print(svalue[-2::-2]) # -2 index로부터 2칸씩 들여서 표현
# print(svalue[::-1]) # 문자열 반전
# print(svalue[2:8:2]) # 2 ~ 7까지 2step


##############################################################
# # 문자열 메서드
# # 문자열을 다룰 수 있도록 만들어 둔 클래스에서 제공하는 문자열 클래스의 기능(Function)
##############################################################
svalue = "Python Programming"
print(svalue.find('o')) # 0 index 부터 가장 가까운 o의 index를 반환 (없으면 -1)
print(svalue.rfind('og')) # 마지막 index 부터 처음 나타나는 'og' 의 o index를 반환
print(svalue.index('x')) # 왼쪽에서 찾는다 없으면 오류
print(svalue.count('n')) # n 문자열의 개수를 반환한다.

# 메서드가 반환하는 데이터 타입은 int
print(svalue.count('n'), type(svalue.count('n')))

# 2023.01 ~ 현재까지 안도이 연령별 성비 확인
# 통계 데이터에서 '남자'의 데이터의 개수를 확인할 때.
if svalue.count('남자') > svalue.count('여자') :
    pass
