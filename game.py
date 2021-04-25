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


print("1.패닉셀한다. 2.추가매수한다. 3.한숨쉬고 업비트를 끈다. ")
num = int(input("선택 : "))

if(num==1):
    print("패닉셀을 하자, 다시 반등이 왔습니다 ㅋㅋ.")
if(num==2):
    print("추가매수하자, 다시 떨어집니다 ㅋㅋ.")
if(num==3):
    num1 = int(input("예상 손실 : "))
    num2 = int(input("예상 손실 : "))
    print("업비트에서",sonsil(num1, num2),"%의 손실알림이 도착했습니다. 어떻게 하시겠습니까?")3
