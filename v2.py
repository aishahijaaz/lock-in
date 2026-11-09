
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk

# Main window
root = tk.Tk()
root.title("Lock In - Version 2")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#FFF0B5")

# Load Figma background
background = Image.open("assets/idle_background.png")
background = background.resize((400, 500))
background_photo = ImageTk.PhotoImage(background)

background_label = tk.Label(
    root,
    image=background_photo,
    bd=0
)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Animated LOCK IN DIVA heading
heading_colors = [
    "#F962A0",
    "#FA7AA6",
    "#FA92AC",
    "#FBABB2",
    "#FBC3B8"
]

heading_index = 0

heading_label = tk.Label(
    root,
    text="LOCK IN DIVA",
    font=("Pixelify Sans", 32),
    fg=heading_colors[0],
    bg="#FFF0B5",
    bd=0
)

heading_label.place(x=200, y=65, anchor="center")


def animate_heading():
    global heading_index

    heading_label.config(fg=heading_colors[heading_index])

    heading_index = (heading_index + 1) % len(heading_colors)

    root.after(500, animate_heading)


animate_heading()


# Timer
timer_label = tk.Label(
    root,
    text="25:00",
    font=("Pixelify Sans", 42),
    fg="#E88DAA",
    bg="#FFF0B5",
    bd=0
)
timer_label.place(x=200, y=327, anchor="center")

# Cat placeholder
cat_label = tk.Label(
    root,
    bg="#FFF0B5",
    bd=0
)
cat_label.place(x=200, y=190, anchor="center")


# Load animated GIFs
def load_gif(path):
    gif = Image.open(path)
    loaded_frames = []

    for frame in ImageSequence.Iterator(gif):
        frame = frame.convert("RGBA")
        frame = frame.resize((190, 190))
        loaded_frames.append(ImageTk.PhotoImage(frame))

    return loaded_frames


idle_frames = load_gif("assets/cat_idle.gif")
focus_frames = load_gif("assets/cat_focus.gif")

current_frames = idle_frames
frame_index = 0


def set_cat_mode(mode):
    global current_frames, frame_index

    if mode == "focus":
        current_frames = focus_frames
    else:
        current_frames = idle_frames

    frame_index = 0


def animate_cat():
    global frame_index

    cat_label.config(image=current_frames[frame_index])

    frame_index = (frame_index + 1) % len(current_frames)

    root.after(80, animate_cat)


# Timer logic
time_left = 25 * 60
timer_running = False


def update_timer():
    minutes = time_left // 60
    seconds = time_left % 60

    timer_label.config(text=f"{minutes:02d}:{seconds:02d}")


def countdown():
    global time_left, timer_running

    if not timer_running:
        return

    if time_left > 0:
        time_left -= 1
        update_timer()
        root.after(1000, countdown)
    else:
        timer_running = False
        button_label.config(image=start_button_photo)
        set_cat_mode("idle")


# Load actual Figma buttons
start_image = Image.open(
    "assets/start_button.png"
).convert("RGBA")

pause_image = Image.open(
    "assets/pause_button.png"
).convert("RGBA")

start_image = start_image.resize((156, 48))
pause_image = pause_image.resize((156, 48))

start_button_photo = ImageTk.PhotoImage(start_image)
pause_button_photo = ImageTk.PhotoImage(pause_image)


# Display Figma START button
button_label = tk.Label(
    root,
    image=start_button_photo,
    bg="#FFF0B5",
    bd=0,
    cursor="hand2"
)

button_label.place(x=200, y=390, anchor="center")


# Start / Pause functionality
def toggle_timer():
    global timer_running

    timer_running = not timer_running

    if timer_running:
        button_label.config(image=pause_button_photo)
        set_cat_mode("focus")
        countdown()
    else:
        button_label.config(image=start_button_photo)
        set_cat_mode("idle")


button_label.bind(
    "<Button-1>",
    lambda event: toggle_timer()
)


# Start cat animation
animate_cat()

# Run application
root.mainloop()
