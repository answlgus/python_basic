#집합 (set)
# 1,2,3을 원소로 가지는 집합 생성
s = {1,2,3}
print(s)
#print(s[1])

print(s, type(s))

# 집합의 연산
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

#s1과 s2의 교집합
print(s1 & s2)

print(s1.intersection(s2))

# 합집합
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

print(s1|s2)

print(s1.union(s2))

#차집합
s1 = {1,2,3,4,5}
s2 = {3,4,5,6,7}

print(s1-s2)

#집합 원소의 uniqueness를 활용하는 경우(서로 다른 숫자가 몇 개 있는지)
L = [1,2,3,3,4,1,2,34,5,6,1,2]
print(set(L))

#7가지 라는 결과를 도출하고자 할 경우
print(len(set(L)))

#집합관련 함수
#add
s = set()
s.add(3)
print(s)

#update
s = {1,2,3}
s.update({4,5})
print(s)

#remove
s.remove(3)
print(s)