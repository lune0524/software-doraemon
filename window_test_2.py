import random
import time

def smell():
    smell_level = random.randint(0, 100)
    return smell_level

def smell_set():
    smell_level = smell()  # 환기필요도 생성
    print('환기 필요도: ', smell_level)
    # 환기필요도가 일정 수준(50) 이상일 때
    if smell_level > 50:
        while True:
            window_person = input("창문을 열겠습니까? (Y/N): ").strip().upper()
            if window_person in ["Y", "N"]:
                break
            print("잘못된 입력입니다. Y 또는 N으로 답해주세요.")

        if window_person == "Y":
            print("창문을 엽니다.")

            while True:
                air_person = input("냉난방기를 켜겠습니까? (Y/N): ").strip().upper()
                if air_person in ["Y", "N"]:
                    break
                print("잘못된 입력입니다. Y 또는 N으로 답해주세요.")

                if air_person == "Y":
                    print("냉난방기를 켭니다.")
                else:
                    print("냉난방기를 끕니다.")
        else:
            print("창문을 열지 않습니다.")

    else:
        print("냄새 수치가 낮아 창문을 열 필요가 없습니다.")

def smell_time():
    # 시간별 수치 변화를 나타내는 함수
    smell_level = smell()
    pass