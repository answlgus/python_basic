#Slicing
L = [1,2,3,4,5]

#L의 첫번째 부터 index2까지 자르기
print(L[0:2])

#L의 두번째 부터 index4 까지 자르기
print(L[1:4])

#시작 index를 생략하면 ,자동으로 index는 0이 된다(맨 처음부터)
#처음부터 index3까지 자르기
print(L[:3])

#끝 index 생략하면, 자동으로 index는 리스트의 길이가 된다
print(L[:-1]) 

#L[:-1] == L[:len(L) -1] == L[:5 -1] == L[:4] 

print(L[-2:])

#L[-2:] == L[len(L)-2 : len(L)] == L[5-2 : 5] == L[3:5]

#리스트 연산

#리스트 더하기
L= [1,2,3]
L2=[4,5]

print(L+L2)

#리스트 곱하기
print(L *3)

#리스트 수정하기
L[2] = 1
L2[0] = 7

print(L)
print(L2)

print(L+L2)

