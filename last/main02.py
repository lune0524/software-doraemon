from door_last_heesung import access_control
from light_last_saesol import light

def main():
    print("=== 출입 관리 및 조명 시스템 ===\n")
    while True:
        print("\n--- 출입 권한 확인 중입니다 ---")
        user_status = access_control()  # 교수님 or 학생 입장 처리
        if user_status:
                action = input("입실 또는 퇴실을 선택해주세요. (입실/퇴실/종료): ").strip()
                if action == "입실":
                    light("in")  # 입실 처리
                elif action == "퇴실":
                    light("out")  # 퇴실 처리
                elif action == "종료":
                    print("시스템을 종료합니다. 안녕히 가세요!")
                    return
                else:
                    print("잘못된 입력입니다. '입실', '퇴실', '종료' 중 하나를 입력하세요.")
        else:
            print("권한 확인 실패. 시스템을 종료합니다.")
if __name__ == "__main__":
    main()
