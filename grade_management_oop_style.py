class Student:
    def __init__(self, stn, name, eng, c, py):
        self.stn = stn
        self.name = name
        self.eng = eng
        self.c = c
        self.py = py
        self.total, self.avg = self.cal_sumavg(eng, c, py)
        self.grade = self.cal_grade(self.avg)
        self.rank = None
    
    def cal_sumavg(self, a, b, c):
        total = a + b + c
        avg = total / 3
        return total, avg
    
    def cal_grade(self, avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        stn = int(input("학번: "))
        name = input("이름: ")
        eng = int(input("영어 점수: "))
        c = int(input("C언어 점수: "))
        py = int(input("파이썬 점수: "))
        student = Student(stn, name, eng, c, py)
        self.students.append(student)

    def del_student(self, student_id):
        for student in self.students:
            if student.stn == student_id:
                self.students.remove(student)
                print(f"학생 {student.name}의 정보 삭제")
                return
        print("해당 학번을 가진 학생을 찾을 수 없습니다.")

    def show_all_students(self):
        if not self.students:
            print("등록된 학생 정보가 없습니다.")
            return
        print("\t\t\t성적관리 프로그램")
        print("===================================================================")
        print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
        print("===================================================================")
        for student in self.students:
            print((f"{student.stn}\t{student.name}\t{student.eng}\t{student.c}\t{student.py}\t{student.total}\t{student.avg:.2f}\t{student.grade}\t{student.rank}"))

    def count_80_up(self):
        count = 0
        for student in self.students:
            if student.avg >= 80:
                count += 1
        return count

    def sort_students(self):
        self.students.sort(key=lambda x: x.total, reverse=True)
        for i, student in enumerate(self.students, start=1):
            student.rank = i

    def search_student(self, search_key):
        found = False
        for student in self.students:
            if str(student.stn) == search_key or student.name == search_key:
                print("학번\t이름\t영어\tC-언어\t파이썬\t총점\t평균\t학점\t등수")
                print("===================================================================")
                print(f"{student.stn}\t{student.name}\t{student.eng}\t{student.c}\t{student.py}\t{student.total}\t{student.avg:.2f}\t{student.grade}\t{student.rank}")
                found = True
        if not found:
            print(f"학번 또는 이름 '{search_key}'에 해당하는 학생 정보가 없습니다.")


student_manager = StudentManager()

for i in range(5):
    student_manager.add_student()

student_manager.sort_students()
student_manager.show_all_students()
print("80점 이상인 학생 수: ", student_manager.count_80_up())

while True:
    print("\n1. 학생 정보 추가")
    print("2. 학생 정보 삭제")
    print("3. 개인 정보 출력")
    print("4. 전체 정보 출력")
    print("다른 숫자: 종료")
    choice = int(input("원하는 작업을 선택하세요: "))

    if choice == 1:
        student_manager.add_student()
    elif choice == 2:
        student_id = int(input("삭제할 학생의 학번을 입력하세요: "))
        student_manager.del_student(student_id)
    elif choice == 3:
        search_key = input("학번 또는 이름을 입력하세요: ")
        student_manager.search_student(search_key)
    elif choice == 4:
        student_manager.sort_students()
        student_manager.show_all_students()
        print("80점 이상인 학생 수: ", student_manager.count_80_up())
    else:
        print("프로그램을 종료합니다.")
        break
