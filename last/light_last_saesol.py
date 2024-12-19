import time


def light(action, state, timeout=14400):  #입실,퇴실,자동소등,자동소등 기본값
    """

    in:입실처리,current_people에 +1
    out:퇴실처리,current_people에 -1
    check: in ,out에 저장된 시간이 timeout=14400 오버되면 자동 불 꺼짐
    "light_on":true,False로 현재 과방 불 상태 확인
    "current_people":현재 과방안에 있는 학생 수
    "last_activity_time":마지막 입/출입 시간 저장

    """
    light_on = state["light_on"]
    current_people = state["current_people"]
    last_activity_time = state["last_activity_time"]

    if action == "in":
        current_people += 1
        last_activity_time = time.time()
        if light_on==False:  # 불이 꺼져 있으면 켬
            light_on = True
            print("불이 켜졌습니다. 환영합니다")
            print(f"입실 완료.현재 인원: {current_people}")
        else:
            print(f"입실 완료.현재 인원: {current_people}")

    elif action == "out":
        if current_people > 0:
            current_people -= 1
            last_activity_time = time.time()
            print(f"퇴실완료. 현재 인원: {current_people}")
        else:
            print("과방에 아무도 없습니다.")
        
        # 인원이 0명이면 불 끔
        if current_people == 0 and light_on:
            light_on = False
            print("불이 꺼졌습니다.")


    elif action == "check":
        current_time = time.time()
        if light_on and current_time - last_activity_time > timeout:
            light_on = False
            print("오랜 시간 동안 출입이 없어 불이 자동으로 꺼졌습니다.")

    else:
        print("잘못된 동작입니다. 'in', 'out', 'check' 중 하나를 선택하세요.")
    # 현재 상태 출력
    return {
        "light_on": light_on,
        "current_people": current_people,
        "last_activity_time": last_activity_time,
    }, current_people


if __name__ == "__main__":
    state = {
        "light_on": False,
        "current_people": 0,
        "last_activity_time": time.time(),
    }

    # 테스트 실행
    print("=== 테스트 시작 ===")
    state = light("in", state)  # 입실
    time.sleep(2)               # 2초 대기
    state = light("in", state)  # 추가 입실
    state = light("out", state) # 퇴실
    time.sleep(2)               # 2초 대기
    state = light("check", state, timeout=1)  # 자동 소등 확인
    state = light("out", state) # 추가 퇴실
    state = light("check", state, timeout=1)  # 자동 소등 확인
    print("=== 테스트 종료 ===")