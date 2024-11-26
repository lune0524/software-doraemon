import random
import time

def smell():
    # 환기 필요도를 0~100 사이의 임의의 값으로 생성
    return random.randint(0, 100)

def smell_set():
    # 환기 필요도 및 시간별 변화 처리
    smell_level = smell()  # 환기 필요도 생성
    print("환기 필요도:", smell_level)

    if smell_level > 50:  # 환기 필요도가 50 이상일 때
        while True:
            window_person = input("창문을 열겠습니까? (Y/N): ").strip().upper()
            if window_person in ["Y", "N"]:
                break
            print("잘못된 입력입니다. Y 또는 N으로 답해주세요.")

        if window_person == "Y":
            print("창문을 엽니다.")
            air_control()  # 냉난방기 작동 여부 확인
            print("초기 환기 필요도:", smell_level)

            # 환기 필요도가 감소하는 과정을 처리
            while smell_level > 30:  # 환기 필요도가 30 이하가 될 때까지 감소
                time.sleep(1)  # 1초 대기
                decrease = random.randint(5, 15)  # 5~15 사이의 임의 값만큼 감소
                smell_level -= decrease
                if smell_level < 0:
                    smell_level = 0  # 음수 방지
                print(f"현재 환기 필요도: {smell_level}")

            print("환기 필요도가 30 이하로 떨어졌습니다. 창문을 닫습니다.")
        else:
            print("창문을 열지 않습니다.")
    else:
        print("냄새 수치가 낮아 창문을 열 필요가 없습니다.")


def air_control():
    # 냉난방기 작동 여부를 묻는 함수
    while True:
        air_person = input("냉난방기를 켜겠습니까? (Y/N): ").strip().upper()
        if air_person in ["Y", "N"]:
            break
        print("잘못된 입력입니다. Y 또는 N으로 답해주세요.")

    if air_person == "Y":
        print("냉난방기를 켭니다.")
    else:
        print("냉난방기를 끕니다.")
        

# 테스트 실행
if __name__ == "__main__":
    smell_set()