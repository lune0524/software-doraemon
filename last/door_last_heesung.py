import time

# 교수님 리스트
professors = ["송주환", "김영수", "이근호", "고선우", "권수태"]

# 학생 이름-학번 딕셔너리
students = {
    "장영곤": "202411246",
    "이경민": "202392007",
    "우새솔": "202410798",
    "윤다영": "202411594",
    "양희성": "202411594",
    "박소현": "202412153",
    "김용진": "202411375"
}

def access_control():
    user_type = input("교수님이십니까 학생이십니까? (교수/학생): ").strip()
    
    if user_type == "교수":
        professors_name = input("이름을 입력하세요: ").strip()
        if professors_name in professors:
            print(f"{professors_name} 교수님, 환영합니다! 문이 열립니다.")
            while True:
                entry = input("들어오시겠습니까? (Y/N): ").strip().upper()
                if entry in ("Y", "N"):
                    return entry
                print("잘못된 입력입니다. Y 또는 N 으로 입력해주세요.")
        else:
            print(f"{professors_name}님은 권한이 없습니다. 출입이 제한됩니다.")
            return None

    elif user_type == "학생":
        student_input = input("이름과 학번을 입력하세요 (예: 홍길동 202411001): ").strip()
        try:
            student_name, student_number = student_input.split()
        except ValueError:
            print("잘못된 입력 형식입니다. 이름과 학번을 띄어쓰기로 구분하여 입력해주세요.")
            return None

        if student_name in students and students[student_name] == student_number:
            print(f"{student_name}님, 인공지능학과 확인 완료! 문이 열립니다.")
            while True:
                entry = input("들어오시겠습니까? (Y/N): ").strip().upper()
                if entry in ("Y", "N"):
                    return entry
                print("잘못된 입력입니다. Y 또는 N 으로 입력해주세요.")
        else:
            print(f"{student_name}님, 학번 확인 실패! 문이 열리지 않습니다.")
            return None

    else:
        print("잘못된 입력입니다. '교수' 또는 '학생'으로 입력해주세요.")
        return None


# 함수 실행
if __name__ == "__main__":
 access_control()

