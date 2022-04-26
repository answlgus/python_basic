L = [1,2,3]

#비어있는 리스트 만들기
L1 = []
print(type(L1))

L2 = list()
print(type(L2))

#리스트에는 다양한 타입의 원소를 담을 수 있다.(리스트도 담을 수 있음)\
L3 = [1, "Hi" , 3.14 , [1,2,3]]
print(L3)

#2차원 리스트
L4 = [[1,2] ,
      [3,4]]

print(L4)

#Index
L = [1,2,3,4,5]

#L의 첫 번째 원소에 접근 (첫 번째 == 0번째)
print(L[0])

#L의 다섯번째 원소
print(L[4])

#L의 마지막 원소
print(L[-1]) 

#인덱싱을 활용하여 연산해보기
#L의 첫번째, 두번째 원서를 더해보기
print(L[0] + L[1])

#len()을 인덱스에 사용해보기
print(len(L)) #5

#print(L[len(L)]) -> 이렇게 하면 오류

print(L[len(L)-1])

#예
print(L[-3])
print(L[len(L)-3])

#리스트 안에 리스트가 있는 경우 L2에서 2에 접근하기 위해 인덱싱 해보기
L2 = [1,[2,3],5]

#2는 두번째 원소의 첫번째 원소 (리스트 속의 리스트에 또 인덱싱 해주면 됨)
print(L2[1][0]) #== [2,3] [0]
print(L2[1])
