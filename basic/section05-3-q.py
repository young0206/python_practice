# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for a1 in q1.keys():
    if a1 == '가을':
        print(q1[a1])

print()

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

for a2 in q2.values():
    if a2 == '사과':
        print("사과가 있습니다.")
        break
else:
    print("사과가 없습니다.")

print()

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

a3 = 61

if a3 >= 81 and a3 <= 100:
    print("A학점")
elif a3 >= 61:
    print("B학점")
elif a3 >= 41:
    print("C학점")
elif a3 >= 21:
    print("D학점")
elif a3 >= 0 and a3 <= 20:
    print("E학점")

print()

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18

a = 12
b = 6
c = 18

if (a > b and a > c):
    print(a)
elif (b > a and b > c):
    print(b)
else:
    print(c)

print()

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)

a = "891022-2473827"

if a[7] == "2" or a[7] == "4":
    print("여자")
elif a[7] == "1" or a[7] == "3":
    print("남자")
else:
    print("외계인")

print()

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "정", "을", "병"]

for a3 in q3:
    if a3 == "정":
        continue
    print(a3)

print()

q5 = [x for x in q3 if x != '정']
print(q5)

print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.

for i in range(1, 100, 2):
    print(i, end=' ')

print()
print()

q6 = [x for x in range(1, 101) if x % 2 != 0]
print(q6, end=' ')

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for a4 in q4:
    if len(a4) >= 5:
        print(a4, end=", ")

print()
print()

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for a5 in q5:
    if a5.islower():
        print(a5, end=", ")

print()
print()

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for a6 in q6:
    if a6.islower():
        print(a6.upper(), end=", ")
    else:
        print(a6.lower(), end=", ")

print()
print()

# 일반적인 방법
numbers = []

for n in range(1, 101):
    numbers.append(n)
print(numbers)


# 리스트 컨프리헨션
numbers2 = [x for x in range(1, 101)]
print(numbers2)