import time
import random

def battery_level():
    # 0~90 사이의 랜덤 값 생성
    level = random.randint(0, 90)
    return level

def charging():
    while True:  # 무한 반복하여 올바른 입력을 받을 때까지 계속 묻기
        level = battery_level()
        print(f"현재 배터리 잔량은 {level}%입니다.")
        answer = input("\n전자기기를 올려주시겠습니까? (Y/N):").strip().upper()
        if answer == "Y":
            # 초기 배터리 잔량 생성
            
            
            print("충전을 시작합니다.")
            while level < 100:
                time.sleep(1)  # 1초를 10분의 시뮬레이션으로 간주
                level += 10
                if level > 100:
                    level = 100  # 배터리 최대치는 100%
                print(f"충전 중... 현재 배터리: {level} %")
            print("충전이 완료되었습니다!")
            break  # 충전이 끝났으므로 반복 종료
        elif answer == "N":
            print("충전을 하지 않습니다.")
            break  # 충전하지 않겠다고 했으므로 반복 종료
        else:
            print("잘못된 입력입니다. Y 또는 N을 입력해주세요.")  # 잘못된 입력에 대한 안내 메시지

# 메인 실행 로직
if __name__ == "__main__":
    charging()
