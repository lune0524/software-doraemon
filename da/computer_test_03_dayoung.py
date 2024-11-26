import time
import threading

# 자리 배치
seats = {
    "1조": 6,
    "2조": 7,
    "3조": 7,
    "4조": 8,
    "5조": 9,
    "6조": 8,
}

# 조별 인원
key_seats = {key: 0 for key in seats}

# TV 상태 저장
tv_status = {key: False for key in seats}

# TV 종료 타이머
def auto_turn_off(seat):
    print(seat,"의 TV가 5초 뒤에 꺼질 예정입니다...")
    time.sleep(5)  # 테스트용으로 5초 설정. 실제 사용 시 더 긴 시간으로 조정 가능.
    if key_seats[seat] == 0:  # 사람이 없을 경우에만 꺼짐
        tv_status[seat] = False
        print(seat,"의 TV가 꺼졌습니다.\n")

# 자리 선택 함수
def choose_seat():
    while True:
        print("자리 배치 안내:")
        print('Group 1(6명) | Group 4(8명) \nGroup 2(7명) | Group 5(9명) \nGroup 3(7명) | Group 6(8명)')
        print()

        # 컴퓨터 자리
        print("4조 바로 앞에 컴퓨터 자리가 있습니다.\n")

        # 사용자 선택
        choice = input("모둠 자리(Group 1, Group 2, Group 3, Group 4, Group 5, Group 6) 또는 컴퓨터 자리를 선택하세요 (종료하려면 '종료' 입력): ")

        if choice == "종료":
            print("프로그램을 종료합니다.")
            break
        elif choice in seats:
            if key_seats[choice] < seats[choice]:
                key_seats[choice] += 1
                tv_status[choice] = True
                print(f"{choice} TV가 켜졌습니다. 현재 인원: {key_seats[choice]}/{seats[choice]}")
            else:
                print(f"{choice}는 이미 자리가 가득 찼습니다. 다른 조를 선택해 주세요.\n")

            # 자리 떠날 때 처리
            leave = input(f"{choice} 자리를 떠나시겠습니까? (예/아니오): ").strip()
            if leave == "예":
                key_seats[choice] -= 1
                print(f"{choice} TV 상태: 인원 {key_seats[choice]}")
                if key_seats[choice] == 0:  # 사람이 없으면 타이머 실행
                    threading.Thread(target=auto_turn_off, args=(choice,)).start()
        elif choice in ["컴퓨터자리", "컴퓨터", "컴퓨터 자리"]:
            print("TV와 컴퓨터 전원이 켜집니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해 주세요.\n")

# 함수 호출
choose_seat()
