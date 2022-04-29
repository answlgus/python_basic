#원소 1 , 2 를 가지는 튜플 생성

t = (1, 2)
print(t)

t1 = ()
print(t1 , type(t1))

t2 = ('a' , 'b' , ('a','b'))
print(t2)

print(t2[:2])

#indexing 
t = (1, 2)
print(t[0])

print(t[-1])

#튜플 원소변경
#t[0] = 3 
#print(t)

#더하기
t = (1,2)
t2 = (3,4)
print(t+t2)

#곱하기
print(t2*3)

#len()함수
t = (1,2)
print(len(t*3))