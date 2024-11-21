def electronic_signboard():
    # 사용자 정보 입력
    name = input("이름을 입력하세요: ")
    student_id = input("학번을 입력하세요: ")

    # 학번 검사
    if student_id.startswith("AI"):  # AI로 시작하면 인공지능학과로 간주
        print(f"환영합니다, {name}님! 문이 열립니다.")
        
        # 출입 여부 질문
        entry_response = input("출입하시겠습니까? (YES/NO): ").strip().upper()
        if entry_response == "YES":
            print("출석이 인정되었습니다.")
        elif entry_response == "NO":
            print("출석이 인정되지 않았습니다.")
        else:
            print("잘못된 입력입니다. 출입 여부를 다시 확인하세요.")
    else:
        print("죄송합니다. 학번이 인공지능학과가 아닙니다. 문이 닫힙니다.")

# 함수 실행
electronic_signboard()

