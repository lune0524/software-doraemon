import time

#@@학생 리스트 관리는 불이랑 거리가 너무 멀어지는것 같아서 아예 삭제
def light(action, state, timeout=14400):  #입실,퇴실,자동소등,자동소등 기본값
#@@라이트로 변경완료
    light_on = state["light_on"]
    current_people = state["current_people"]
    last_activity_time = state["last_activity_time"]
#@@글로벌삭제 
    if action == "in":
        current_people += 1
        last_activity_time = time.time()
        if not light_on:  # 불이 꺼져 있으면 켬
            light_on = True
            print("불이 켜졌습니다. 환영합니다")
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
#@@check는 마지막 사람 시간 체크해주는거라 변경 불가
    else:
        print("잘못된 동작입니다. 'in', 'out', 'check' 중 하나를 선택하세요.")
    # 현재 상태 출력
    return {
        "light_on": light_on,
        "current_people": current_people,
        "last_activity_time": last_activity_time,
    }

state = {
    "light_on": False,
    "current_people": 0,
    "last_activity_time": time.time(),
}
#@@ out: 특정 학생의 퇴실.
#@@ check: 과방 전체의 상태 점검 후, 자동 소등.
#궁금한거 있으면 물어보슈