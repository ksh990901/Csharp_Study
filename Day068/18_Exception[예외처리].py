############################################################
# # 예외 처리
# # try / except
# # . 프로그램을 실행할 때 개발자가 미연에 알아차리지 못한 오류나
# # . 사용자의 예외 데이토 입력 상황통신 규약에 맞지 않는
# # . 데이터의 전송 등의 예외 상황
# #  유연하게 대처하고 프로그램의 유지 보수를 도와준다.
# #  . 사용자에게 시스템 오류를 노출하지 않고 올바르게 로직을 처리
# # 할 수 있게 하여 프로그램의 신뢰성을 높이고, 사용자에게
# # 올바른 사용을 유도 할 수 있다.



# # try, except의 기본용법
# while  (True) :
#     # 점수로 문제를 입력할수도 있는 상황
#     ivalue = input("점수를 입력하세요.")
#     score = 0
#     try : 
#         # 입력받은 내용을 정수로 형변환
#         score = int(ivalue)
#     except :
#         print("정수만 입력하세요.")
#         score = 100
#     print("값 : ", score)


# # except의 종류
# # Exception : 예외 상황의 최상위 클래스. (모든 예외 상황을 검출할 수 있다.)
# 점수로 문제를 입력할수도 있는 상황
ivalue = input("점수를 입력하세요.")
score = 0
try : 
        # 입력받은 내용을 정수로 형변환
    score = int(ivalue)
except Exception :
    print("정수만 입력하세요.")
    score = 100
print("값 : ", score)



# # Exception : 예외 상황의 최상위 클래스. (모든 예외상황을 검출 할 수 있다.)
# ivalue = input("점수를 입력하세요.")
# score = 0
# try : 
#     # 입력받은 내용을 정수로 형변환
#     score = int(ivalue)
# except TypeError : # 데이터 타입 형 변환에 실패 하였을 경우
#     print("타입형 변환에 실패")
#     score = 20
# print("값 : ", score)



# # # Exception : 예외 상황의 최상위 클래스. (모든 예외상황을 검출 할 수 있다.)
# ivalue = input("점수를 입력하세요.")
# score = 0
# try : 
#     # 입력받은 내용을 정수로 형변환
#     score = int(ivalue)
# except TypeError : # 데이터 타입 형 변환에 실패 하였을 경우
#     print("타입형 변환에 실패")
#     score = 20
# except ValueError : # 값의 형식을 잘못 입력하였을 경우
#     print("값의 형식 변환에 실패")
#     score = 100
# print("값 : ", score)


# # # Exception : 예외 상황의 최상위 클래스. (모든 예외상황을 검출 할 수 있다.)
# ivalue = input("점수를 입력하세요.")
# score = 0
# try : 
#     # 입력받은 내용을 정수로 형변환
#     score = int(ivalue)
# except ValueError : # 값의 형식을 잘못 입력하였을 경우
#     print("타입형 변환에 실패")
#     score = 20
# except Exception : # 데이터 타입 형 변환에 실패 하였을 경우
#     print("타입형 변환에 실패")
#     score = 20
# print("값 : ", score)



## 예외 상황의 강제 발생 raise
# ivalue = input("점수를 입력하세요.")
# score = 0
# try : 
#         # 입력받은 내용을 정수로 형변환
#     score = int(ivalue)
#     if score > 100 :
#         raise Exception("100보다 큰수는 입력 할 수 없습니다.")
# except ValueError : # 값의 형식을 잘못 입력하였을 경우
#     print("타입형 변환에 실패.")
#     score = 20    
# except Exception as ex : # 에러 클래스의 최상위 검출 클래스
#     print(ex)
#     score = 20
# print("값 : ", score)




# # finally
# ivalue = input("점수를 입력하세요.")
# score = 0
# try : 
#     # 입력받은 내용을 정수로 형변환
#     score = int(ivalue)
#     if score > 100 :
#         raise Exception("100 보다 큰수는 입력 할 수 없습니다.")
#     print("데이터 저장 완료 Commit")
# except ValueError : # 값의 형식을 잘못 입력하였을 경우
#     print("타입형 변환에 실패.")
#     print("데이터 복구 rollback")
#     score = 20    
# except Exception as ex : # 에러 클래스의 최상위 검출 클래스
#     print(ex)
#     print("데이터 복구 rollback")
#     score = 20
# finally : 
#     print("데이터 베이스 접속을 차단 합니다.")
# print("값 : ", score)


# ### 예외 상황의 검출
# # # try / except 를 간결하게 처리 할 수 있도록 줄인구문
# # # 특정 시점의 예외 상황을 발생 시켜 로직을 검중 할 때 사용

# value = input("점수를 입력하세요.")
# try :     
#     score = int(value)
# # 100 이하가 아니라면 예외상황을 발생
#     assert score <= 100 , "134행 : 점수 범위 초과"
# except : 
#     pass
# print(score) 


# ### 예외 상황의 검출
# # # try / except 를 간결하게 처리 할 수 있도록 줄인구문
# # # 특정 시점의 예외 상황을 발생 시켜 로직을 검중 할 때 사용

# value = input("점수를 입력하세요.")
# try :     
#     score = int(value)
# # 100 이하가 아니라면 예외상황을 발생
#     assert score <= 100 , "134행 : 점수 범위 초과"
# except ValueError : # 값의 형식을 잘못 입력하였을 경우
#     print("타입형 변환에 실패.")
#     print("데이터 복구 rollback")
#     score = 20    
# except Exception as ex : # 에러 클래스의 최상위 검출 클래스
#     print(ex)
#     print("데이터 복구 rollback")
#     score = 20
# print(score)


### 예외 상황의 검출
# # try / except 를 간결하게 처리 할 수 있도록 줄인구문
# # 특정 시점의 예외 상황을 발생 시켜 로직을 검중 할 때 사용

value = input("점수를 입력하세요.")
try :     
    score = int(value)
# 100 이하가 아니라면 예외상황을 발생
    assert score <= 100 , "170행 : 점수 범위 초과"
except ValueError : # 값의 형식을 잘못 입력하였을 경우
    print("타입형 변환에 실패.")
    print("데이터 복구 rollback")
    score = 20    
except AssertionError as ae : # 에러 클래스의 최상위 검출 클래스
    print(ae)
print(score)
