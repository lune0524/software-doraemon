# main.py
import threading
import time
from door_test_03_heesung import check_professors, check_student
from light_test_02_saesol import light, state
from window_test_04_sohyun import smell_set
from air_test_04_younggon import air, stove
from computer_test_04_dayoung import choose_seat
from charging_test_04_kyungmin import charging
from turtle_02 import draw_room, open_door, turn_on_tv, sit_down

# 각 기능을 별도로 실행할 함수 정의
def door_function():
    check_professors()
    check_student()

def light_function():
    print("\n불 상태 관리 시작!")
    global state
    state = light("in", state)  # 입실 처리
    time.sleep(2)
    state = light("out", state)  # 퇴실 처리
    time.sleep(2)
    state = light("check", state)  # 자동 소등 체크

def window_function():
    print("\n창문 환기 관리 시작!")
    smell_set()

def air_function():
    print("\n냉난방기 관리 시작!")
    air()
    stove()

def computer_function():
    print("\n컴퓨터 자리 관리 시작!")
    choose_seat()

def charging_function():
    print("\n충전 관리 시작!")
    charging()

def turtle_function():
    print("\n터틀 애니메이션 시작!")
    draw_room()
    open_door()
    turn_on_tv(-180, 200)  # 서쪽 TV
    sit_down(-300, -20)  # 1조 자리

# 메인 실행
if __name__ == "__main__":
    # 병렬 실행을 위해 쓰레드 사용
    threads = [
        threading.Thread(target=door_function),
        threading.Thread(target=light_function),
        threading.Thread(target=window_function),
        threading.Thread(target=air_function),
        threading.Thread(target=computer_function),
        threading.Thread(target=charging_function),
        threading.Thread(target=turtle_function)
    ]
    
    # 모든 쓰레드 시작
    for thread in threads:
        thread.start()
    
    # 모든 쓰레드 종료 대기
    for thread in threads:
        thread.join()

    print("\n모든 작업이 완료되었습니다!")
