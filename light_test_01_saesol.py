import time

# 천장등 상태와 인원수를 관리하는 변수
light_on = False
current_people = 0
last_activity_time = time.time()

def ceiling_light(action, student_id=None, student_name=None, timeout=14400):
 
    global light_on, current_people, last_activity_time

    if action == "in":
        # 입실 처리예정
        pass

    elif action == "out":
        # 퇴실 처리예정
        pass

    elif action == "check":
        # 자동 소등 처리예정
        pass

    else:
        print("잘못된 동작입니다. 'in', 'out', 'check' 중 하나를 선택하세요.")

    # 현재 상태 출력
    return {
        "light_on": light_on,
        "current_people": current_people
    }