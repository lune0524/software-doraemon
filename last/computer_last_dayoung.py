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
def auto_tv_off(seat):
    print(f"{seat}의 TV가 5초 뒤에 꺼질 예정입니다...")
    time.sleep(5)  # 테스트용으로 5초 설정. 실제 사용 시 더 긴 시간으로 조정 가능.
    if key_seats[seat] == 0:  # 사람이 없을 경우에만 꺼짐
        tv_status[seat] = False
        print(f"{seat}의 TV가 꺼졌습니다.\n")

# 자리 선택 함수
def choose_seat():
    print("\n자리 배치 안내:")
    print('1조(6명) | 4조(8명)\n2조(7명) | 5조(9명)\n3조(7명) | 6조(8명)')
    print("\n4조 바로 앞에 컴퓨터 자리가 있습니다.\n")

    while True:
        # 사용자 선택
        choice = input("모둠 자리(1조, 2조, 3조, 4조, 5조, 6조) 또는 '나가기'를 선택하세요 (종료하려면 '종료' 입력): ")

        if choice == "종료":
            print("프로그램을 종료합니다.")
            break
        elif choice == "나가기":
            current_seat = next((seat for seat, count in key_seats.items() if count > 0), None)
            if current_seat:
                key_seats[current_seat] -= 1
                print(f"{current_seat}에서 나왔습니다. 현재 인원: {key_seats[current_seat]}/{seats[current_seat]}")
                if key_seats[current_seat] == 0:  # 나간 후 사람이 없으면 타이머 실행
                    threading.Thread(target=auto_tv_off, args=(current_seat,)).start()
            else:
                print("현재 앉아 있는 자리가 없습니다.")
        elif choice in seats:
            if key_seats[choice] < seats[choice]:
                key_seats[choice] += 1
                if not tv_status[choice]:
                    tv_status[choice] = True
                    print(f"{choice} TV가 켜졌습니다.")
                print(f"{choice}에 앉았습니다. 현재 인원: {key_seats[choice]}/{seats[choice]}")
                break
            else:
                print(f"{choice}는 이미 자리가 가득 찼습니다. 다른 조를 선택해 주세요.\n")
        elif choice in ["컴퓨터자리", "컴퓨터", "컴퓨터 자리"]:
            print("TV와 컴퓨터 전원이 켜집니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 선택해 주세요.\n")

# 함수 호출

if __name__ == "__main__":
    choose_seat()