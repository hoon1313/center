#함수적용
def sonsil(a,b):   
    a = num1
    b = num2
    result = int(a)+int(b)
    return result   

#이름 및 정보 입력 (dic)
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
doge = int(money*1.4)
bitcoin = int(money*0.7)

print("충전된 돈",money,"원으로 어떤코인을 구매할까요?")
print("1.도지코인. 2.비트코인 3.수면매수 ")
num = int(input("선택 : "))

if(num==1):
    print("일론머스크의 트윗질로 가격이 올라갑니다")
    print("현재 잔고 : ",doge)
if(num==2):
    print("비트코인의 하락장에 갇혔습니다.")
    print("현재 잔고 : ",bitcoin)
if(num==3):
    num1 = int(input("예상 이득 퍼센트 : "))
    num2 = int(input("예상 손해 퍼센트 : "))
    print("업비트에서",sonsil(num1,num2),"%의 손실알림이 도착했습니다.")
    
    num3 = int(money * ((1.0 - (num1+num2)) / 100.0))

    print("현재 잔고 :", num3)

