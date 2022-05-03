#구구단 만들기
number = 1

while number < 10: # number <=9 도 가능
    print("2*%d = %d" % (number , 2*number)) #number가 1~9까지 반복
    number = number+1
    
#커피 프로그램

#커피 수량
coffee = 5

#
while coffee > 0 :
    money = int(input("금액을 입력해주세요 : "))
    
    if money == 300:
        print("coffee")
        
        #커피를 하나씩 줄인다
        coffee = coffee -1
        
    elif money < 300:
        print("%d원을 반환합니다" % money) 
        
        #커피 줄이면 안됨.

    
    else:
        print("coffee")
        
        #커피를 하나씩 줄인다
        coffee = coffee - 1 
        
        #300원 이상 지불했기 때문에 지불한돈 - 300 해서 거슬러 주기
        print("%d원을 반환합니다" %(money - 300))

#while문 종료시 출력        
print("커피가 모두 소진되었으니 관리자에게 문의해주세요") 