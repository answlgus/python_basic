#append
L = []

L.append(3)
L.append(2)
L.append(1)

print(L)

#sort(): 정렬
L.sort()
print(L)

#내림차순
L.sort(reverse=True) #descending order
print(L)

#reverse
L = [1,2,3,4,5,6]

#홀수번째 인덱스 추출
print(L[::2]) # 처음부터 끝까지 두칸씩 == L[0:len(L):2]

print(L[::-1])

#pop()
L.pop()
L.pop()
L.pop()
print(L)
