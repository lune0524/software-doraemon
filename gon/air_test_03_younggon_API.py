import random
import time

def temperature():
    temp = random.randint(0, 40)
    print("현재 온도는", temp, "도 입니다.")
    return temp

def air():
    temp = temperature()
    if temp > 26:
        print("현재 온도가", temp, "도 입니다. 냉방기가 작동합니다.")
        print("창문이 닫힙니다.")
        time.sleep(10)
        print("현재 온도가 24도로 맞춰집니다. 냉방기가 꺼집니다.")
    else:
        print("현재 온도가", temp, "도 이므로 적정 온도입니다.")

def stove():
    temp = temperature()
    if temp < 18:
        print("현재 온도가", temp, "도 입니다. 난방기가 작동합니다.")
        print("창문이 닫힙니다.")
        time.sleep(10)
        print("현재 온도가 20도로 맞춰집니다. 난방기가 꺼집니다.")
    else:
        print("현재 온도가", temp, "도 이므로 적정 온도입니다.")

air()
stove()
