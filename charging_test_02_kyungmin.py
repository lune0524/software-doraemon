import time
import computer_test_02_dayoung

def wireless_charging():
    print("\n전자기기를 올려주시겠습니까? (Y/N)")
    answer = input().strip().upper()
    
    if answer == "Y":
        print("충전을 시작합니다.")
        battery_level = 0  # 초기 배터리 잔량
        while battery_level < 100:
            time.sleep(1)  # 1초를 10분의 시뮬레이션으로 간주
            battery_level += 10
            if battery_level > 100:
                battery_level = 100  # 배터리 최대치는 100%
            print("충전 중... 현재 배터리: ", battery_level,"%")
        print("충전이 완료되었습니다!")
    elif answer == "NO":
        print("충전을 하지 않습니다.")
    else:
        print("잘못된 입력입니다. 충전 프로세스를 종료합니다.")

# 메인 실행 로직
while True:
    selected_seat = choose_seat()
    if selected_seat is None:  # 종료 조건
        break
    wireless_charging()