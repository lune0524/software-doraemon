import time

def generate_battery_level():
    # 현재 시간을 초 단위로 가져와 배터리 잔량을 계산 (0~90 사이 값 생성)
    current_time = int(time.time())  # 현재 시간을 초 단위로 가져옴
    battery_level = (current_time % 91)  # 0~90 사이의 값 생성
    return battery_level

def wireless_charging():
    print("\n전자기기를 올려주시겠습니까? (Y/N)")
    answer = input().strip().upper()
    
    if answer == "Y":
        # 초기 배터리 잔량 생성
        battery_level = generate_battery_level()
        print(f"현재 배터리 잔량은 {battery_level}%입니다.")
        
        print("충전을 시작합니다.")
        while battery_level < 100:
            time.sleep(1)  # 1초를 10분의 시뮬레이션으로 간주
            battery_level += 10
            if battery_level > 100:
                battery_level = 100  # 배터리 최대치는 100%
            print("충전 중... 현재 배터리: ", battery_level, "%")
        print("충전이 완료되었습니다!")
    elif answer == "N":
        print("충전을 하지 않습니다.")
    else:
        print("잘못된 입력입니다. 충전 프로세스를 종료합니다.")

# 메인 실행 로직
wireless_charging()
