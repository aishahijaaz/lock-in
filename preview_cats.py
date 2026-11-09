
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

root = tk.Tk()
root.title("Lock In - Cat Animation Test")
root.geometry("400x500")
root.configure(bg="#FFF0B5")

gif = Image.open("assets/cat_focus.gif")

frames = []

for frame in ImageSequence.Iterator(gif):
    frame = frame.convert("RGBA")
    frame = frame.resize((250, 250))
    frames.append(ImageTk.PhotoImage(frame))

cat_label = tk.Label(root, bg="#FFF0B5")
cat_label.pack(expand=True)

frame_index = 0

def animate():
    global frame_index

    cat_label.config(image=frames[frame_index])

    frame_index = (frame_index + 1) % len(frames)

    root.after(80, animate)

animate()

root.mainloop()
