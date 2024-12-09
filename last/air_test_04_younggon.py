import requests 
# HTTP 요청을 보내는 라이브러리, 외부 API와 통신에 사용합니다.
# requests가 작동하지 않을경우 pip install --upgrade requests 를 터미널에 입력한다면 작동 될것 입니다.
import time

API_KEY = "64f6a9776012addf90ba6752fb5288f9"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

requests.packages.urllib3.disable_warnings()
# 출력때 생기는 정식 명칭은 Python warning라는 거 없에는 코드

city = "Jeonju"
air_status = "꺼짐"
stove_status = "꺼짐"

def temperature():
    """
    특정 도시의 현재 온도를 OpenWeatherMap API에서 가져옵니다.
    """
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url, verify=False)
    data = response.json()
        
    try:
        current_temp = data['main']['temp']
        print(f"현재{city}의 온도는 {current_temp}°C 입니다.")
        return current_temp
    except:
        print("에러가 발생했습니다. API_KEY가 정확한지 확인해 주세요.")
        
def air():
    """
    냉방기 함수입니다.
    """
    global air_status
    temp = temperature()
    if temp > 26:
        print(f"현재 온도가 {temp}°C 입니다. 냉방기가 작동합니다.")
        air_status = "켜짐"
        print("창문이 닫힙니다.")
        time.sleep(10)
        print("현재 온도가 24°C로 맞춰집니다. 냉방기가 꺼집니다.")
        air_status = "꺼짐"
    else:
        print(f"현재 온도가 {temp}°C 이므로 적정 온도입니다.")

def stove():
    """
    난방기 함수입니다.
    """
    global stove_status
    temp = temperature()
    if temp < 18:
        print(f"현재 온도가 {temp}°C 입니다. 난방기가 작동합니다.")
        stove_status = "켜짐"
        print("창문이 닫힙니다.")
        time.sleep(10)
        print("현재 온도가 20°C로 맞춰집니다. 난방기가 꺼집니다.")
    else:
        print(f"현재 온도가 {temp}°C 이므로 적정 온도입니다.")
        stove_status = "꺼짐"

if __name__ == "__main__":
    air()
    stove()
