from tkinter import Tk, Entry, Label, END, Button

# variaveis
valor_fahrenheit = 0
valor_celsius = 0

# Criando a tela
window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=200, height=200)
window.config(padx=50, pady=100)

# Input Celsius
c_input = Entry(width=10)
c_input.grid(column=0, row=0)
c_label = Label(text='ºC')
c_label.grid(column=1, row=0)


# Equals
equal = Label(text="=")
equal.grid(column=2,row=0)

# Input Fahrenheit
f_input = Entry(width=10)
f_label= Label(text="º F")
f_input.grid(column=3,row=0)
f_label.grid(column=4, row=0)


# Botao calculo
def action():
    try:
        if f_input.get().strip():
            f = float(f_input.get())
            c = (f - 32) * 5/9
            c_input.delete(0, END)
            c_input.insert(END, string=f"{c:.2f}")
        elif c_input.get().strip():
            c = float(c_input.get())
            f = (c * 9/5) + 32
            f_input.delete(0,END)
            f_input.insert(END, string=f"{f:.2f}")
        else:
            c_input.delete(0, END)
            f_input.delete(0, END)
    except ValueError:
        c_input.delete(0, END)
        f_input.delete(0,END)


button = Button(text="Calcular", command=action)
button.grid(column=2, row=1, pady=10, padx=10)



window.mainloop()