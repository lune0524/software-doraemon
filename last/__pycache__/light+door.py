from door_last_heesung import access_control  # 문 관련 함수
from light_last_saesol import light  # 불 관련 함수
import time

if __name__ == "__main__":
    # 초기 상태 정의
    state = {
        "light_on": False,
        "current_people": 0,
        "last_activity_time": time.time(),
    }

    print("=== 출입 확인 ===")
    # 교수님이나 학생 출입 여부 확인
    if check_professors() or check_student():
        print("출입이 승인되었습니다.")
        
        # 입실 시 불 켜기
        state = light("in", state)
        
        # 10초 후 퇴실 시뮬레이션 (테스트용)
        time.sleep(10)
        print("=== 퇴실 ===")
        state = light("out", state)
    else:
        print("출입이 거부되었습니다.")