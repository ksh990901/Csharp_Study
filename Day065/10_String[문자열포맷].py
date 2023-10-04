while True:
    identity = input("주민등록 번호 를 입력 하세요: ").replace("-","").replace(" ","")
    
    ###################### 벨리 데이션 : 검증 로직 먼저 수행 #############################
    if not identity.isnumeric() : # 숫자를 입력 하지 않은 경우 리턴
        print("숫자 만 입력하세요")
        continue
    #### 숫자 만 입력되어있는 상태
    if len(identity) != 13 :
        print("주민등록 번호 는 13자리를 입력하세요.")
        continue
    ####################################################################################

    # 정상 적으로 데이터를 받았기 때문에 비교하는 로직 
    result = "성별 : "
    sung = identity[6] #9000001111111
    if sung == "1" or sung == "3" : result += "남자"
    elif sung == "2" or sung == "4" : result += "여자"
    else : 
        print("성별을 확인할 수 없습니다.")
        continue
    age = int(identity[:2]) #9000001111111
    result += " %d 살입니다." %  (23 + (100 - age))   if age > 23 else    (23 - age)
    print(result)
    break
