
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

def start_timer():
    print("Timer started!")
    timer_label.config(text="24:59")

button = tk.Button(
    root, text="START", fg="black",
    bg="#61588F", command=start_timer
)
button.pack(pady=20)

root.mainloop()
