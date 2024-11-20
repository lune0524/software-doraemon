import random


def temperature():
    return random.uniform(0, 40)


def control_temperature():
    current_temp = temperature()
   
    print(f"현재 온도: {current_temp:.1f}°C")


    if current_temp < 18:
        print("난방기를 작동합니다. 목표 온도: 20~22°C로 올라갑니다.")
        print("창문이 닫힙니다.")
   
    elif 20 <= current_temp <= 22:
        print("현재 온도가 적정 범위에 있습니다.")
        print("난방기와 냉방기의 작동을 멈춥니다.")
        window()


    elif current_temp > 26:
        print("냉방기를 작동합니다. 목표 온도: 24~26°C로 내려갑니다.")
        print("창문이 닫힙니다.")
   
    else:
        print("현재 온도가 냉난방 작동 범위 밖입니다.")
        print("난방기와 냉방기의 작동을 멈춥니다.")
        window()


def window():
    """
    창문을 열지 여부를 묻고, 사용자 입력에 따라 동작합니다.
    """
    answer = input("창문을 여시겠습니까? (Y/N): ").strip().upper()
    if answer == "Y":
        print("창문을 엽니다.")
    elif answer == "N":
        print("창문을 열지 않습니다.")
    else:
        print("잘못된 입력입니다. 창문을 열지 않습니다.")



