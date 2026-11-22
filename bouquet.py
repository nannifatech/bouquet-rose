import tkinter as tk
import math
import random

# Finestra
root = tk.Tk()
root.title("Bouquet di Rose di Numeri")
root.geometry("800x700")
root.configure(bg="#1a0f1a")
canvas = tk.Canvas(root, width=800, height=700, bg="#1a0f1a", highlightthickness=0)
canvas.pack()

# Colori per le rose - rosso, rosa, viola, arancione
COLORI_ROSE = ["#ff2d55", "#ff6b9d", "#ff3b30", "#ff9500", "#c86bff", "#ff4d6d"]

# Ogni rosa: x, y, dimensione, colore, velocità, fase
rose = []
for i in range(7):
    rose.append({
        "x": 180 + (i % 3) * 190 + random.randint(-30, 30),
        "y": 180 + (i // 3) * 140 + random.randint(-20, 20),
        "size": random.randint(55, 75),
        "colore": random.choice(COLORI_ROSE),
        "velocita": random.uniform(0.02, 0.05),
        "fase": random.uniform(0, 6.28),
        "rotazione": random.uniform(0, 6.28)
    })

tempo = 0

def disegna_rosa(x, y, size, colore, rotazione, tempo):
    # Spirale di numeri che forma la rosa
    # Più vai verso il centro, più i numeri sono piccoli e fitti
    for r in range(size, 5, -6):
        # Quanti numeri in questo anello
        n_numeri = int(r / 4) + 4
        for i in range(n_numeri):
            angolo = (i / n_numeri) * 2 * math.pi + rotazione + (size - r) * 0.15
            px = x + math.cos(angolo) * r
            py = y + math.sin(angolo) * r * 0.9
            
            # Numero casuale ma stabile per posizione
            numero = (i * 7 + int(r) + int(tempo*2)) % 10
            
            # Dimensione font: più grande fuori, più piccolo dentro
            font_size = int(10 + r * 0.18)
            
            # Sfumatura: centro più chiaro
            canvas.create_text(px, py, text=str(numero), 
                               fill=colore, 
                               font=("Courier", font_size, "bold"))
    # Centro della rosa
    canvas.create_text(x, y, text=str(random.randint(0,9)), 
                       fill="#ffe0e6", font=("Courier", 16, "bold"))

def disegna_stelo(x, y):
    # Stelo verde fatto di numeri verdi che scendono
    for i in range(25):
        py = y + 50 + i * 8
        px = x + math.sin(tempo * 0.5 + i * 0.2) * 3
        canvas.create_text(px, py, text=str(random.randint(0,9)),
                           fill="#2ecc71", font=("Courier", 9, "bold"))

def anima():
    global tempo
    tempo += 0.05
    canvas.delete("all")
    
    # Sfondo di numeri che cadono
    for _ in range(15):
        sx = random.randint(0, 800)
        sy = random.randint(0, 700)
        canvas.create_text(sx, sy, text=str(random.randint(0,9)),
                           fill="#3a2a3a", font=("Courier", 12))
    
    # Disegna ogni rosa con movimento di oscillazione
    for r in rose:
        # Movimento a onda: oscilla a destra e sinistra
        offset_x = math.sin(tempo + r["fase"]) * 12
        offset_y = math.cos(tempo * 0.7 + r["fase"]) * 6
        rot = r["rotazione"] + tempo * r["velocita"] * 10
        
        disegna_stelo(r["x"] + offset_x, r["y"] + offset_y)
        disegna_rosa(r["x"] + offset_x, r["y"] + offset_y, 
                      r["size"], r["colore"], rot, tempo)
    
    # Fiocco del bouquet - fatto di numeri
    for i in range(30):
        px = 400 + (i-15)*12
        py = 560 + abs(i-15)*3
        canvas.create_text(px, py, text=str(i%10),
                           fill="#ffcc00", font=("Courier", 14, "bold"))
    
    canvas.create_text(400, 640, text="BOUQUET DI NUMERI",
                       fill="white", font=("Arial", 20, "bold"))
    
    root.after(50, anima)

anima()
root.mainloop()
