import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Bouquet Rose Vere")
root.geometry("800x750")
root.configure(bg="white")
canvas = tk.Canvas(root, width=800, height=750, bg="white", highlightthickness=0)
canvas.pack()

tempo = 0

# ORDINE IMPORTANTE: prima quelle DIETRO, per ultima quella DAVANTI
# Dietro -> davanti
POS_ROSE = [
    (265, 295, 55, "#007aff"),  # blu - più dietro a sinistra
    (535, 295, 55, "#34c759"),  # verde - più dietro a destra
    (305, 230, 78, "#ff9500"),  # arancione
    (495, 230, 78, "#ffcc00"),  # gialla
    (350, 310, 82, "#c86bff"),  # viola
    (450, 310, 82, "#00c7be"),  # turchese
    (400, 180, 85, "#ff2d55"),  # rossa in alto
    (400, 270, 90, "#ff6b9d"),  # rosa - DAVANTI A TUTTE, per ultima
]

def disegna_rosa_petali(x, y, size, colore, rot):
    # TAPPO BIANCO: cancella le rose dietro che stanno sotto questa
    # Così la rosa davanti copre davvero quelle dietro
    canvas.create_oval(x - size*1.15, y - size*1.0, x + size*1.15, y + size*1.0, fill="white", outline="white")
    
    # 1. CONTORNO ESTERNO A PETALI - 5 petali
    for step in range(180):
        ang = (step / 180) * 2 * math.pi
        r = size * (0.82 + 0.28 * math.sin(5 * ang + rot))
        px = x + math.cos(ang) * r
        py = y + math.sin(ang) * r * 0.85
        num = (step + int(tempo * 3)) % 10
        canvas.create_text(px, py, text=str(num), fill=colore, font=("Courier", 12, "bold"))

    # 2. PETALI INTERNI
    for step in range(130):
        ang = (step / 130) * 2 * math.pi
        r = size * 0.55 * (0.82 + 0.28 * math.sin(5 * ang + rot + 1.2))
        px = x + math.cos(ang) * r
        py = y + math.sin(ang) * r * 0.85
        num = (step * 2 + int(tempo * 3)) % 10
        canvas.create_text(px, py, text=str(num), fill=colore, font=("Courier", 10, "bold"))

    # 3. CUORE A SPIRALE
    for t in range(80):
        tt = t / 80 * 4 * math.pi + rot
        r = 4 + t * 0.25
        px = x + math.cos(tt) * r
        py = y + math.sin(tt) * r * 0.85
        num = (t + int(tempo * 4)) % 10
        canvas.create_text(px, py, text=str(num), fill=colore, font=("Courier", 9, "bold"))

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

    # Steli
    for i in range(35):
        py = 380 + i * 5
        larg = 60 - i * 1.2
        for k in range(4):
            px = 400 + random.uniform(-larg, larg) * (i/40)
            canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#2e9e5b", font=("Courier", 9, "bold"))

    # Carta
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

    ox = math.sin(tempo) * 6
    oy = math.cos(tempo * 0.8) * 3
    # Le disegno in ordine: dietro -> davanti
    # Ognuna cancella con il bianco quello che c'è sotto di lei
    for (x, y, s, c) in POS_ROSE:
        disegna_rosa_petali(x + ox, y + oy, s, c, tempo * 0.4)

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
