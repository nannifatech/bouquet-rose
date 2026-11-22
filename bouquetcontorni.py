import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Bouquet Contorni")
root.geometry("800x750")
root.configure(bg="white")
canvas = tk.Canvas(root, width=800, height=750, bg="white", highlightthickness=0)
canvas.pack()

tempo = 0

# Ogni rosa ora ha un colore diverso!
# (x, y, grandezza, colore)
POS_ROSE = [
    (400, 180, 85, "#ff2d55"),  # rossa
    (305, 230, 78, "#ff9500"),  # arancione
    (495, 230, 78, "#ffcc00"),  # gialla
    (350, 310, 82, "#c86bff"),  # viola
    (450, 310, 82, "#00c7be"),  # turchese
    (400, 270, 90, "#ff6b9d"),  # rosa forte al centro
    (265, 295, 55, "#007aff"),  # blu
    (535, 295, 55, "#34c759"),  # verde
]

def disegna_rosa_contorno(x, y, size, colore, rot):
    # SOLO IL CONTORNO - 2 anelli di numeri, dentro vuoto
    for r in [size, size - 10]:
        n = int(r / 3.2) + 6
        for i in range(n):
            ang = (i / n) * 2 * math.pi + rot
            px = x + math.cos(ang) * r
            py = y + math.sin(ang) * r * 0.85
            num = (i * 5 + int(tempo * 4)) % 10
            fs = int(10 + r * 0.12)
            canvas.create_text(px, py, text=str(num), fill=colore, font=("Courier", fs, "bold"))
    
    # Piccolo cerchio al centro - solo il cuore della rosa
    for i in range(8):
        ang = (i / 8) * 2 * math.pi + rot
        px = x + math.cos(ang) * 12
        py = y + math.sin(ang) * 12 * 0.85
        canvas.create_text(px, py, text=str((i + int(tempo*2)) % 10), fill=colore, font=("Courier", 11, "bold"))

def disegna_verde():
    for _ in range(90):
        ang = random.uniform(0, 2*math.pi)
        dist = random.uniform(120, 210)
        px = 400 + math.cos(ang) * dist
        py = 250 + math.sin(ang) * dist * 0.75
        if 300 < px < 500 and 150 < py < 350:
            continue
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#2ecc71", font=("Courier", 9, "bold"))

def anima():
    global tempo
    tempo += 0.05
    canvas.delete("all")

    # Steli che si stringono
    for i in range(35):
        py = 380 + i * 5
        larg = 60 - i * 1.2
        for k in range(4):
            px = 400 + random.uniform(-larg, larg) * (i/40)
            canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#2e9e5b", font=("Courier", 9, "bold"))

    # Carta del mazzo
    for i in range(50):
        px = random.uniform(220, 400)
        py = 380 + (400 - px) * 0.45
        if py < 600:
            canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#e8e8e8", font=("Courier", 9))
    for i in range(50):
        px = random.uniform(400, 580)
        py = 380 + (px - 400) * 0.45
        if py < 600:
            canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#e8e8e8", font=("Courier", 9))

    disegna_verde()

    # Rose - solo contorni, oscillano insieme
    ox = math.sin(tempo) * 6
    oy = math.cos(tempo * 0.8) * 3
    for (x, y, s, c) in POS_ROSE:
        disegna_rosa_contorno(x + ox, y + oy, s, c, tempo * 0.4)

    # Fiocchetto
    for i in range(20):
        px = 400 + random.uniform(-15, 15)
        py = 570 + random.uniform(-10, 10)
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#ffcc00", font=("Courier", 12, "bold"))
    for i in range(35):
        px = 400 - 20 - i * 3
        py = 570 + math.sin(i*0.3) * 18
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#ffcc00", font=("Courier", 11, "bold"))
        px = 400 + 20 + i * 3
        py = 570 + math.sin(i*0.3) * 18
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#ffcc00", font=("Courier", 11, "bold"))

    root.after(60, anima)

anima()
root.mainloop()
