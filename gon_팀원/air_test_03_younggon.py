import requests
import time

API_KEY = "64f6a9776012addf90ba6752fb5288f9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def temperature():
    """
    특정 도시의 현재 온도를 OpenWeatherMap API에서 가져옵니다.
    city에는 도시 이름을 영어로 입력해주세요. 철자 정확하게
    """
    city = input("도시 이름을 입력하세요: ")
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url, verify=False)
    data = response.json()
        
    try:
        current_temp = data['main']['temp']
        print("현재", city, "의 온도는", current_temp, "도 입니다.")
        return current_temp
    except:
        print("에러가 발생했습니다. KEY 또는 도시이름이 정확한지 확인해 주세요.")
        
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
        
temperature()
