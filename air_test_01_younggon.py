import random


def temperature():
    return random.uniform(0, 40)


def control_temperature():
    current_temp = temperature()
   
    print("현재 온도: ", current_temp)


    if current_temp < 18:
        print("난방기를 작동합니다.")
        print("창문이 닫힙니다.")
   
    elif 20 <= current_temp <= 22:
        print("현재 온도가 적정 범위에 있습니다.")
        print("난방기와 냉방기의 작동을 멈춥니다.")


    elif current_temp > 26:
        print("냉방기를 작동합니다.")
        print("창문이 닫힙니다.")
   
    else:
        print("현재 온도가 냉난방 작동 범위 밖입니다.")
        print("난방기와 냉방기의 작동을 멈춥니다.")
