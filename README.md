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
| 2028-01-30 | Agudeza visual — banderas Código Internacional de Señales Marítimas | 99274 | FinAno2020.png | Nieves, Enric, Ari, Alex | PDTE |
| 2028-02-24 | Adivina quién soy | DIONISIO | Gerard_20220805.png | Gerard | PDTE |
| 2028-03-08 | Cultura: iniciales de famosos, especial mujeres | JAMAICA | Lugar02_01.jpg .. Lugar02_07.jpg | Ajenos | PDTE |
| 2028-11-24 | Ingenio: negro sobre negro | 300.000 | The_Rolling_Stones_Paint_It_Black.mp3 | N/A | PDTE |
