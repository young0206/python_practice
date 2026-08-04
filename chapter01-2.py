# Chapter01-2
# 파이썬 심호
# 객체 지향 프로그래밍 (OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Student():
    """
    Student Class
    Author: Lee
    Date: 2026.08.04
    """

    # 클래스 변수
    student_count = 0

    def __init__(self, name, number, grade, details, email=None):
        # 인스턴스 변수
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1

    def __str__(self):
        return 'str {}'.format(self._name)

    def __repr__(self):
            return 'repr {}'.format(self._name)

    def detail_info(self):
        print('Current Id: {}'.format(self))
        print('Student Detail Info: {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1

# Self 의미
stud1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2': 44})
stud2 = Student('Change', 2, 3, {'gender': 'Female', 'score1': 85, 'score2': 74}, 'aaa@naver.com')

# ID 확인
print(id(stud1))
print(id(stud2))

print(stud1._name == stud2._name)
print(stud1 is stud2)

# dir & dict 확인
print(dir(stud1))
print(dir(stud2))

print()
print()

print(stud1.__dict__)
print(stud2.__dict__)

# Doctring
print(Student.__doc__)
print()

# 실행 
stud1.detail_info()
stud2.detail_info()
print()

# 에러
# Student.detail_info()

Student.detail_info(stud1)
Student.detail_info(stud2)
print()

# 비교
print(stud1.__class__, stud2.__class__)
print(id(stud1.__class__) == id(stud2.__class__))

print()

# 인스턴스 변수
# 직접 접근 (PEP 문법적으로 권장 x)

print(stud1._name, stud2._name)
print(stud1._email, stud2._email)

print()
print()

# 클래스 변수

# 접근
print(stud1.student_count)
print(stud2.student_count)
print(Student.student_count)

print()
print()

# 공유 확인
print(Student.__dict__)
print(stud1.__dict__)
print(stud2.__dict__)

print()
print()

# 인스턴스 네임 스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능 (인스턴스 검색 후 -> 상위 (클래스 변수, 부모 클래스 변수))

del stud2

print(stud1.student_count)
print(Student.student_count)