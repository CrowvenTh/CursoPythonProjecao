import tkinter as tk

def submit():
    print("Nome:", name_entry.get())
    print("Idade:", age_entry.get())

app = tk.Tk()
app.title("Formulário de Entrada")

tk.Label(app, text="Nome:").grid(row=0)
tk.Label(app, text="Idade:").grid(row=1)

name_entry = tk.Entry(app)
age_entry = tk.Entry(app)

name_entry.grid(row=0, column=1)
age_entry.grid(row=1, column=1)

submit_button = tk.Button(app, text="Enviar", command=submit)
submit_button.grid(row=2, column=1)

app.mainloop()