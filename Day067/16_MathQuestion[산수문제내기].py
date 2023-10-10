# #############################################
# # # 임의의 수 2개 덧셈 맞추기 
# import random
# a = random.randint(1,9) # 1 ~ 9 임의의값
# b = random.randint(1,9) # 1 ~ 9 임의의값
# question = "%s + %s = " %(a,b)
# ans  = int(input(question)) # 질/답 동기화
# if ans == a + b:
#     print("정답입니다.")
# else : 
#     print("틀렸습니다.")




#############################################
# # 임의의 수 2개 덧셈 맞추기 
# # 반복 해서 물어보되 0 을입력하면 프로그램 종료하기
# # 총 질문의 횟수 와 정답의 횟수 를 종료 전 표현

# import random

# questionCnt = 0 # 질문의 횟수
# resultCnt   = 0 # 정답 횟수
# while True :
#     questionCnt += 1 # 질문의 횟수 증가
#     a = random.randint(1,9) # 1 ~ 9 임의의값
#     b = random.randint(1,9) # 1 ~ 9 임의의값
#     question = "%s + %s = " %(a,b)
#     ans  = int(input(question)) # 질/답 동기화
#     if ans == 0 : 
#         break
#     elif ans == a + b :
#         resultCnt += 1 # 정답 횟수가 1 증가
#         print("정답입니다.")
#     else : 
#         print("틀렸습니다.")
# print("총 %d 문제 중 정답횟수는 %d" % (questionCnt, resultCnt))






#############################################
# # 임의의 수 2개 덧셈 맞추기 
# # 반복 해서 물어보되 0 을입력하면 프로그램 종료하기
# # 총 질문의 횟수 와 정답의 횟수 를 종료 전 표현 
# # 사칙 연산 을 임의로 받아서 결과 를 비교 하기. 

# import random

# questionCnt = 0 # 질문의 횟수
# resultCnt   = 0 # 정답 횟수
# op = ['+','-','*','/'] # 임의로 추출 할 사칙 연산 기호


# def rans() : # 정답을 맞추었을때 실행할 함수
#     global resultCnt
#     resultCnt += 1 # 정답 횟수가 1 증가
#     print("정답입니다.")


# while True :
#     questionCnt += 1 # 질문의 횟수 증가
#     a = random.randint(1,9) # 1 ~ 9 임의의값
#     b = random.randint(1,9) # 1 ~ 9 임의의값
#     r = random.randrange(len(op)) # 0 ~ 3  사칙연산 리스트에서 임의의 기호 받아내기
#     question = "%s %s %s = " %(a,op[r],b)
#     ans  = int(input(question)) # 질/답 동기화
#     if ans == 0 : 
#         break
#     elif r == 0 and ans == a + b :
#         rans()
#     elif r == 1 and ans == a - b :
#         rans()
#     elif r== 2 and ans == a * b :
#         rans()
#     elif r== 3 and ans == a / b :
#         rans()
#     else : 
#         print("틀렸습니다.")
# print("총 %d 문제 중 정답횟수는 %d" % (questionCnt, resultCnt))





        
#############################################################################
# # 실습 
# # 숫자 0을 종료 시그널로 입력 하였는지 구분하는 로직으로 업데이트
#############################################################################
# # 1. 함수 등록을 통한 리펙터링 으로 코드 간결화 해서 로직 완성하기
# import random

# questionCnt = 0 # 질문의 횟수
# resultCnt   = 0 # 정답 횟수
# op = ['+','-','*','/'] # 임의로 추출 할 사칙 연산 기호


# def rans(_r,_a,_b) :
#     global resultCnt
#     # 정답인지 비교 로직 추가
#     if (_r == 0 and ans == _a + _b) or (_r == 1 and ans == _a - _b) or (_r== 2 and ans == _a * _b) or (_r== 3 and ans == _a / _b) :
#         resultCnt += 1 # 정답 횟수가 1 증가
#         print("정답입니다.")
#     else : 
#         print("틀렸습니다.")

# while True :
#     questionCnt += 1 # 질문의 횟수 증가
#     a = random.randint(1,9) # 1 ~ 9 임의의값
#     b = random.randint(1,9) # 1 ~ 9 임의의값
#     r = random.randrange(len(op)) # 0 ~ 3  사칙연산 리스트에서 임의의 기호 받아내기
#     question = "%s %s %s = " %(a,op[r],b)
#     ans  = int(input(question)) # 질/답 동기화
#     if ans == 0 : # 사용자가 0 을 입력하였을 경우 
#         # 프로그램 종료 인지 또는 정답을 입력하였는지 판단하기 위해 질문
#         if "Y" == input("0 을입력, 종료 : Y , 정답 : N ? ").upper() :
#             break
#         else : # 정답 을 입력 한 것이라고 했을때
#             rans(r,a,b)
    
#     # 사용자가 0 을 입력하지 않았을 경우 정답 비교 
#     else : 
#         rans(r,a,b) 

# print("총 %d 문제 중 정답횟수는 %d" % (questionCnt, resultCnt))





# # 2. 분기 문 을 간결하게 줄여서 코드 리펙터링 
# # 리펙토링 : 기존의 소스 코드의 결과 를 그대로 두고 코드를 효율적이거나(메모리) 가독성이 좋도록
# #           수정하는 기법. ( 패턴 )
# import random

# questionCnt = 0 # 질문의 횟수
# resultCnt   = 0 # 정답 횟수
# op = ['+','-','*','/'] # 임의로 추출 할 사칙 연산 기호 


# while True :
#     questionCnt += 1 # 질문의 횟수 증가
#     a = random.randint(1,9) # 1 ~ 9 임의의값
#     b = random.randint(1,9) # 1 ~ 9 임의의값
#     r = random.randrange(len(op)) # 0 ~ 3  사칙연산 리스트에서 임의의 기호 받아내기
#     question = "%s %s %s = " %(a,op[r],b)
#     ans  = int(input(question)) # 질/답 동기화
    
#     # 사용자가 0 을 입력하였을 경우 
#     # 프로그램 종료 인지 또는 정답을 입력하였는지 판단하기 위해 질문
#     if ans == 0 and "Y" == input("0 을입력, 종료 : Y , 정답 : N ? ").upper() :  
#         break
#     # 사용자가 0 을 입력하지 않았을 경우 정답 비교 
#     else : 
#         if (r == 0 and ans == a + b) or (r == 1 and ans == a - b) or (r== 2 and ans == a * b) or (r== 3 and ans == a / b) :
#             resultCnt += 1 # 정답 횟수가 1 증가
#             print("정답입니다.")
#         else : 
#             print("틀렸습니다.") 

# print("총 %d 문제 중 정답횟수는 %d" % (questionCnt, resultCnt))






#############################################################
# # 0 ~ 100 까지 의 숫자 맞추기
# # . 틀렸을 경우 UP / Down 여부를 알려주기
# # . 정답일 경우 시도 회수 표현하기.
############################################################
# import random as rn

# # 컴퓨터가 생각하는 값
# value = rn.randint(1,100) # 이상 , 이하
# count  = 0 # 총 시도 횟수
# while (True) :
#     count += 1 
#     ians = int(input("값을 입력 하세요 (정수) : "))
#     if value ==  ians :
#         break
#     elif value > ians :
#         print("더 큽니다.") 
#     else :
#         print("더 작습니다.")
# print("정답입니다. 총 시도 횟수 : ", count)
