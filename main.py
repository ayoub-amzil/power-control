import tkinter as tk
import subprocess
import ctypes
from tkinter import messagebox


def forceful_shutdown():
    confirmed = messagebox.askokcancel("Confirmation", "Are you sure you want to shut down?")
    if confirmed:
        subprocess.run(["shutdown", "/s", "/f", "/t", "1"])


def forceful_restart():
    confirmed = messagebox.askokcancel("Confirmation", "Are you sure you want to restart?")
    if confirmed:
        subprocess.run(["shutdown", "/r", "/f", "/t", "1"])


def forceful_lock_session():
    confirmed = messagebox.askokcancel("Confirmation", "Are you sure you want to lock the session?")
    if confirmed:
        subprocess.run(["rundll32.exe", "user32.dll,LockWorkStation"])


def turn_off_screen():
    ctypes.windll.user32.SendMessageW(0xFFFF, 0x112, 0xF170, 2)


window = tk.Tk()
window.title("Power Control")
window.geometry("360x150")
window.configure(bg="#f0f0f0")
window.iconbitmap("power.ico")
window.resizable(False, False)

button_width = 15
button_height = 2
font_style = ("Arial", 12, "bold")

shutdown_button = tk.Button(window, text="Shutdown", command=forceful_shutdown, bg="#ff5555", fg="white", font=font_style, width=button_width, height=button_height)
shutdown_button.grid(row=0, column=0, pady=10, padx=10)

restart_button = tk.Button(window, text="Restart", command=forceful_restart, bg="#55ff55", fg="white", font=font_style, width=button_width, height=button_height)
restart_button.grid(row=0, column=1, pady=10, padx=10)

lock_button = tk.Button(window, text="Lock Session", command=forceful_lock_session, bg="#5555ff", fg="white", font=font_style, width=button_width, height=button_height)
lock_button.grid(row=1, column=0, pady=10, padx=10)

screen_off_button = tk.Button(window, text="Turn Off Screen", command=turn_off_screen, bg="#aa55aa", fg="white", font=font_style, width=button_width, height=button_height)
screen_off_button.grid(row=1, column=1, pady=10, padx=10)

window.mainloop()