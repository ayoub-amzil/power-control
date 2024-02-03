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

button_width = 15
button_height = 2
font_style = ("Arial", 12, "bold")