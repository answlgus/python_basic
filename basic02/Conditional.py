#if
#a가 5일때 a = 5 이면 True 출력
a = 5

if a == 5:
    print("True")
print("False") 

#비교연산
#a == b  같다
#a != b  다르다
#a > b | a < b  크다 작다
#a >= b | a <= b  크거나 작다 , 작거나 같다 

#논리연산
#a and b #A 와 B 둘 다 만족
#a or b # A 또는 B 중 하나 이상 만족 
#not a # a가 아님

#자판기 만들기

#가격이 300원, 300원이 들어오면 cofee를 준다
money = 300
if money == 300:
    print("coffee")

#돈이 200원만 있는 경우
if money < 300:
    print("%d원을 돌려줍니다." % money)

#돈이 1000원 있는 경우
if money > 300:
    print("coffee") 
    print("%d원을 돌려줍니다." % (money - 300)) 


#else , elif 문 적용해보기

money = 1000
if money == 300:
    print("coffee")
elif money < 300:
    print("%d원을 돌려줍니다." % money)
else:
    print("coffee")
    print("%d원을 돌려줍니다." % (money-300))
    
#nested 구조
money = 500
if money == 300:
    print("coffee")
else:
    if money < 300:
        print("%d원을 돌려줍니다." % money)
    else:
        print("coffee")
        print("%d원을 돌려줍니다." % (money - 300))