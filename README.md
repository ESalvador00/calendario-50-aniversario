# 🎉 Calendario de 50 Aniversario — 2028/2029

## Estructura
```
calendario-50-aniversario/
├── index.html
└── dias/
    ├── 2028-01-11.html  ← primer día clickable
    ├── ...
    ├── 2028-12-31.html
    ├── 2029-01-01.html
    └── 2029-01-10.html  ← último día clickable
```

## Reglas del calendario
- **Enero 2028, días 1–10:** ocultos (no linkables)
- **Enero 2029, días 11–31:** ocultos (no linkables)
- **Días pasados:** apagados, no clickables
- **Hoy:** círculo dorado con animación de pulso
- **Días futuros:** clickables pero muestran popup "¡No seas impaciente!"
- **Favoritos:** corazón ♡/❤ en cada página, se refleja en el index

---

## 🔓 Modo Preview (para pruebas)

El modo preview desactiva el bloqueo de días futuros y permite navegar
todo el calendario libremente sin popups.

**Contraseña:** `UNLOCK`

### Activar modo preview
Abre el calendario en el navegador y añade `?preview=UNLOCK` a la URL:
```
https://TU_USUARIO.github.io/calendario-50-aniversario/?preview=UNLOCK
```
Verás el badge 🔓 **Modo preview activo** bajo el título.
A partir de ese momento, aunque cierres y vuelvas a abrir, el modo
preview sigue activo (se guarda en el navegador).

### Desactivar modo preview
Añade `?preview=off` a la URL:
```
https://TU_USUARIO.github.io/calendario-50-aniversario/?preview=off
```
El badge desaparece y el comportamiento normal (con popups) se restaura.

### Probar en local (archivo abierto directamente)
```
file:///ruta/al/proyecto/index.html?preview=UNLOCK   ← activar
file:///ruta/al/proyecto/index.html?preview=off      ← desactivar
```

---

## Despliegue en GitHub Pages
Settings → Pages → Branch: main / root → Save
URL: `https://TU_USUARIO.github.io/calendario-50-aniversario/`
