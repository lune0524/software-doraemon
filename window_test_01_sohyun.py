import random

def smell_set():

    smell_level = random.randint(0, 100)
    print('환기필요도: ', smell_level)

    # 환기필요도가 일정 수준(50) 이상일 때
    if smell_level > 50:
        print(smell_level)
        window_person = input("창문을 열겠습니까? (예/아니오): ")
        if window_person == "예":
            print("창문을 엽니다.")
            air_person = input("냉난방기를 켜겠습니까? (예/아니오): ")
            if air_person == "예":
                print("냉난방기를 켭니다.")
            else:
                print("냉난방기를 끕니다.")
        else:
            print("창문을 열지 않습니다.")
    else:
        print("냄새 수치가 낮아 창문을 열 필요가 없습니다.")