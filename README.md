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
| 2028-01-12 | Sigue la letra | La flaca (Jarabe de Palo) | La_flaca.mp3 | N/A | PDTE |
| 2028-01-14 | Adivina las películas | Dirty Dancing, Frozen, La Mision, Los Cazafantasmas, Matrix | Dirty_Dancing, Frozen, La_Mision, Los_Cazafantasmas, Matrix (mp3 y jpg) | N/A | PDTE |
| 2028-01-17 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-01-19 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-01-21 | Cultura: iniciales de famosos | CORCEGA | Lugar01_01.jpg .. Lugar01_07.jpg | Ajenos | PDTE |
| 2028-01-22 | Minijuego (Mastermind) | N/A | N/A | N/A | PDTE |
| 2028-01-24 | Adivina quién soy | HEIMDALL | Alex_20220817.png | Alex | PDTE |
| 2028-01-26 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-01-28 | Timeline histórico doble | A:01-06 / B:01-06 | Timeline01_01A..06A.png + Timeline01_01B..06B.png | N/A | PDTE |
| 2028-01-30 | Agudeza visual — banderas Código Internacional de Señales Marítimas | 99274 | FinAno2020.png | Nieves, Enric, Ari, Alex | PDTE |
| 2028-02-01 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-02-02 | Cultura: iniciales de famosos, especial cine | QUEBEC | Lugar06_01.jpg .. Lugar06_06.jpg | Ajenos | PDTE |
| 2028-02-03 | Puzzle visual | ALEX | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2028-02-05 | Minijuego (Ranas Saltadoras) | N/A | N/A | N/A | PDTE |
| 2028-02-06 | Agudeza visual — clickmap museo (binario) | ENRIC | Museo_visual.png + Museo_clickmap.png + Ultima_cena.png + Ariadna_20190701.png | Ariadna | PDTE |
| 2028-02-09 | Timeline musical, España en los 2000 | 2002-2008 | Asereje.jpg .. Tenia_tanto_que_darte.jpg | N/A | PDTE |
| 2028-02-18 | Adivina las películas | Regreso al Futuro, ET El Extraterrestre, Mision Imposible, Toy Story, Alien El octavo pasajero | Regreso_al_Futuro, ET_El_Extraterrestre, Mision_Imposible, Toy_Story, Alien_El_octavo_pasajero (mp3 y jpg) | N/A | PDTE |
| 2028-02-20 | Palabras Intraducibles - Japonés | IKIGAI | NievesAriAlex_20160406.jpg | Nieves, Ariadna y Alexandra | PDTE |
| 2028-02-21 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-02-22 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-02-24 | Adivina quién soy | DIONISIO | David_20220805.png | David | PDTE |
| 2028-02-26 | Escape Room: 01-El archivo secreto | ENIGMA | ER01_EscenarioVisual.jpg + ER01_EscenarioClickmap.jpg | N/A | PDTE |
| 2028-02-28 | Sigue la letra | Llamando a la Tierra (M-Clan) | Llamando_a_la_Tierra.mp3 | N/A | PDTE |
| 2028-03-03 | Adivina las películas | Amelie, El Guardaespaldas, Ghost, Oppenheimer, Sherlock Holmes | Amelie, El_Guardaespaldas, Ghost, Oppenheimer, Sherlock_Holmes (mp3 y jpg) | N/A | PDTE |
| 2028-03-04 | Minijuego (Simón Dice) | N/A | N/A | N/A | PDTE |
| 2028-03-06 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-03-07 | Puzzle visual | AFI | Puzzle02_01.png .. Puzzle02_04.png | N/A | PDTE |
| 2028-03-08 | Cultura: iniciales de famosos, especial mujeres | JAMAICA | Lugar02_01.jpg .. Lugar02_07.jpg | Ajenos | PDTE |
| 2028-03-12 | Agudeza visual — cifrado César | PLATANO | Alex_20191006.png | Alex | PDTE |
| 2028-03-13 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-03-14 | Sigue la letra | Sin ti no soy nada (Amaral) | Sin_ti_no_soy_nada.mp3 | N/A | PDTE |
| 2028-03-15 | Adivina quién soy | AGATHA CHRISTIE | Mari_20220819.png | Mari | PDTE |
| 2028-03-26 | Palabras Intraducibles - Brasileño | CAFUNE | NievesAri_20210817.png | Nieves y Ariadna | PDTE |
| 2028-03-28 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-04-08 | Minijuego (El Lobo, la Cabra y la Col) | N/A | N/A | N/A | PDTE |
| 2028-04-10 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-04-11 | Adivina quién soy | DALI | Ari_20130601.png | Ariadna | PDTE |
| 2028-04-12 | Sigue la letra | No dudaría (Antonio Flores) | No_dudaria.mp3 | N/A | PDTE |
| 2028-04-16 | Agudeza visual — clickmap museo (coordenadas hex) | CHAD | Museo2_visual.png + Museo2_clickmap.png + Cuadros_verdes.png + Ariadna_20190601.png | Ariadna | PDTE |
| 2028-04-17 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-04-18 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-04-19 | Cultura: iniciales de famosos, especial política | MADEIRA | Lugar07_01.jpg .. Lugar07_07.jpg | Ajenos | PDTE |
| 2028-04-27 | Puzzle visual | ECF | Puzzle03_01.png .. Puzzle03_02.png | N/A | PDTE |
| 2028-04-28 | Adivina las películas | El Rey León, Titanic, Piratas del Caribe, Forrest Gump, Braveheart | El_Rey_Leon, Titanic, Piratas_del_Caribe, Forrest_Gump, Braveheart (mp3 y jpg) | N/A | PDTE |
| 2028-05-06 | Minijuego (Las 5 Monedas de Tait) | N/A | N/A | N/A | PDTE |
| 2028-05-08 | Adivina quién soy | VOLDEMORT | Alex_20200222.png | Alex | PDTE |
| 2028-05-09 | Timeline musical, España en los 80 | 1980-1987 | No_dudaria.jpg .. Hijo_de_la_luna.jpg | N/A | PDTE |
| 2028-05-13 | Satisfacción con restricciones múltiples | Enric: negra+manta / Nieves: roja+cámara / Ariadna: azul+auriculares / Alex: verde+consola | RSR05_Escenario.webp + RSR05_01A..01D.png + RSR05_02A..02D.png | Enric, Nieves, Ariadna, Alex | PDTE |
| 2028-05-14 | Palabras Intraducibles - Japonés | BOKETTO | Enric_20220816.png | Enric | PDTE |
| 2028-05-16 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-05-17 | Sigue la letra | La chispa adecuada (Héroes del Silencio) | La_chispa_adecuada.mp3 | N/A | PDTE |
| 2028-05-22 | Cultura: iniciales de famosos | CAPRI | Lugar08_01.jpg .. Lugar08_05.jpg | Ajenos | PDTE |
| 2028-05-23 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-05-24 | Puzzle visual | ARI | Puzzle04_01.png .. Puzzle04_07.png | N/A | PDTE |
| 2028-05-26 | Adivina las películas | Fiebre del Sábado Noche, Jurassic Park, Coco, Gladiator, Pulp Fiction | Fiebre_del_Sabado_Noche, Jurassic_Park, Coco, Gladiator, Pulp_Fiction (mp3 y jpg) | N/A | PDTE |
| 2028-05-29 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-06-01 | Puzzle visual | ACHI | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2028-06-03 | Minijuego (La Balanza Falsa) | N/A | N/A | N/A | PDTE |
| 2028-06-05 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-06-06 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-06-11 | Agudeza visual — Fibonacci | 1597 | Alex_20170807.png | Alex | PDTE |
| 2028-06-12 | Sigue la letra | Voy en un coche (Christina y Los Subterráneos) | Voy_en_un_coche.mp3 | N/A | PDTE |
| 2028-06-14 | Cultura: iniciales de famosos | OKINAWA | Lugar03_01.jpg .. Lugar03_07.jpg | Ajenos | PDTE |
| 2028-06-15 | Adivina quién soy | TESLA | Gerard_20160205.png | Gerard | PDTE |
| 2028-06-16 | Adivina las películas | Flashdance, El Señor de los Anillos, Batman, Up, Cinema Paradiso | Flashdance, El_Senor_de_los_Anillos, Batman, Up, Cinema_Paradiso (mp3 y jpg) | N/A | PDTE |
| 2028-06-18 | Escape Room: 02-Sala de Control Nuclear | SOLES | ER02_EscenarioVisual.jpg + ER02_EscenarioClickmap.jpg | N/A | PDTE |
| 2028-06-19 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-07-03 | Puzzle visual | ACHI | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2028-07-04 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-07-08 | Minijuego (La Puerta de los Glifos) | N/A | N/A | N/A | PDTE |
| 2028-07-10 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-07-11 | Timeline histórico doble | A:01-06 / B:01-06 | Timeline02_01A..06A.png + Timeline02_01B..06B.png | N/A | PDTE |
| 2028-07-12 | Adivina quién soy | POE | David_20231209.png | David | PDTE |
| 2028-07-16 | Agudeza visual — Elementos químicos | BRUSELAS | Alex_20231027.png | Alex | PDTE |
| 2028-07-18 | Cultura: iniciales de famosos | HAWAII | Lugar09_01.jpg .. Lugar09_06.jpg | Ajenos | PDTE |
| 2028-07-19 | Sigue la letra | Vino tinto (Estopa) | Vino_tinto.mp3 | N/A | PDTE |
| 2028-07-21 | Adivina las películas | Superman, Grease, La Sirenita, Indiana Jones, American Beauty | Superman, Grease, La_Sirenita, Indiana_Jones, American_Beauty (mp3 y jpg) | N/A | PDTE |
| 2028-07-23 | Palabras Intraducibles - Alemán | SEHNSUCHT | AriAlex_20170611.jpg | Ariadna y Alex | PDTE |
| 2028-07-24 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-07-28 | Timeline musical, España en los 90 | 1990-1999 | Entre_dos_tierras.jpg .. Tu_calorro.jpg | N/A | PDTE |
| 2028-08-01 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-08-02 | Puzzle visual | ACHI | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2028-08-07 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-08-11 | Adivina las películas | La Bella y la Bestia, Solo en Casa, Halloween, Top Gun, El Caballero Oscuro | La_Bella_y_la_Bestia, Solo_en_Casa, Halloween, Top_Gun, El_Caballero_Oscuro (mp3 y jpg) | N/A | PDTE |
| 2028-08-17 | Adivina quién soy | NAPOLEON | Juan_20190813.png | Juan | PDTE |
| 2028-08-20 | Palabras Intraducibles - Tagalo | GIGIL | Alex_20140531.png | Alex | PDTE |
| 2028-08-21 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-08-23 | Sigue la letra | Hijo de la luna (Mecano) | Hijo_de_la_luna.mp3 | N/A | PDTE |
| 2028-08-26 | Minijuego (Las Jarras de Agua) | N/A | N/A | N/A | PDTE |
| 2028-08-30 | Cultura: iniciales de famosos | MALLORCA | Lugar10_01.jpg .. Lugar10_08.jpg | Ajenos | PDTE |
| 2028-09-03 | Palabras Intraducibles - Finlandés | SISU | Nieves_20160102.jpg | Nieves | PDTE |
| 2028-09-04 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-09-05 | Puzzle visual | ACHI | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2028-09-09 | Minijuego (El Cruce del Puente) | N/A | N/A | N/A | PDTE |
| 2028-09-12 | Adivina quién soy | MARY SHELLEY | Cristina_20130713.png | Cristina | PDTE |
| 2028-09-18 | Cultura: iniciales de famosos, especial música | BORNEO | Lugar04_01.jpg .. Lugar04_06.jpg | Ajenos | PDTE |
| 2028-09-20 | Sigue la letra | Ella (Viceversa) | Ella.mp3 | N/A | PDTE |
| 2028-09-22 | Adivina las películas | Pesadilla antes de Navidad, La La Land, El Último Mohicano, The Pianist, Inside Out | Pesadilla_antes_de_Navidad, La_La_Land, El_Ultimo_Mohicano, The_Pianist, Inside_Out (mp3 y jpg) | N/A | PDTE |
| 2028-09-25 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-09-26 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-10-02 | Puzzle visual | ACHI | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2028-10-03 | Cultura: iniciales de famosos | CRETA | Lugar11_01.jpg .. Lugar11_05.jpg | Ajenos | PDTE |
| 2028-10-08 | Escape Room: 03-Laboratorio Alquímico | Esencia Pura | ER03_EscenarioVisual.jpg + ER03_EscenarioClickmap.jpg | N/A | PDTE |
| 2028-10-09 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-10-10 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-10-16 | Sigue la letra | Chiquilla (Seguridad Social) | Chiquilla.mp3 | N/A | PDTE |
| 2028-10-18 | Timeline musical, Internacional en los 90 | 1990-1999 | Ice_ice_baby.jpg, Losing_my_religion.jpg, Zombie.jpg, Wannabe.jpg, Baby_one_more_time.jpg, Genie_in_a_Bottle.jpg + .mp3 | N/A | PDTE |
| 2028-10-20 | Adivina las películas | Rocky, Harry Potter, Aladdin, Superdetective en Hollywood, Karate Kid | Rocky, Harry_Potter, Aladdin, Superdetective_en_Hollywood, Karate_Kid (mp3 y jpg) | N/A | PDTE |
| 2028-10-22 | Palabras Intraducibles - Griego | MERAKI | Cumple_20170211.jpg | Nieves, Ariadna y Alex | PDTE |
| 2028-10-23 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-10-24 | Adivina quién soy | GOYA | Enric_20110101.png | Enric | PDTE |
| 2028-10-28 | Minijuego (Reparto de Combustible) | N/A | N/A | N/A | PDTE |
| 2028-11-06 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-11-07 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-11-10 | Adivina las películas | Armageddon, Fama, Los Increíbles, La historia interminable, Los Goonies | Armageddon, Fama, Los_Increibles, La_historia_interminable, Los_Goonies (mp3 y jpg) | N/A | PDTE |
| 2028-11-13 | Sigue la letra | Voy a pasármelo bien (Hombres G) | Voy_a_pasarmelo_bien.mp3 | N/A | PDTE |
| 2028-11-14 | Adivina quién soy | ELEVEN | Ari_20220701.png | Ariadna | PDTE |
| 2028-11-18 | Minijuego (El Triángulo Girado) | N/A | N/A | N/A | PDTE |
| 2028-11-19 | Palabras Intraducibles - Yiddish | NAKHES | Alex_20250622.jpg | Alexandra | PDTE |
| 2028-11-20 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-11-21 | Cultura: iniciales de famosos | MALTA | Lugar12_01.jpg .. Lugar12_05.jpg | Ajenos | PDTE |
| 2028-11-22 | Puzzle visual | ACHI | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2028-11-24 | Ingenio: negro sobre negro | 300.000 | The_Rolling_Stones_Paint_It_Black.mp3 | N/A | PDTE |
| 2028-12-05 | Laberinto Invisible | N/A | N/A | N/A | PDTE |
| 2028-12-07 | Puzzle visual | ACHI | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2028-12-09 | Satisfacción con restricciones múltiples | Enric: ajedrez+frutos secos / Nieves: cartas+patatas / Ariadna: puzle+galletas / Alex: dominó+gominolas | RSR12_Escenario.webp + RSR12_01A..01D.png + RSR12_02A..02D.png | Enric, Nieves, Ariadna, Alex | PDTE |
| 2028-12-11 | Sigue la letra | Cuéntame un cuento (Celtas Cortos) | Cuentame_un_cuento.mp3 | N/A | PDTE |
| 2028-12-13 | Adivina quién soy | DARTH VADER | Enric_20130227.png | Enric | PDTE |
| 2028-12-15 | Adivina las películas | Sister Act, Beetlejuice, Reservoir Dogs, El resplandor, Jumanji | Sister_Act, Beetlejuice, Reservoir_Dogs, El_resplandor, Jumanji (mp3 y jpg) | N/A | PDTE |
| 2028-12-18 | Rosco de pasapalabra | N/A | N/A | N/A | PDTE |
| 2028-12-19 | Cultura: iniciales de famosos, especial deporte | ONTARIO | Lugar05_01.jpg .. Lugar05_07.jpg | Ajenos | PDTE |
| 2028-12-20 | Adivina el logo correcto | 10 logos icónicos | Logos.png | N/A | PDTE |
| 2028-12-23 | Minijuego (La Torre de Hanoi) | N/A | N/A | N/A | PDTE |
| 2029-01-02 | Puzzle visual | ACHI | Puzzle01_01.png .. Puzzle01_05.png | N/A | PDTE |
| 2029-01-03 | Timeline musical, Internacional en los 2000 | 2000-2009 | Music.jpg, Complicated.jpg, Hey_Ya.jpg, Crazy.jpg, Umbrella.jpg, I_Gotta_Feeling.jpg + .mp3 | N/A | PDTE |


---

## Utilidades

### Descargar audio desde YouTube a MP3
- **yoump3.app** → https://yoump3.app/es11
  Permite convertir y descargar cualquier vídeo de YouTube como archivo MP3.
  Útil para obtener los audios de las canciones usadas en los días de tipo "Timeline musical".

### Obtener carátulas de películas
- **IMDb** → https://www.imdb.com/es/?ref_=tt_nv_home
  Buscar la película, descargar el póster oficial desde la ficha.
  Recortar la imagen a proporción **2:3** antes de guardarla en `/media`.
---

## ✅ TO-DO — Temas pendientes

|  Día / Ámbito | Descripción | Estado |
|--------------|-------------|--------|
|  Logos icónicos (×9 días) | Rellenar contenido de: 2028-01-17, 2028-02-01, 2028-04-10, 2028-06-05, 2028-08-07, 2028-09-04, 2028-10-09, 2028-11-06, 2028-12-20 | 🔲 Pdte |
|  Puzzle visuales | OK: 03-FEB, 07-MAR, 27-ABR, 24-MAY | 🔲 Pdte |
|  Pasapalabra (×12 meses) | Completar los restos de letras para los 12 meses del calendario | 🔲 Pdte |
|  Laberinto invisible (×12 meses) | Definir y actualizar el laberinto | 🔲 Pdte |
|  Escape Rooms + Retos de observación | Añadir música ambiental de fondo en los días tipo Escape Room y en los retos de agudeza visual | 🔲 Pdte |
