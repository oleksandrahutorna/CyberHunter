import tkinter as tk
import random
from tkinter import messagebox

score = 0
lives = 5
level = 1
speed = 1000
goal = 100
move_job = None

def move_character():
    global speed, move_job
    if lives > 0 and score < goal:
        new_x = random.randint(50, 700)
        new_y = random.randint(80, 500)

        btn_target.place(x=new_x, y=new_y)
        move_job = root.after(speed, move_character)
    else:
        move_job = None

def on_click():
    global score, speed, level
    if lives <= 0: return

    score += 1
    if score % 5 == 0:
        level += 1
        speed = max(300, speed - 50)
        root.config(bg=random.choice(["#f0f0f0", "#e1f5fe", "#fff9c4"]))


    update_ui()

    if score >= goal:
        messagebox.showinfo("ПЕРЕМОГА!", f"Ти набрав {goal} очок! Рівень: {level}")
        reset_game()

def miss_click(event=None):
    global lives
    if event is not None and event.widget == root:
        lives -= 1
        update_ui()
        root.config(bg="#ffcdd2")
        root.after(100, lambda: root.config(bg="#f0f0f0"))

        if lives <= 0:
            messagebox.showerror("GAME OVER", f"Життя закінчилися! Твій рахунок: {score}")
            reset_game()

def update_ui():
    label_info.config(text=f"очки: {score} | життя: {lives} | рівень: {level}")

def reset_game():
    global score, lives, level, speed, move_job
    if move_job is not None:
        root.after_cancel(move_job)
        move_job = None

    score = 0
    lives = 5
    level = 1
    speed = 1000
    update_ui()
    move_character()

root = tk.Tk()
root.title("Cyber Hunter 2026")
root.geometry("800x600")
root.resizable(False, False)

root.bind("<Button-1>", miss_click)

label_info = tk.Label(root, text=f"очки: 0, | життя: 5   | рівень: 1",  font=("Courier New", 20, "bold"), bg="#333", fg="white")
label_info.pack(fill="x")

btn_target = tk.Button(root, text="❤", font=("Arial", 25), command=on_click, bg="#4caf50", fg="white", width=3, relief="raised")
btn_target.place(x=350, y=250)

move_character()

root.mainloop()