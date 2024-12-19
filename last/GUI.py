import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

# 상태 데이터 초기화
state = {
    "light_on": False,
    "current_people": 0,
    "inside_people": [],
    "window_open": False,
    "air_status": "꺼짐",
}

seats = {
    "1조": 6,
    "2조": 7,
    "3조": 7,
    "4조": 8,
    "5조": 9,
    "6조": 8,
    "컴퓨터 자리": 1,
}
key_seats = {key: 0 for key in seats}

# 교수님과 학생 데이터
professors = ["송주환", "김영수", "이근호", "고선우", "권수태", "민정익"]
students = {
    "장영곤": "202411246",
    "이경민": "202392007",
    "우새솔": "202410798",
    "윤다영": "202411594",
    "양희성": "202411594",
    "박소현": "202412153",
    "김용진": "202411375",
}

# 출입 관리
def open_access_control(root):
    """입실 관리 창"""
    def enter_room():
        user_type = user_type_var.get()
        input_data = entry.get().strip()

        if user_type == "교수님":
            if input_data in professors:
                if input_data not in state["inside_people"]:
                    state["inside_people"].append(input_data)
                    state["current_people"] += 1
                    state["light_on"] = True
                    update_status()
                    messagebox.showinfo("입실 완료", f"{input_data} 교수님이 입실하셨습니다.\n출석이 완료되었습니다.")
                else:
                    messagebox.showwarning("중복 입실", f"{input_data} 교수님은 이미 입실 중입니다.")
            else:
                messagebox.showwarning("등록 오류", "해당 이름의 교수님은 등록되어 있지 않습니다.")
        elif user_type == "학생":
            try:
                name, student_id = input_data.split()
                if name in students and students[name] == student_id:
                    if input_data not in state["inside_people"]:
                        state["inside_people"].append(input_data)
                        state["current_people"] += 1
                        state["light_on"] = True
                        update_status()
                        messagebox.showinfo("입실 완료", f"{name}({student_id}) 학생이 입실하였습니다.\n출석이 완료되었습니다.")
                    else:
                        messagebox.showwarning("중복 입실", f"{name}({student_id}) 학생은 이미 입실 중입니다.")
                else:
                    messagebox.showwarning("등록 오류", "해당 이름과 학번이 등록되지 않았거나 일치하지 않습니다.")
            except ValueError:
                messagebox.showwarning("입력 오류", "이름과 학번을 공백으로 구분하여 입력해주세요.")
        else:
            messagebox.showwarning("선택 오류", "교수님 또는 학생을 선택해주세요.")

    def update_status():
        light_status.set(f"조명 상태: {'켜짐' if state['light_on'] else '꺼짐'}")
        current_people.set(f"현재 인원: {state['current_people']}명")

    access_window = tk.Toplevel(root)
    access_window.title("입실 관리")
    access_window.geometry("400x300")

    tk.Label(access_window, text="입실 관리", font=("Arial", 16)).pack(pady=10)

    tk.Label(access_window, text="사용자 유형:").pack()
    user_type_var = tk.StringVar(value="교수님")
    tk.Radiobutton(access_window, text="교수님", variable=user_type_var, value="교수님").pack()
    tk.Radiobutton(access_window, text="학생", variable=user_type_var, value="학생").pack()

    tk.Label(access_window, text="이름 또는 이름+학번:").pack()
    entry = tk.Entry(access_window)
    entry.pack(pady=5)

    tk.Button(access_window, text="입실", command=enter_room).pack(pady=10)

    light_status = tk.StringVar(value="조명 상태: 꺼짐")
    tk.Label(access_window, textvariable=light_status).pack(pady=5)

    current_people = tk.StringVar(value="현재 인원: 0명")
    tk.Label(access_window, textvariable=current_people).pack()

    tk.Button(access_window, text="닫기", command=access_window.destroy).pack(pady=10)

# 냉난방 및 창문 제어
def temperature_control_step(main_window, next_step):
    """냉난방 및 창문 제어 창"""
    def check_smell():
        smell_level = random.randint(0, 100)
        smell_status.set(f"환기 필요도: {smell_level}")
        if smell_level > 50:
            messagebox.showinfo("환기 필요", "환기가 필요합니다.")
        else:
            messagebox.showinfo("환기 불필요", "환기가 필요하지 않습니다.")

    def toggle_window():
        state["window_open"] = not state["window_open"]
        window_status.set(f"창문 상태: {'열림' if state['window_open'] else '닫힘'}")
        if state["window_open"]:
            messagebox.showinfo("창문 열림", "창문이 열렸습니다.")
        else:
            messagebox.showinfo("창문 닫힘", "창문이 닫혔습니다.")

    def control_air_conditioner():
        temp = random.randint(15, 30)
        temperature_status.set(f"현재 온도: {temp}°C")
        if temp > 26:
            state["air_status"] = "냉방기 켜짐"
            messagebox.showinfo("냉방기 작동", "냉방기가 켜졌습니다. 온도를 낮춥니다.")
        elif temp < 18:
            state["air_status"] = "난방기 켜짐"
            messagebox.showinfo("난방기 작동", "난방기가 켜졌습니다. 온도를 올립니다.")
        else:
            state["air_status"] = "꺼짐"
            messagebox.showinfo("적정 온도", "현재 온도가 적정합니다. 냉난방기를 사용하지 않습니다.")
        air_conditioner_status.set(f"냉난방기 상태: {state['air_status']}")

    temp_window = tk.Toplevel(main_window)
    temp_window.title("냉난방 및 창문 제어")
    temp_window.geometry("400x400")

    tk.Label(temp_window, text="냉난방 및 창문 제어", font=("Arial", 16)).pack(pady=10)

    temperature_status = tk.StringVar(value="현재 온도: 미확인")
    tk.Label(temp_window, textvariable=temperature_status).pack(pady=5)
    tk.Button(temp_window, text="온도 확인 및 냉난방기 제어", command=control_air_conditioner).pack(pady=5)

    smell_status = tk.StringVar(value="환기 필요도: 미확인")
    tk.Label(temp_window, textvariable=smell_status).pack(pady=5)
    tk.Button(temp_window, text="환기 확인", command=check_smell).pack(pady=5)

    window_status = tk.StringVar(value="창문 상태: 닫힘")
    tk.Label(temp_window, textvariable=window_status).pack(pady=5)
    tk.Button(temp_window, text="창문 열기/닫기", command=toggle_window).pack(pady=5)

    air_conditioner_status = tk.StringVar(value="냉난방기 상태: 꺼짐")
    tk.Label(temp_window, textvariable=air_conditioner_status).pack(pady=10)

    tk.Button(temp_window, text="다음 단계", command=lambda: [temp_window.destroy(), next_step()]).pack(pady=10)

# 자리 선택 및 충전
def seat_and_charging_step(main_window):
    """자리 선택 및 충전 관리 창"""
    def choose_seat():
        selected_seat = seat_var.get()
        if selected_seat in seats:
            if key_seats[selected_seat] < seats[selected_seat]:
                key_seats[selected_seat] += 1
                messagebox.showinfo("자리 배정", f"{selected_seat}에 자리가 배정되었습니다.")
            else:
                messagebox.showwarning("자리 부족", f"{selected_seat}에 자리가 가득 찼습니다.")
        else:
            messagebox.showwarning("잘못된 선택", "유효하지 않은 자리입니다.")

    def start_charging():
        level = random.randint(0, 90)
        messagebox.showinfo("충전 시작", f"현재 배터리 잔량은 {level}%입니다.")
        while level < 100:
            time.sleep(1)
            level += 10
            charging_status.set(f"충전 중: {level}%")
        charging_status.set("충전 완료!")
        messagebox.showinfo("충전 완료", "충전이 완료되었습니다.")

    seat_window = tk.Toplevel(main_window)
    seat_window.title("자리 선택 및 충전")
    seat_window.geometry("400x400")

    tk.Label(seat_window, text="자리 선택", font=("Arial", 16)).pack(pady=10)

    seat_var = tk.StringVar(value="1조")
    seat_menu = ttk.Combobox(seat_window, textvariable=seat_var, values=list(seats.keys()), state="readonly")
    seat_menu.pack(pady=5)

    tk.Button(seat_window, text="자리 선택", command=choose_seat).pack(pady=5)

    tk.Label(seat_window, text="충전 관리", font=("Arial", 16)).pack(pady=10)
    charging_status = tk.StringVar(value="충전 대기 중")
    tk.Label(seat_window, textvariable=charging_status).pack(pady=5)
    tk.Button(seat_window, text="충전 시작", command=start_charging).pack(pady=5)

    tk.Button(seat_window, text="종료", command=seat_window.destroy).pack(pady=10)

# 메인 GUI
def start_main_gui():
    root = tk.Tk()
    root.title("관리 시스템")
    root.geometry("400x200")

    tk.Label(root, text="관리 시스템", font=("Arial", 20)).pack(pady=10)
    tk.Button(root, text="입실 관리", command=lambda: open_access_control(root), width=20).pack(pady=10)
    tk.Button(root, text="시작", command=lambda: temperature_control_step(root, lambda: seat_and_charging_step(root)), width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_main_gui()
