import tkinter as tk
import math
import random

root = tk.Tk()
root.title("Bouquet Vero")
root.geometry("800x750")
root.configure(bg="white")
canvas = tk.Canvas(root, width=800, height=750, bg="white", highlightthickness=0)
canvas.pack()

tempo = 0

# Posizioni delle rose come nella foto: a mazzo rotondo, vicine vicine
# (x, y, grandezza, colore)
POS_ROSE = [
    (400, 180, 85, "#ff8fb3"),  # centrale in alto
    (305, 230, 78, "#ff6b9d"),  # sinistra alta
    (495, 230, 78, "#ff8fb3"),  # destra alta
    (350, 310, 82, "#ff5c8a"),  # sinistra bassa
    (450, 310, 82, "#ff6b9d"),  # destra bassa
    (400, 270, 90, "#ffc0d5"),  # centrale davanti, la più grande
    (265, 295, 55, "#ff8fb3"),  # piccola lato sx
    (535, 295, 55, "#ff8fb3"),  # piccola lato dx
]

def disegna_rosa(x, y, size, colore, rot):
    # Spirale di numeri che fa la rosa, più fitta al centro
    for r in range(size, 4, -5):
        n = int(r / 3.5) + 5
        for i in range(n):
            ang = (i / n) * 2 * math.pi + rot + (size - r) * 0.22
            px = x + math.cos(ang) * r
            py = y + math.sin(ang) * r * 0.85
            num = (i * 3 + int(r) + int(tempo * 3)) % 10
            fs = int(8 + r * 0.16)
            canvas.create_text(px, py, text=str(num), fill=colore, font=("Courier", fs, "bold"))
    # Centro chiarissimo
    canvas.create_text(x, y, text=str(random.randint(0,9)), fill="#fff0f5", font=("Courier", 14, "bold"))

def disegna_verde():
    # Foglioline verdi intorno alle rose, come nella foto - numeri verdi piccoli
    for _ in range(120):
        # Posizioni a corona intorno al mazzo
        ang = random.uniform(0, 2*math.pi)
        dist = random.uniform(120, 210)
        px = 400 + math.cos(ang) * dist
        py = 250 + math.sin(ang) * dist * 0.75
        # Non disegnare sopra le rose centrali
        if 300 < px < 500 and 150 < py < 350:
            continue
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#2ecc71", font=("Courier", 10, "bold"))
        canvas.create_text(px+4, py+4, text=str(random.randint(0,9)), fill="#27ae60", font=("Courier", 8, "bold"))

def anima():
    global tempo
    tempo += 0.05
    canvas.delete("all")

    # 1. STELO che si stringe verso il basso (come nella foto)
    for i in range(40):
        py = 380 + i * 5
        # si stringe verso il centro
        larg = 60 - i * 1.2
        for k in range(5):
            px = 400 + random.uniform(-larg, larg) * (i/40)
            canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#2e9e5b", font=("Courier", 9, "bold"))

    # 2. CARTA / CONO del mazzo - due triangoli chiari
    # Lato sinistro della carta
    for i in range(60):
        px = random.uniform(220, 400)
        py = 380 + (400 - px) * 0.45 + random.uniform(-5, 5)
        if py < 600:
            canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#fde8f0", font=("Courier", 9))
    # Lato destro della carta
    for i in range(60):
        px = random.uniform(400, 580)
        py = 380 + (px - 400) * 0.45 + random.uniform(-5, 5)
        if py < 600:
            canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#fde8f0", font=("Courier", 9))

    # 3. VERDE intorno
    disegna_verde()

    # 4. ROSE - oscillano tutte insieme come un mazzo vero
    ox = math.sin(tempo) * 6
    oy = math.cos(tempo * 0.8) * 3
    for (x, y, s, c) in POS_ROSE:
        disegna_rosa(x + ox, y + oy, s, c, tempo * 0.4)

    # 5. FIOCCHETTO bianco/crema come nella foto
    # Nodo centrale
    for i in range(20):
        px = 400 + random.uniform(-15, 15)
        py = 570 + random.uniform(-10, 10)
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#fff5cc", font=("Courier", 12, "bold"))
    # Ali del fiocco a sinistra e destra
    for i in range(35):
        # sinistra
        px = 400 - 20 - i * 3
        py = 570 + math.sin(i*0.3) * 18
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#fff5cc", font=("Courier", 11, "bold"))
        # destra
        px = 400 + 20 + i * 3
        py = 570 + math.sin(i*0.3) * 18
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#fff5cc", font=("Courier", 11, "bold"))
    # Code del fiocco che scendono
    for i in range(25):
        px = 390 - i * 1.5
        py = 585 + i * 4
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#fff5cc", font=("Courier", 10, "bold"))
        px = 410 + i * 1.5
        py = 585 + i * 4
        canvas.create_text(px, py, text=str(random.randint(0,9)), fill="#fff5cc", font=("Courier", 10, "bold"))

    root.after(60, anima)

anima()
root.mainloop()
