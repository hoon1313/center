#함수적용
def sonsil(a,b):   
    a = num1
    b = num2
    result = int(a)+int(b)
    return result   

#수면매수용 리스트 작성 & 글자길이순으로 정렬
su = ['리플(0)','리스크(1)','메디블록(2)','온톨로지(3)','비트토렌트(4)','스트라이크(5)','베이직어텐션토큰(6)']
su.sort(key=len)

#이름 및 정보 입력 (딕셔너리)
name1 = input("이름을 입력하세요 : ")
id = {'이름': name1 , '전화번호':'010-0000-1111', '생년월일': '1999.01.01', '학번' : '20170947'}

#게임시작
print(name1,"님 반갑습니다!")
print(name1,"님의 정보를 보시겠습니까? [Y/N] ") 

#유저 정보확인 예스 올 노
user = str(input(">> "))

#정보확인에 Y를 쳤을 때
if user == "Y": 
    print("정보를 읽은 후, 게임을 시작합니다." ) 
    print(id,"\n") 

#게임시작 & 금액충전
print("업비트 접속 완료.")
print("얼마를 충전하시겠습니까? ")
money = int(input("충전금액 : "))
print(money,"원이 충전되었습니다.\n")

#도지코인 샀을때와 비트코인 샀을때 가격 상승하락
doge = int(money*1.4)
bitcoin = int(money*0.7)

#충전된 돈으로 코인구매과정
print("충전된 돈",money,"원으로 어떤코인을 구매할까요?")
print("1.도지코인 2.비트코인 3.수면매수 ")
num = int(input("선택 : "))

#어떤코인을 구매했는가
if(num==1):
    print("일론머스크의 한마디로 가격이 40% 올라갔습니다.")
    print("현재 잔고 : ",doge)
if(num==2):
    print("비트코인의 하락장에 갇혀 30% 손실이 일어났습니다.")
    print("현재 잔고 : ",bitcoin)
 #수면매수 선택 시
if(num==3):
    # 사용자 선택 및 랜덤
    print("어떤 코인을 구매하실래요?? 1.사용자선택 2.랜덤 ")
    su1 = int(input(">> "))
    #사용자 선택을 골랐을 때
    if(su1 == 1):
        print(su)
        su2 = int(input(">>>>  "))
        print(su[su2],"을(를) 구매합니다. 건승을 빕니다.")
    # 랜덤을 골랐을 때
    if(su1 == 2):
        import random
        print(random.choice(su),"코인이(가) 랜덤으로 구매되었습니다. 건승을 빕니다.")
   
    num1 = int(input("예상 손해 퍼센트[1] : "))
    num2 = int(input("예상 손해 퍼센트[2] : "))
    print("업비트에서",sonsil(num1,num2),"%의 손실알림이 도착했습니다.")
    print("눈물을 머금고 잠에듭니다.")
    
    # 예상손해 퍼센트 1 + 2
    num3 = money * (1 - (num1+num2)/ 100)

    print("잔고 :", int(num3))
print("게임을 종료합니다.")



