import time

# 교수님 리스트
def access_control():
    professors = ["송주환", "김영수", "이근호", "고선우", "권수태","민정익"]
    students = {
        "장영곤": "202411246",
        "이경민": "202392007",
        "우새솔": "202410798",
        "윤다영": "202411594",
        "양희성": "202411594",
        "박소현": "202412153",
        "김용진": "202411375"
    }

    while True:
        user_type = input("교수님이십니까 학생이십니까? (교수/학생): ").strip()

        if user_type == "교수":
            professors_name = input("이름을 입력하세요: ").strip()
            if professors_name in professors:
                print(f"{professors_name} 교수님, 환영합니다! 문이 열립니다.")
                # 교수님 입/퇴실 여부 확인
                while True:
                    entry = input("들어오시겠습니까? (Y/N/돌아가기/종료): ").strip().upper()
                    if entry == "Y":
                        print("출석이 인정되었습니다. 오늘도 좋은 하루 보내세요!")
                        return professors_name, "Y"
                    elif entry == "N":
                        print("출석이 인정되지 않았습니다. 다음에 다시 방문해주세요.")
                        return professors_name, "N"
                    elif entry == "돌아가기":
                        # 교수/학생 단계로 돌아가기
                        return None, "돌아가기"
                    elif entry == "종료":
                        print("시스템을 종료합니다.")
                        return None, "종료"
                    else:
                        print("잘못된 입력입니다. 'Y', 'N', '돌아가기', '종료' 중 하나를 입력해주세요.")

            else:
                print(f"{professors_name}님은 권한이 없습니다. 출입이 제한됩니다.")
                # 권한 없는 경우 다시 교수/학생 선택 단계로
                continue

        elif user_type == "학생":
            student_input = input("이름과 학번을 입력하세요 (예: 홍길동 202411001): ").strip()

            try:
                student_name, student_number = student_input.split()
            except ValueError:
                print("잘못된 입력 형식입니다. 이름과 학번을 띄어쓰기로 구분하여 입력해주세요.")
                continue  # 다시 교수/학생 선택으로

            if student_name in students and students[student_name] == student_number:
                print(f"{student_name}님, 인공지능학과 확인 완료! 문이 열립니다.")
                while True:
                    entry = input("들어오시겠습니까? (Y/N/돌아가기/종료): ").strip().upper()
                    if entry == "Y":
                        print("출석이 인정되었습니다. 오늘도 좋은 하루 보내세요!")
                        return student_name, "Y"
                    elif entry == "N":
                        print("출석이 인정되지 않았습니다. 다음에 다시 방문해주세요.")
                        return student_name, "N"
                    elif entry == "돌아가기":
                        return None, "돌아가기"
                    elif entry == "종료":
                        print("시스템을 종료합니다.")
                        return None, "종료"
                    else:
                        print("잘못된 입력입니다. 'Y', 'N', '돌아가기', '종료' 중 하나를 입력해주세요.")
            else:
                print(f"{student_name}님, 학번 확인 실패! 문이 열리지 않습니다.")
                print("시스템에 정보가 없습니다. 관리자를 통해 추가해주세요.")
                # 정보 없는 경우 계속해서 교수/학생 선택 단계로
                continue

        else:
            print("잘못된 입력입니다. '교수', '학생', '종료' 중에서 선택해주세요.")
