import random

def smell_set():

    smell_level = random.randint(0, 100)
    print('현재 냄새수치: ', smell_level)

    # 냄새 수치가 일정 수준(50) 이상일 때
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

if __name__ == "__main__":
    smell_set()

    # 그럼 창문을 열었을때는 냉난방기를 키지않고 닫았을때만 냉난방기를 키는것으로 하는것 
    # 예 아니오 이런식으로 대답안하면 다시 while문 써서 물어보는거 추가할거에요
    # 약간 그거할까 프로그램이 종료될때 냄새수치가 줄어드는거 출력하고 닫는거를 추가를 하는게 
    # 타임을 불러와서 시간이 지남에 따라 수치변화율을 나타내고 마지막에 수치와 창문을 자동으로 닫겠습니다를 출력