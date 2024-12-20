import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

# 상태 데이터 초기화
state = {
    "light_on": False,
    "current_people": 0,
    "inside_people": [],
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

# 출입 관리 함수
def open_access_control():
    """출입 관리 창"""
    def enter_room():
        name = name_entry.get().strip()
        if name and name not in state["inside_people"]:
            state["inside_people"].append(name)
            state["current_people"] += 1
            state["light_on"] = True
            update_status()
            messagebox.showinfo("입실", f"{name}님이 입실하셨습니다.")
        elif name in state["inside_people"]:
            messagebox.showwarning("중복 입실", f"{name}님은 이미 입실 중입니다.")
        else:
            messagebox.showwarning("입력 오류", "이름을 입력해주세요.")

    def exit_room():
        name = name_entry.get().strip()
        if name in state["inside_people"]:
            state["inside_people"].remove(name)
            state["current_people"] -= 1
            if state["current_people"] == 0:
                state["light_on"] = False
            update_status()
            messagebox.showinfo("퇴실", f"{name}님이 퇴실하셨습니다.")
        else:
            messagebox.showwarning("퇴실 오류", f"{name}님은 실내에 없습니다.")

    def update_status():
        light_status.set(f"조명 상태: {'켜짐' if state['light_on'] else '꺼짐'}")
        current_people.set(f"현재 인원: {state['current_people']}명")

    access_window = tk.Toplevel(root)
    access_window.title("출입 관리")
    access_window.geometry("400x200")

    tk.Label(access_window, text="출입 관리", font=("Arial", 16)).pack(pady=10)
    tk.Label(access_window, text="이름:").pack()
    name_entry = tk.Entry(access_window)
    name_entry.pack(pady=5)

    tk.Button(access_window, text="입실", command=enter_room).pack(pady=5)
    tk.Button(access_window, text="퇴실", command=exit_room).pack(pady=5)

    light_status = tk.StringVar(value="조명 상태: 꺼짐")
    tk.Label(access_window, textvariable=light_status).pack(pady=5)

    current_people = tk.StringVar(value="현재 인원: 0명")
    tk.Label(access_window, textvariable=current_people).pack()

# 냉난방 및 창문 제어
def open_temperature_control():
    """냉난방 및 창문 제어 창"""
    def check_smell():
        smell_level = random.randint(0, 100)
        smell_status.set(f"환기 필요도: {smell_level}")
        if smell_level > 50:
            messagebox.showinfo("환기 필요", "환기가 필요합니다.")
        else:
            messagebox.showinfo("환기 불필요", "환기가 필요하지 않습니다.")

    def toggle_window():
        window_status.set(f"창문 상태: {'열림' if window_status.get() == '닫힘' else '닫힘'}")

    temp_window = tk.Toplevel(root)
    temp_window.title("냉난방 및 창문 제어")
    temp_window.geometry("400x200")

    tk.Label(temp_window, text="냉난방 및 창문 제어", font=("Arial", 16)).pack(pady=10)

    smell_status = tk.StringVar(value="환기 필요도: 미확인")
    tk.Label(temp_window, textvariable=smell_status).pack(pady=5)
    tk.Button(temp_window, text="환기 확인", command=check_smell).pack(pady=5)

    window_status = tk.StringVar(value="창문 상태: 닫힘")
    tk.Label(temp_window, textvariable=window_status).pack(pady=5)
    tk.Button(temp_window, text="창문 열기/닫기", command=toggle_window).pack(pady=5)

# 자리 선택 및 충전
def open_seat_and_charging():
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

    seat_window = tk.Toplevel(root)
    seat_window.title("자리 선택 및 충전")
    seat_window.geometry("400x300")

    tk.Label(seat_window, text="자리 선택", font=("Arial", 16)).pack(pady=10)

    seat_var = tk.StringVar(value="1조")
    seat_menu = ttk.Combobox(seat_window, textvariable=seat_var, values=list(seats.keys()), state="readonly")
    seat_menu.pack(pady=5)

    tk.Button(seat_window, text="자리 선택", command=choose_seat).pack(pady=5)

    tk.Label(seat_window, text="충전 관리", font=("Arial", 16)).pack(pady=10)
    charging_status = tk.StringVar(value="충전 대기 중")
    tk.Label(seat_window, textvariable=charging_status).pack(pady=5)
    tk.Button(seat_window, text="충전 시작", command=start_charging).pack(pady=5)

# 메인 GUI
root = tk.Tk()
root.title("관리 시스템")
root.geometry("400x300")

tk.Label(root, text="관리 시스템", font=("Arial", 20)).pack(pady=10)
tk.Button(root, text="출입 관리", command=open_access_control, width=20).pack(pady=10)
tk.Button(root, text="냉난방 및 창문 제어", command=open_temperature_control, width=20).pack(pady=10)
tk.Button(root, text="자리 선택 및 충전", command=open_seat_and_charging, width=20).pack(pady=10)

root.mainloop()
