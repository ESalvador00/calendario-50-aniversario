#!/usr/bin/env python3
"""Generates all 366 individual day pages for the 2028 50th Anniversary Calendar."""

import os
from datetime import date, timedelta

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "dias")
os.makedirs(OUTPUT_DIR, exist_ok=True)

MONTHS_ES = [
    "Enero","Febrero","Marzo","Abril","Mayo","Junio",
    "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"
]
DAYS_ES = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

start = date(2028, 1, 1)
end   = date(2028, 12, 31)
delta = timedelta(days=1)

TEMPLATE = """\
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — 50 Aniversario 2028</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400&family=Cormorant+Garamond:wght@300;400;500&display=swap" rel="stylesheet">
  <style>
    :root {
      --gold: #C9A84C;
      --gold-light: #E8C97A;
      --gold-dark: #8B6914;
      --cream: #FAF6EE;
      --dark: #1A1410;
    }
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background-color: var(--dark);
      color: var(--cream);
      font-family: 'Cormorant Garamond', serif;
      min-height: 100vh;
      display: flex; flex-direction: column;
    }
    body::before {
      content: '';
      position: fixed; inset: 0;
      background:
        radial-gradient(ellipse at 25% 15%, rgba(201,168,76,0.10) 0%, transparent 55%),
        radial-gradient(ellipse at 75% 85%, rgba(124,54,38,0.10) 0%, transparent 55%);
      pointer-events: none; z-index: 0;
    }
    .wrap {
      position: relative; z-index: 1;
      max-width: 800px; margin: 0 auto;
      padding: 3rem 2rem 4rem;
      flex: 1; display: flex; flex-direction: column;
    }
    .day-hero {
      text-align: center;
      flex: 1;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      padding: 3rem 0 2rem;
    }
    .ornament-line-h {
      display: flex; align-items: center; justify-content: center; gap: 1rem;
      margin-bottom: 2rem;
    }
    .o-line { height: 1px; width: 60px; background: linear-gradient(to right, transparent, var(--gold)); }
    .o-line.r { background: linear-gradient(to left, transparent, var(--gold)); }
    .o-dot { width: 5px; height: 5px; background: var(--gold); border-radius: 50%; }
    .day-of-week {
      font-size: 0.85rem; letter-spacing: 0.4em;
      text-transform: uppercase; color: rgba(201,168,76,0.5);
      margin-bottom: 1rem;
    }
    h1 {
      font-family: 'Playfair Display', serif;
      font-size: clamp(3rem, 9vw, 7rem);
      font-weight: 900; line-height: 1;
      background: linear-gradient(135deg, var(--gold-light) 0%, var(--gold) 50%, var(--gold-dark) 100%);
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 0.5rem;
    }
    .month-label {
      font-family: 'Playfair Display', serif;
      font-size: clamp(1.4rem, 3.5vw, 2.4rem);
      font-weight: 400; font-style: italic;
      color: rgba(250,246,238,0.45);
      margin-bottom: 2.5rem;
    }
    .content-area {
      width: 100%;
      border: 1px solid rgba(201,168,76,0.15);
      border-radius: 4px;
      padding: 2.5rem;
      min-height: 220px;
      background: rgba(255,255,255,0.02);
      color: rgba(250,246,238,0.4);
      font-size: 1rem;
      font-style: italic;
      text-align: center;
      display: flex; align-items: center; justify-content: center;
    }
    .day-nav {
      display: flex; justify-content: space-between; align-items: center;
      padding-top: 2.5rem;
      border-top: 1px solid rgba(201,168,76,0.1);
      margin-top: 2.5rem;
    }
    .nav-btn {
      font-size: 0.8rem; letter-spacing: 0.15em; text-transform: uppercase;
      color: rgba(201,168,76,0.5); text-decoration: none;
      padding: 0.6rem 1.2rem;
      border: 1px solid rgba(201,168,76,0.18);
      border-radius: 2px;
      transition: all 0.2s;
    }
    .nav-btn:hover { color: var(--gold-light); border-color: rgba(201,168,76,0.5); background: rgba(201,168,76,0.05); }
    .nav-btn.disabled { opacity: 0; pointer-events: none; }
    .year-badge {
      font-size: 0.7rem; letter-spacing: 0.3em;
      color: rgba(201,168,76,0.25); text-transform: uppercase;
    }
    .back-link {
      display: block; text-align: center;
      margin-top: 2rem;
      color: rgba(201,168,76,0.35);
      font-size: 0.75rem; letter-spacing: 0.25em; text-transform: uppercase;
      text-decoration: none;
      transition: color 0.2s;
    }
    .back-link:hover { color: var(--gold); }
  </style>
</head>
<body>
<div class="wrap">

  <div class="day-hero">
    <div class="ornament-line-h">
      <div class="o-line"></div><div class="o-dot"></div><div class="o-line r"></div>
    </div>
    <p class="day-of-week">{day_name}</p>
    <h1>{day_num}</h1>
    <p class="month-label">de {month_name}</p>
    <div class="content-area">
      <p>Espacio reservado para el contenido de este día</p>
    </div>
  </div>

  <nav class="day-nav">
    {prev_link}
    <span class="year-badge">50 Aniversario · 2028</span>
    {next_link}
  </nav>

  <a class="back-link" href="../index.html">&#8592; Volver al Calendario</a>

</div>
</body>
</html>
"""

current = start
total = 0

while current <= end:
    month_name = MONTHS_ES[current.month - 1]
    day_name   = DAYS_ES[current.weekday()]
    day_num    = current.day
    month_num  = current.month

    title = f"{day_num} de {month_name}"
    slug  = f"{month_num:02d}-{day_num:02d}.html"
    filepath = os.path.join(OUTPUT_DIR, slug)

    prev_date = current - delta
    next_date = current + delta

    def nav_href(d):
        if d.year != 2028:
            return None
        return f"{d.month:02d}-{d.day:02d}.html"

    prev_href = nav_href(prev_date)
    next_href = nav_href(next_date)

    prev_label = f"{prev_date.day} de {MONTHS_ES[prev_date.month-1]}" if prev_href else ""
    next_label = f"{next_date.day} de {MONTHS_ES[next_date.month-1]}" if next_href else ""

    prev_link = f'<a class="nav-btn" href="{prev_href}">&#8592; {prev_label}</a>' if prev_href else '<span class="nav-btn disabled"></span>'
    next_link = f'<a class="nav-btn" href="{next_href}">{next_label} &#8594;</a>' if next_href else '<span class="nav-btn disabled"></span>'

    html = TEMPLATE.format(
        title=title,
        day_name=day_name,
        day_num=day_num,
        month_name=month_name,
        prev_link=prev_link,
        next_link=next_link,
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    total += 1
    current += delta

print(f"Generated {total} day pages in '{OUTPUT_DIR}'")
