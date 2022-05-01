#dict 생성
D = {} 

print(type(D))

#테이블 만들기
D = {"Jhon" : '0011' , "Maria" : '1234'}
print(D , type(D))

#dict indexing
print(D["Jhon"]) #key를 통해 Value에 접근

#원소 추가
#key가 'a' value가 3인 원소 추가
D['a'] = 3
print(D)

D['a'] = 4
print(D)

D2 = {'a' : 1 , 'a' : 2 , 'b' : 3}
print(D2)

#사전 관련 함수
D = {'name'  : 'kim' , 'phone' : '01011112222' , 'birth' : '1111'}

#keys
print(D.keys())

#valuse
print(D.values())

#items
print(D.items())

#get
D = {'name'  : 'kim' , 'phone' : '01011112222' , 'birth' : '1111'}

print(D.get('phone'))
print(D.get('address' , 'Seoul'))

#in

print('phone' in D)
print('major' in D)

print('1111' in D.values())

