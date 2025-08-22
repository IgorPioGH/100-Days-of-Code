from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer, reps
    window.after_cancel(timer)
    # timer 00:00
    imagem.itemconfig(timer_text, text="00:00")
    # title "Timer"
    texto.config(text="Timer")
    # checkmarks ""
    reps = 0
    marks = ""
    checkmarks.config(text=marks)



# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN

    if reps % 8 == 0:
        count_down(long_break_sec)
        texto.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        texto.config(text="Short Break", fg=PINK)
    else:
        texto.config(text="Study Time", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count=10):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    # editando o texto da imagem
    imagem.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >0:
        global timer
        timer = window.after(1000, count_down,count-1) # Recursao
    else:
        start_timer()
        marks = ""
        for _ in range(reps//2):
            marks += "✓"
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# Colocando texto
texto = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW, highlightthickness=0)
texto.grid(column=1,row=0)

# Colocando imagem
imagem = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
foto = PhotoImage(file="tomato.png")# le um arquivo para pegar uma foto
imagem.create_image(100, 110, image=foto) # create_image(x, y)
# colocando texto sobre a imagem
timer_text = imagem.create_text(100, 130,text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
imagem.grid(column=1,row=1)


# Colocando botao esquerdo e fazendo executar a funcao de comecar a contar
botao_esq = Button(text="Start", highlightthickness=0, command=start_timer)
botao_esq.grid(column=0,row=2)

# Colocando botao direito
botao_dir = Button(text="Reset", highlightthickness=0, command=reset_timer)
botao_dir.grid(column=2,row=2)

# Colocando checkmark
checkmarks = Label(text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1,row=3)



window.mainloop()