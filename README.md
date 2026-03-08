# 🎉 Calendario de 50 Aniversario — 2028/2029

## Estructura
```
calendario-50-aniversario/
├── index.html
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

## Pendiente de añadir
- Contenido de los retos de cada día (en `content-area` de cada página)
- Recompensas de cada día (en el popup `reward-text` de cada página)
