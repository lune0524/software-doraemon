import time
from door_last_heesung import access_control
from light_last_saesol import light
from window_last_sohyun import smell_set
from air_last_younggon import temperature, air_stove
from computer_last_dayoung import choose_seat
from charging_last_kyungmin import charging

def main():
    # 조명 상태 초기화
    state = {
        "light_on": False,
        "current_people": 0,
        "last_activity_time": time.time()
    }
    
    print("\n--- 출입 권한 확인 ---")
    while True:
        # 출입 권한 확인 및 entry 값 받기
        entry = access_control()  # 교수님 또는 학생 입장 여부 처리

        if entry == "Y":  # 입실
            state, _ = light("in", state)  # 입실: current_people +1 및 조명 상태 확인
        elif entry == "N":  # 퇴실
            state, _ = light("out", state)  # 퇴실: current_people -1 및 조명 상태 확인
        elif entry == "종료":
            print("시스템을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 입력입니다. '입실(Y)', '퇴실(N)', '종료' 중 하나를 입력하세요.")
    
    # 온도 확인 및 냄새 설정
    temperature()
    a = smell_set()
    if a == 'Y':
        air_stove()

    # 현재 사람 수를 기준으로 자리 선택 및 충전
    people = state["current_people"]
    for i in range(people):
        choose_seat()
        charging()


if __name__ == "__main__":
    main()