
import tkinter as tk

root = tk.Tk()
root.title("Lock In")
root.geometry("400x500")
root.configure(bg="#61588F")

heading = tk.Label(
    root, text="LOCK IN", font=("Arial", 24),
    fg="white", bg="#61588F"
)
heading.pack(pady=20)

timer_label = tk.Label(
    root, text="25:00", font=("Arial", 48),
    fg="white", bg="#61588F"
)
timer_label.pack(pady=30)

time_left = 1500
timer_running = False


def start_timer():
    global timer_running

    if timer_running:
        return

    timer_running = True
    countdown()


def countdown():
    global time_left, timer_running

    minutes = time_left // 60
    seconds = time_left % 60

    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")

    if time_left > 0:
        time_left -= 1
        root.after(1000, countdown)
    else:
        timer_running = False
        timer_label.config(text="00:00")


button = tk.Button(
    root, text="START", fg="black",
    bg="#61588F", command=start_timer
)
button.pack(pady=20)

root.mainloop()
