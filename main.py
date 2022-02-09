import tkinter, win32api, os, time
import customtkinter as custom
import threading


def soundBeep(number):
    for i in range(number):
        time.sleep(0.05)
        win32api.Beep(1000, 100)


def clickExited():
    soundBeep(3)
    os._exit(0)


def eventHackedMoney(var):
    global label_notify
    if var.get():
        soundBeep(2)
        label_notify.configure(text= "Money")
        label_status.configure(text_color = "lime")
        label_status["text"] = "ON"
    else:
        soundBeep(1)
        label_notify.configure(text="Money")
        label_status.configure(text_color = "red")
        label_status["text"] = "OFF"


def eventHackedLevel(var):
    global label_notify
    if var.get():
        soundBeep(2)
        label_notify.configure(text="Level")
        label_status.configure(text_color="lime")
        label_status["text"] = "ON"
    else:
        soundBeep(1)
        label_notify.configure(text="Level")
        label_status.configure(text_color="red")
        label_status["text"] = "OFF"


# --------------------------------------------------------------

WIDTH = 1920
HEIGHT = 1080

soundBeep(3)
window = custom.CTk()
window.title("              ")
window.overrideredirect(False)
custom.set_default_color_theme("dark-blue")
window.resizable(width=False, height=False)
window.call("wm", "attributes", ".", "-alpha", "1")
window.call("wm", "attributes", ".", "-topmost", "true")
window.geometry(f"{int(WIDTH / 6)}x{int(HEIGHT / 2)}+800+200")

# --------------------------------------------------------------

frame_background = custom.CTkFrame(master=window, width=150, height=30, corner_radius=0)
frame_background.configure(fg_color="gray17", bg="gray17")
frame_background.pack(side="top", fill="both")

label_title = custom.CTkLabel(master=frame_background, width=200, height=30, corner_radius=0)
label_title.configure(text="Name Process", text_color="yellow", font=("LCDMONO", 14, "bold"))
label_title.configure(bg_color="gray20", fg_color="gray20")
label_title.pack(side="left")

button_exit = custom.CTkButton(master=frame_background, text_font=("LCDMONO", 14), corner_radius=0)
button_exit.configure(text="Quit", border_color="gray17", hover_color="red", fg_color="lime")
button_exit.configure(command=clickExited)
button_exit.pack(side="right")

# --------------------------------------------------------------

frame_background = custom.CTkFrame(master=window, width=150, height=450, corner_radius= 0)
frame_background.configure(fg_color="gray10", bg="gray10")
frame_background.pack(fill="both")

label_money = custom.CTkLabel(master=frame_background, width=100, height=25, corner_radius=1)
label_money.configure(text="MONEY", font=("LCDMONO", 14, "bold"), text_color="yellow")
label_money.configure(bg_color="gray20", fg_color="gray20")
label_money.place(x=50, y=50)

label_level = custom.CTkLabel(master=frame_background, width=100, height=25, corner_radius=1)
label_level.configure(text="LEVEL", font=("LCDMONO", 14, "bold"), text_color="yellow")
label_level.configure(bg_color="gray20", fg_color="gray20")
label_level.place(x=50, y=100)

label_1 = custom.CTkLabel(master=frame_background, width=100, height=25, corner_radius=1)
label_1.configure(text="SELECT", font=("LCDMONO", 14, "bold"), text_color="yellow")
label_1.place(x=50, y=200)

label_2 = custom.CTkLabel(master=frame_background, width=100, height=25, corner_radius=1)
label_2.configure(text="SELECT", font=("LCDMONO", 14, "bold"), text_color="yellow")
label_2.place(x=50, y=250)

label_3 = custom.CTkLabel(master=frame_background, width=100, height=25, corner_radius=1)
label_3.configure(text="SELECT", font=("LCDMONO", 14, "bold"), text_color="yellow")
label_3.place(x=50, y=300)

# --------------------------------------------------------------

on_image = tkinter.PhotoImage(width=48, height=19)
off_image = tkinter.PhotoImage(width=48, height=19)
off_image.put(("red",), to=(0, 0, 23, 18))
on_image.put(("lime",), to=(24, 0, 47, 18))

intvar_money = tkinter.IntVar(value=0)
checkbutton_money = tkinter.Checkbutton(frame_background, image=off_image, selectimage=on_image, bd=1)
checkbutton_money.configure(indicatoron=False, onvalue=1, offvalue=0, variable=intvar_money)
checkbutton_money.configure(command=lambda: eventHackedMoney(intvar_money))
checkbutton_money.configure(bg="gray17", selectcolor="gray17")
checkbutton_money.configure(activebackground="gray32")
checkbutton_money.place(x=200, y=50)

intvar_level = tkinter.IntVar(value=0)
checkbutton_level = tkinter.Checkbutton(frame_background, image=off_image, selectimage=on_image, bd=1)
checkbutton_level.configure(indicatoron=False, onvalue=1, offvalue=0, variable=intvar_level)
checkbutton_level.configure(command=lambda: eventHackedLevel(intvar_level), bg="gray17")
checkbutton_level.configure(bg="gray17", selectcolor="gray17")
checkbutton_level.configure(activebackground="gray32")
checkbutton_level.place(x=200, y=100)

intvar_2 = tkinter.IntVar(value=0)
checkbutton = tkinter.Checkbutton(frame_background, image=off_image, selectimage=on_image, bd=1)
checkbutton.configure(indicatoron=False, onvalue=1, offvalue=0, variable=intvar_2)
checkbutton.configure(bg="gray17", selectcolor="gray17")
checkbutton.configure(activebackground="gray32")
checkbutton.place(x=200, y=200)

intvar_3 = tkinter.IntVar(value=0)
checkbutton = tkinter.Checkbutton(frame_background, image=off_image, selectimage=on_image, bd=1)
checkbutton.configure(indicatoron=False, onvalue=1, offvalue=0, variable=intvar_3)
checkbutton.configure(bg="gray17", selectcolor="gray17")
checkbutton.configure(activebackground="gray32")
checkbutton.place(x=200, y=250)

intvar_4 = tkinter.IntVar(value=0)
checkbutton = tkinter.Checkbutton(frame_background, image=off_image, selectimage=on_image, bd=1)
checkbutton.configure(indicatoron=False, onvalue=1, offvalue=0, variable=intvar_4)
checkbutton.configure(bg="gray17", selectcolor="gray17")
checkbutton.configure(activebackground="gray32")
checkbutton.place(x=200, y=300)


label_notify = custom.CTkLabel(master=frame_background, width=100, height=30, corner_radius=2)
label_notify.configure(text="Notify", font=("LCDMONO", 14, "bold"), text_color="yellow")
label_notify.configure(bg_color="gray5", fg_color="gray5")
label_notify.place(x=50, y=370)

label_status = custom.CTkLabel(master=frame_background, width=50, height=30, corner_radius=2)
label_status.configure(text="OFF", font=("LCDMONO", 14, "bold"), text_color="red")
label_status.configure(bg_color="gray5", fg_color="gray5")
label_status.place(x=200, y=370)

# --------------------------------------------------------------

frame_background = custom.CTkFrame(master=window, width=150, height=75, corner_radius=0)
frame_background.configure(fg_color="gray10", bg="gray10")
frame_background.pack(side="bottom", fill="both")

label = custom.CTkLabel(master=frame_background, width=320, height=30, corner_radius=0)
label.configure(text="Three Dragons", font=("LCDMONO", 14, "bold"), text_color="yellow")
label.configure(bg_color="gray17", fg_color="gray17")
label.place(x=0, y=0)

label = custom.CTkLabel(master=frame_background, width=320, height=30, corner_radius=0)
label.configure(text="Mod By Duke", font=("LCDMONO", 14, "bold"), text_color="yellow")
label.configure(bg_color="gray17", fg_color="gray17")
label.place(x=0, y=30)

# --------------------------------------------------------------

try:
    window.mainloop()
except KeyboardInterrupt:
    exit(0)
