################################################################
# # 파일 스트림 
# # 물리적 공간에 배치되어 있는 (하드디스크, 웹 서버) 파일 데이터를
# #  관리하는 기능
# # open 과 close로 프로그램과 파일 데이터 간의 흐름을 연결 / 차단
# # 특정 파일에 스트림이 연결 되어있는 경우 프로그램이 졸요하지 않는
# # 이상 외부에서 접근 할 수 없는 상태가 된다. 
# # (반드시 close()안정적으로 사용)


### 파일 쓰기
# w : 파일의 내용을 word.txt에 덮어쓰기
# t : 텍스트 유형으로 파일을 생성 / 덮어쓰기
# f : 파일 스트림 
# f = open('word.txt', 'wt') # 파일스트림 open
# message = '''
# 파일을 읽고 쓸수 있는 데이터를 작성합니다.
# 데이터는 텍스트 유형으로 저장 됩니다.
# 최초 1회 w를 통해 insert 되며
# 이후 w를 하게 되면 모든 내용이 update 됩니다.
# '''
# f.write(message) # 내용 등록
# f.close() # 파일 스트림 종료



### 파일 읽어오기
# try : 
#     f = open("word.txt", "rt") # word.txt라는 텍스트 파일에 접근하여 읽어온다.
#     message = f.read() # 읽어온 내용을 message 변수에 담가
#     print(message)
# except FileNotFoundError : # 해당 파일을 찾을 수 없을 때
#     print("찾을 파일이 없습니다.")
# finally : 
#     f.close() # 파일 스트림 닫아주기.



# try : 
#     f = open("word2.txt", "rt") # word.txt라는 텍스트 파일에 접근하여 읽어온다.
#     message = f.read() # 읽어온 내용을 message 변수에 담가
#     print(message)
# except FileNotFoundError : # 해당 파일을 찾을 수 없을 때
#     print("찾을 파일이 없습니다.")
# finally :
#     pass 
#    f.close() # 파일 스트림 닫아주기.    



### 파일 읽어오기2
# # 파일을 읽어 오면서 검증 작업을 할 때 유리
# try : 
#     f = open("word.txt", "rt") # word.txt라는 텍스트 파일에 접근하여 읽어온다.
#     while(True) : 
#         message = f.read(2) # 2자씩 읽어오기.
#         if len(message) == 0 :
#             break
#         print(message,end='')
# except FileNotFoundError : # 해당 파일을 찾을 수 없을 때
#     print("찾을 파일이 없습니다.")
# finally : 
#     f.close() # 파일 스트림 닫아주기.



### 파일 읽어오기3
# # 한줄씩 읽어오기 (개행하는 단위)
# try : 
#     f = open("word.txt", "rt") # word.txt라는 텍스트 파일에 접근하여 읽어온다.
#     while(True) : 
#         message = f.readline() # 한줄 씩 읽어오기ㅣ
#         if not message : # 읽어온 줄의 데이토가 없을 경우 break
#             break
#         print(message)
# except FileNotFoundError : # 해당 파일을 찾을 수 없을 때
#     print("찾을 파일이 없습니다.")
# finally : 
#     f.close() # 파일 스트림 닫아주기.



### 파일 읽어오기4
# # 한줄씩 읽어오기 읽어온 데이터를 리스트에 담기.
# try : 
#     f = open("word.txt", "rt") # word.txt라는 텍스트 파일에 접근하여 읽어온다. 
#     message = f.readlines() # 한줄 씩 읽어오기
#     for word in message :
#         print(word)
#     print(message, end ='')
# except FileNotFoundError : # 해당 파일을 찾을 수 없을 때
#     print("찾을 파일이 없습니다.")
# finally : 
#     f.close() # 파일 스트림 닫아주기.





### 파일 읽어오기5
# # 파일 스트림 자체를 표현하기
# try : 
#     f = open("word.txt", "rt") # word.txt라는 텍스트 파일에 접근하여 읽어온다.
#     for rows in f : 
#         print(rows, end='')
# except FileNotFoundError : # 해당 파일을 찾을 수 없을 때
#     print("찾을 파일이 없습니다.")
# finally : 
#     f.close() # 파일 스트림 닫아주기.



######## 파일 이어 쓰기
# try : 
#     f = open("word.txt", "rt") # word.txt라는 텍스트 파일에 접근하여 덧붙이기 한다.
#     f.write("\na 는 파일의 내용을 추가로 이어서 쓰는 기능 입니다.")
    
#     # 덧붙인 내용 확인하기
#     f = open("word.txt", "rt")
#     for row in f :
#         print(row,end='')
# except FileNotFoundError : # 해당 파일을 찾을 수 없을 때
#     print("찾을 파일이 없습니다.")
# finally : 
#     f.close() # 파일 스트림 닫아주기.


## 파일 스트림을 자동으로 close() 해주는 with as ######
# with open('word.txt', 'rt') as f :
#     message = f.read()
# 코드 블럭이 끝났을 때 자동 Close()
# print(message)
