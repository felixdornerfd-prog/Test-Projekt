import tkinter as tk
from tkinter import font

# ===============================
# Berechnungsfunktion
# ===============================
def calculate(op):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        if op == '+':
            result.set(a + b)
        elif op == '-':
            result.set(a - b)
        elif op == '*':
            result.set(a * b)
        elif op == '/':
            result.set(a / b if b != 0 else "Fehler: ÷0")

    except ValueError:
        result.set("Ungültige Eingabe")


# ===============================
# Hauptfenster
# ===============================
root = tk.Tk()
root.title("Mini-Rechner")
root.geometry("360x280")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# ===============================
# Schriftarten
# ===============================
font_entry = font.Font(family="Segoe UI", size=12)
font_result = font.Font(family="Segoe UI", size=16, weight="bold")
font_button = font.Font(family="Segoe UI", size=12, weight="bold")

# ===============================
# Eingabebereich
# ===============================
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack(pady=15)

entry_a = tk.Entry(
    input_frame,
    width=12,
    font=font_entry,
    justify="center",
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry_a.grid(row=0, column=0, padx=8)

entry_b = tk.Entry(
    input_frame,
    width=12,
    font=font_entry,
    justify="center",
    bg="#2d2d2d",
    fg="white",
    insertbackground="white",
    relief="flat"
)
entry_b.grid(row=0, column=1, padx=8)

# ===============================
# Ergebnisanzeige
# ===============================
result = tk.StringVar()

result_label = tk.Label(
    root,
    textvariable=result,
    font=font_result,
    bg="#252526",
    fg="#4fc3f7",
    width=20,
    height=2
)
result_label.pack(pady=15)

# ===============================
# Button-Bereich
# ===============================
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

button_style = {
    "width": 6,
    "height": 2,
    "font": font_button,
    "bg": "#3a3a3a",
    "fg": "white",
    "activebackground": "#007acc",
    "activeforeground": "white",
    "relief": "flat",
    "cursor": "hand2"
}

for i, op in enumerate(['+', '-', '*', '/']):
    tk.Button(
        button_frame,
        text=op,
        command=lambda o=op: calculate(o),
        **button_style
    ).grid(row=0, column=i, padx=6)

# ===============================
# Event-Loop
# ===============================
root.mainloop()