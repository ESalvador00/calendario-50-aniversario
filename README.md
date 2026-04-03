# 🎉 Calendario de 50 Aniversario — 2028/2029

## Estructura
```
calendario-50-aniversario/
├── index.html
├── media/              ← imágenes, vídeos, audios usados en los días
│   ├── *.png / *.jpg
│   ├── *.mp4 / *.webm
│   └── *.mp3 / *.ogg
└── dias/
    ├── 2028-01-11.html  ← primer día
    ├── ...
    ├── 2028-12-31.html
    └── 2029-01-10.html  ← último día
```

366 días en total (del 11 de enero de 2028 al 10 de enero de 2029).

---

## Funcionalidades

### Calendario principal (`index.html`)
- **Hoy:** círculo dorado con animación de pulso
- **Días pasados:** visibles y clickables
- **Días futuros:** clickables pero muestran popup "¡No seas impaciente!"
- **Días desarrollados:** punto verde 🟢 en la esquina superior izquierda de la celda

#### Indicador de días desarrollados (punto verde)
El `index.html` marca visualmente los días que ya tienen contenido implementado mediante un pequeño punto verde en la esquina superior izquierda de su celda.

**Cómo funciona:** el array `DEV_DAYS` en el JS del `index.html` contiene las fechas desarrolladas. Cada celda que coincide recibe la clase CSS `.dev`, que activa el punto mediante `::after`.

**Para desactivarlo** cuando ya no sea necesario, basta con comentar una sola línea en el CSS del `index.html`:
```css
/* DEV MARKER — comentar la línea siguiente para ocultar los indicadores */
/* .day-cell.dev::after{...} */
```

**Para añadir un nuevo día** al marcador, agregar su fecha al array `DEV_DAYS` en el JS:
```javascript
const DEV_DAYS = new Set([
  '2028-01-21', '2028-01-24', // ... etc
  '2028-XX-XX'  // ← añadir aquí
]);
```

### Páginas de cada día
Cada día tiene dos iconos en la esquina superior derecha:

- **♡ / ❤ Favorito** — se puede marcar y desmarcar libremente. El corazón rojo aparece también en el calendario principal.
- **☆ / ★ Completado** — indica que se ha superado el reto del día:
  - Sin completar → popup "¡Tu recompensa te espera! Primero debes resolver el desafío..."
  - Ya completado → popup con la recompensa del día
  - Solo se puede marcar en **modo preview** (ver más abajo)

---

## 🔓 Modo Preview (para pruebas)

El modo preview desactiva el bloqueo de días futuros y permite navegar
todo el calendario libremente, además de marcar días como completados.

**Contraseña:** `UNLOCK`

### Activar
```
https://esalvador00.github.io/calendario-50-aniversario/?preview=UNLOCK
```
Aparece el badge 🔓 **Modo preview activo** bajo el título.
El modo se guarda en el navegador, no hace falta añadirlo cada vez.

### Desactivar
```
https://esalvador00.github.io/calendario-50-aniversario/?preview=off
```

### En local (archivo abierto directamente)
```
file:///ruta/al/proyecto/index.html?preview=UNLOCK   ← activar
file:///ruta/al/proyecto/index.html?preview=off      ← desactivar
```

---

## Despliegue en GitHub Pages

1. Subir el contenido del ZIP a un repositorio en GitHub
2. Settings → Pages → Branch: **main** / root → **Save**
3. URL pública:

```
https://esalvador00.github.io/calendario-50-aniversario/
```

---

## Sistema de pistas

Cada página de día puede tener N pistas (el número varía según el día). Se implementan con bolitas de colores debajo del campo de código:

- 🔴 **Rojo** — pista bloqueada, no clickable
- 🟡 **Ámbar** — pista disponible, clickable (pulsa para verla)
- 🟢 **Verde** — pista ya vista, se puede releer

**Comportamiento:** al cargar la página siempre se reinicia — solo la primera bolita está en ámbar. Cada vez que se cierra el popup de una pista, esa bolita se vuelve verde y la siguiente pasa a ámbar.

### Cómo añadir/editar las pistas de un día

En el JS de cada página busca el array `PISTAS` y añade o edita las cadenas de texto:

```javascript
const PISTAS = [
  'Texto de la pista 1...',
  'Texto de la pista 2...',
  'Texto de la pista 3...',
  // tantas como quieras
];
```

Las bolitas del HTML deben coincidir en número con las entradas del array. Ajusta el bloque HTML de las bolitas según las pistas que tenga ese día:

```html
<!-- 3 pistas -->
<div class="pistas-wrap">
  <div class="pista-dot ambar" id="pista-1">1</div>
  <div class="pista-dot rojo"  id="pista-2">2</div>
  <div class="pista-dot rojo"  id="pista-3">3</div>
</div>
```

Y actualiza el array `dotIds` en el JS para que coincida:

```javascript
const dotIds = ['pista-1','pista-2','pista-3'];
let pistaEstado = [1, 0, 0]; // tantos 0 como pistas extra tras la primera
```

---

## Resumen de días con contenido

| Día | Reto | Clave | Media | Actores | Recompensa |
|-----|------|-------|-------|---------|------------|
| 2028-01-21 | Cultura: iniciales de famosos | CORCEGA | Lugar01_01.jpg .. Lugar01_07.jpg | Ajenos | PDTE |
| 2028-01-24 | Adivina quién soy | HEIMDALL | Alex_20220817.png | Alex | PDTE |
| 2028-01-28 | Timeline histórico doble | A:01-06 / B:01-06 | Timeline01_01A..06A.png + Timeline01_01B..06B.png | N/A | PDTE |
| 2028-01-30 | Agudeza visual — banderas Código Internacional de Señales Marítimas | 99274 | FinAno2020.png | Nieves, Enric, Ari, Alex | PDTE |
| 2028-02-06 | Agudeza visual — clickmap museo (binario) | ENRIC | Museo_visual.png + Museo_clickmap.png + Ultima_cena.png + Ariadna_20190701.png | Ariadna | PDTE |
| 2028-02-09 | Timeline musical, España en los 2000 | 2002-2008 | Asereje.jpg .. Tenia_tanto_que_darte.jpg | N/A | PDTE |
| 2028-02-24 | Adivina quién soy | DIONISIO | David_20220805.png | David | PDTE |
| 2028-03-15 | Adivina quién soy | AGATHA CHRISTIE | Mari_20220819.png | Mari | PDTE |
| 2028-03-08 | Cultura: iniciales de famosos, especial mujeres | JAMAICA | Lugar02_01.jpg .. Lugar02_07.jpg | Ajenos | PDTE |
| 2028-04-11 | Adivina quién soy | DALÍ | Ari_20130601.png | Ariadna | PDTE |
| 2028-05-08 | Adivina quién soy | VOLDEMORT | Alex_20200222.png | Alex | PDTE |
| 2028-05-09 | Timeline musical, España en los 80 | 1980-1987 | No_dudaria.jpg .. Hijo_de_la_luna.jpg | N/A | PDTE |
| 2028-06-14 | Cultura: iniciales de famosos | OKINAWA | Lugar03_01.jpg .. Lugar03_07.jpg | Ajenos | PDTE |
| 2028-06-15 | Adivina quién soy | TESLA | Gerard_20160205.png | Gerard | PDTE |
| 2028-07-11 | Timeline histórico doble | A:01-06 / B:01-06 | Timeline02_01A..06A.png + Timeline02_01B..06B.png | N/A | PDTE |
| 2028-07-12 | Adivina quién soy | POE | David_20231209.png | David | PDTE |
| 2028-07-28 | Timeline musical, España en los 90 | 1990-1999 | Entre_dos_tierras.jpg .. Tu_calorro.jpg | N/A | PDTE |
| 2028-08-17 | Adivina quién soy | NAPOLEÓN | Juan_20190813.png | Juan | PDTE |
| 2028-10-18 | Timeline musical, Internacional en los 90 | 1990-1999 | Ice_ice_baby.jpg, Losing_my_religion.jpg, Zombie.jpg, Wannabe.jpg, Baby_one_more_time.jpg, Genie_in_a_Bottle.jpg + .mp3 | N/A | PDTE |
| 2028-11-24 | Ingenio: negro sobre negro | 300.000 | The_Rolling_Stones_Paint_It_Black.mp3 | N/A | PDTE |
| 2029-01-03 | Timeline musical, Internacional en los 2000 | 2000-2009 | Music.jpg, Complicated.jpg, Hey_Ya.jpg, Crazy.jpg, Umbrella.jpg, I_Gotta_Feeling.jpg + .mp3 | N/A | PDTE |

---

## Utilidades

### Descargar audio desde YouTube a MP3
- **yoump3.app** → https://yoump3.app/es11
  Permite convertir y descargar cualquier vídeo de YouTube como archivo MP3.
  Útil para obtener los audios de las canciones usadas en los días de tipo "Timeline musical".
