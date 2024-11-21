import time

# 자리 상태 및 door 파일 시뮬레이션
seats = {
    "1조": {"limit": 6, "members": []},
    "2조": {"limit": 7, "members": []},
    "3조": {"limit": 7, "members": []},
    "4조": {"limit": 8, "members": []},
    "5조": {"limit": 9, "members": []},
    "6조": {"limit": 8, "members": []},
    "computer_seats": {"limit": 1, "members": []},  # 컴퓨터 자리는 한 명만 가능
}

# door 파일 시뮬레이션
door = {"students": [("홍길동", "2023001"), ("김철수", "2023002"), ("이영희", "2023003")]} #


# 자리 선택 함수
def choose_seat():
    print("자리 배치 안내:")
    print('1조(6명) | 4조(8명) \n2조(7명) | 5조(9명) \n3조(7명) | 6조(8명)')
    print("4조 바로 앞에 컴퓨터 자리가 있습니다.\n")

    while True:
        print("\n현재 자리 상황:")
        for group, info in seats.items():
            print(f"{group}: {len(info['members'])}/{info['limit']}")

        choice = input("\n모둠 자리(1조, 2조, 3조, 4조, 5조, 6조) 또는 컴퓨터 자리를 선택하세요: ")

        if choice in seats:
            if len(seats[choice]["members"]) < seats[choice]["limit"]:
                student_name = input("학생 이름을 입력하세요: ")
                student_id = input("학생 학번을 입력하세요: ")

                # door 파일에 학생이 있는지 확인
                if (student_name, student_id) in door["students"]:
                    seats[choice]["members"].append((student_name, student_id))
                    print(f"{choice} TV가 켜집니다! 현재 인원: {len(seats[choice]['members'])}/{seats[choice]['limit']}")
                else:
                    print("학생 정보가 등록되어 있지 않습니다. door 파일을 확인하세요.")
            else:
                print(f"{choice} 자리가 꽉 찼습니다. 다른 자리를 선택해 주세요.")
        elif choice == "컴퓨터자리":
            if len(seats["컴퓨터자리"]["members"]) < seats["컴퓨터자리"]["limit"]:
                student_name = input("학생 이름을 입력하세요: ")
                student_id = input("학생 학번을 입력하세요: ")

                if (student_name, student_id) in door["students"]:
                    seats["컴퓨터자리"]["members"].append((student_name, student_id))
                    print("TV와 컴퓨터 전원이 켜집니다!")
                else:
                    print("학생 정보가 등록되어 있지 않습니다. door 파일을 확인하세요.")
            else:
                print("컴퓨터 자리가 이미 사용 중입니다.")
        else:
            print("잘못된 선택입니다. 다시 선택해 주세요.")
            continue

        # 사용자에게 계속할지 물어보기
        cont = input("\n다른 자리를 선택하시겠습니까? (y/n): ")
        if cont.lower() != 'y':
            break


# 시간에 따른 TV 끄기 (예: 5초 후 TV 자동 종료)
def auto_off():
    print("\n5초 후 TV 전원이 자동으로 꺼집니다.")
    time.sleep(5)
    print("TV 전원이 꺼졌습니다.")


# 메인 실행
choose_seat()
auto_off()
