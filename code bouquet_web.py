# Crea una pagina web con le rose di numeri
html = open("bouquet.html", "w")
html.write("""
<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
body{background:#1a0f1a; margin:0; overflow:hidden}
canvas{display:block}
</style></head><body>
<canvas id="c"></canvas>
<script>
let canvas = document.getElementById("c");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
let ctx = canvas.getContext("2d");
let rose = [];
let colori = ["#ff2d55","#ff6b9d","#ff3b30","#ff9500","#c86bff"];
for(let i=0;i<7;i++){
  rose.push({
    x: 150 + (i%3)*250,
    y: 180 + Math.floor(i/3)*200,
    size: 70,
    colore: colori[i%colori.length],
    fase: Math.random()*6
  });
}
let t=0;
function disegna(){
  ctx.clearRect(0,0,canvas.width,canvas.height);
  t+=0.05;
  rose.forEach(r=>{
    let ox = Math.sin(t + r.fase)*12;
    let oy = Math.cos(t*0.7 + r.fase)*6;
    // stelo di numeri verdi
    ctx.fillStyle="#2ecc71";
    ctx.font="12px Courier";
    for(let i=0;i<20;i++){
      ctx.fillText(Math.floor(Math.random()*10), r.x+ox, r.y+oy+60+i*10);
    }
    // rosa di numeri
    for(let rad=r.size; rad>5; rad-=6){
      let n = Math.floor(rad/4)+4;
      for(let i=0;i<n;i++){
        let ang = (i/n)*Math.PI*2 + t*0.5 + (r.size-rad)*0.15;
        let px = r.x+ox + Math.cos(ang)*rad;
        let py = r.y+oy + Math.sin(ang)*rad*0.9;
        ctx.fillStyle=r.colore;
        ctx.font = `bold ${10+rad*0.18}px Courier`;
        ctx.fillText(Math.floor(Math.random()*10), px, py);
      }
    }
  });
  requestAnimationFrame(disegna);
}
disegna();
</script></body></html>
""")
html.close()
print("Fatto! Ora apri bouquet.html")
