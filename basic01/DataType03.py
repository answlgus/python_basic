#문자열 Formatting(format을 지정) 3가지
#1. print format
print("%s는 %d개 있다." % ("사과" , 4))

#2. str.format
print("{}은/는 {}개 있다" .format ("수박" , 1))

#3. f-string
fruit = "딸기" 
count = 5

print(f"{fruit}는 {count}개 있다.")

#예제> apple = "사과" count = 4
#1. print format
print("%s는 %d개 있다." % ("사과" , 4))

#2. str.format
print("{}는 {}개 있다".format("사과" , 4))

#3. f-string
apple ="사과"
count = 4
print(f"{apple}는 {count}개 있다.")

#문자열 관련 함수 
#대소문자 바꾸기 upper(), lower()
s = "hi"
print(s.upper())

s1 ="HI"
print(s.lower())

#문자 공백 지우기 strip()
#마지막 문자 이후의 공백만 삭제
t = "h  i      "
print(t.strip())

#join() - > 문자열 삽입(문자 간 사이에)
print(",".join("abcd"))

#split() -> 문자열 나누기(공백을 기준)
s = "Life is too short."
print(s.split())

#()에 문자 입력시 해당 문자(token)를 기준으로 나눔
print(s.split("."))

#replace() - > 문자열 바꾸기
print(s.replace("Life" , "This pencil"))

#cf) 빈칸 모두 삭제
print(s.replace(" " , ""))

