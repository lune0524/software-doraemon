student = ['장영곤', '이경민', '우새솔', '윤다영', '양희성', '박소현'] #학생 이름 리스트

professors = ["송주환", "김영수", "이근호","고선우","권수태"] #교수님 이름 리스트


    # Step 1: 이름과 학번 입력

def check_professors():
    
    P_name = input("이름을 입력하세요: ")
    
    if P_name in professors:
        print(f"{P_name} 교수님, 환영합니다! 문이 열립니다.") #교수 검사
check_professors()


def check_student():  
    S_name = input("이름을 입력하세요: ")

    # Step 2: 이름이 리스트에 해당하는지 확인 
    if S_name in student:  #리스트 안에 있는 이름이 아니면 인공지능학과로 간주 하고 다음으로 학번 입력
        print(f"{S_name}님, 인공지능학과 확인 완료! 문이 열립니다.") # 학생 검사
        
        S_number = int(input("학번을 입력 하세요"))
    
        # Step 3: 출입 여부 질문
    while True:    
        entry = input("들어오시겠습니까? (Y/N): ").strip().upper()
        # Step 4: 출입 여부 확인 및 메시지 출력
        if entry == "Y":
            print("출석이 인정되었습니다. 오늘도 좋은 하루 보내세요!")
            break
        elif entry == "N":
            print("출석이 인정되지 않았습니다. 다음에 다시 방문해주세요.")
            break
        else:
            print("잘못된 입력입니다. Y 또는 N 으로 입력해주세요.")
    else:
        print(f"{S_name}님, 학번 확인 실패! 문이 열리지 않습니다.")
        print("출입 권한이 없습니다.")
# 함수 실행
check_student()
