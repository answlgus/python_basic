#문자열
s = "Hello World"
s1 = "Life is short, You need Python"

#MultiLineString """
#오류 발생
#s2 = "Life is short,
#You need Python" 

s2 = """ To be great is
To be Misunderstood
-Ralph Waldo Emerson
"""

# '' 와 ""의 쓰임
s3 = "I'm a boy." #'까지 모두 출력
s4 = 'she said "Go home."' #""까지 모두 출력

#특수문자 표현  \n == new line(enter) 
# 특수문자 표현 \t == tab
print("Hello \n world")
print( "Hello \t world")

#String concatenation
a = "Hello"
b = "World"
print(a + b)

#공백 포함하고자 하는 경우(공백도 더해주기)
#공백 == String
print(a + '' + b)

#문자열의 * 사용
c = "Hello"
print(c*5)

#len -> 문자 길이 출력 함수
s3 = "Enjoy your life."
print(len(s3))

print(s)
print(s1)
print(s2)
print(s3)
print(s4)
