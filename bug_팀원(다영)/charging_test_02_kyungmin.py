import time
from computer_test_02_dayoung import choose_seat

def charging():
    print("\n전자기기를 올려주시겠습니까? (Y/N)")
    answer = input().upper()
    
    if answer == "Y":
        print("충전을 시작합니다.")
        battery = 0  # 초기 배터리 잔량임
        while battery < 100:
            time.sleep(1)  # 1초에 10분씩
            battery += 10
            if battery > 100:
                battery = 100  # 배터리 최대치는 100%
            print("충전 중... 현재 배터리: ", battery,"%")
        print("충전이 완료되었습니다!")
    elif answer == "N":
        print("충전을 하지 않습니다.")
    else:
        print("잘못된 입력입니다. 충전 종료합니다.")

# 메인 실행 로직
while True:
    selected_seat = choose_seat()
    charging()
    if selected_seat is None:  # 종료 조건
        break
    