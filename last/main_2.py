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

    # 현재 내부에 있는 사람들을 추적할 리스트
    inside_people = []

    print("\n--- 출입 권한 확인 ---")
    while True:
        name, entry = access_control()

        if entry == "Y":  # 입실
            if name not in inside_people:
                inside_people.append(name)
                state["current_people"] = len(inside_people) - 1
                state, _ = light("in", state)
                print(f"현재 인원: {state['current_people']}명 ({inside_people})")
            else:
                print(f"{name}님은 이미 입실 중입니다.")

        elif entry == "N":  # 퇴실
            if name in inside_people:
                inside_people.remove(name)
                state["current_people"] = len(inside_people)
                state, _ = light("out", state)
                print(f"현재 인원: {state['current_people']}명 ({inside_people})")
            else:
                print(f"{name}님은 현재 실내에 없습니다. 퇴실할 수 없습니다.")

        elif entry == "돌아가기":
            # 입실도 퇴실도 하지 않고 돌아가기
            print("아무 작업도 하지 않고 이전 단계로 돌아갑니다.")
            continue

        elif entry == "종료":
            print("시스템을 종료합니다. 안녕히 가세요!")
            break

        else:
            print("잘못된 입력입니다. '입실(Y)', '퇴실(N)', '재입력', '돌아가기', '종료' 중 하나를 입력하세요.")

    # 온도 확인 및 냄새 설정
    temperature()
    a = smell_set()
    if a == 'Y':
        air_stove()

    # 현재 남아있는 사람 수 기준으로 자리 선택 및 충전
    people = len(inside_people)
    for i in range(people):
        choose_seat()
        charging()

if __name__ == "__main__":
    main()
