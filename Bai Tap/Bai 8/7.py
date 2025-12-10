import tkinter
import random

# list of possible colours.
colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0

# Bước 2: đổi thời gian từ 30 → 120
timeleft = 120


# ----------------------------
# BẮT ĐẦU GAME
# ----------------------------
def startGame(event):
    global timeleft
    if timeleft == 120:          # thời điểm bắt đầu
        countdown()
    nextColour()


# ----------------------------
# HIỆN MÀU MỚI
# ----------------------------
def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        # Bước 3: tính điểm +2 / -1
        if e.get().lower() == colours[1].lower():
            score += 2
        elif e.get() != "":
            score -= 1

        e.delete(0, tkinter.END)

        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))


# ----------------------------
# COUNTDOWN TIMER
# ----------------------------
def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)


# ----------------------------
# GIAO DIỆN TKINTER
# ----------------------------

root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("400x250")

instructions = tkinter.Label(root,
            text="Type the COLOUR of the word, not the word itself!",
            font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root,
            text="Press Enter to start",
            font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root,
            text="Time left: " + str(timeleft),
            font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)
e.pack()

root.bind('<Return>', startGame)

e.focus_set()

root.mainloop()
