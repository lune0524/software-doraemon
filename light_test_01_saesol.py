import time

# 천장등 상태와 인원수를 관리하는 변수
light_on = False                   #천장등 상태를 나타내는 변수
current_people = 0                           #현재 과방에 있는 사람수를 저장하는 변수
last_activity_time = time.time()            # 마지막으로 사람이 출입한 시간을 기록

def ceiling_light(action, student_id=None, student_name=None, timeout=14400):  #입실,퇴실,자동소등/입,퇴실 학생 학번,이름(선택사항),자동소등 기본값

    global light_on, current_people, last_activity_time #함수내부에서 전역변수를 수정하기 위해 사용

    if action == "in":
        # 입실 처리 작성 예정
        pass

    elif action == "out":
        # 퇴실 처리 작성 예정
        pass

    elif action == "check":
        # 사람이 없을 경우 자동 소등 처리 작성 예정
        pass

    else:
        print("잘못된 동작입니다. 'in', 'out', 'check' 중 하나를 선택하세요.")

    # 현재 상태 출력
    return {
        "light_on": light_on,  #불이 켜져있으면 true 아니면 false
        "current_people": current_people      #과방 안의 현재 인원수
    }


#궁금한거 있으면 물어보슈