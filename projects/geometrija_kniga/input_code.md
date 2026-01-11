Врз основа на материјалите од „Karekök Sıfır Geometri 2023 15.pdf“ и професионалните стандарди за техничка илустрација дефинирани во изворите, ги подготвив следните Asymptote кодови за секоја поединечна илустрација.

Секој дијаграм е реконструиран со примена на „Законот на Жанет“ и техничките правила за маскирање на ознаки.

### 1. Систем на агли со складни делови (Горна илустрација)
Овој дијаграм прикажува симетричен распоред на зраци со ознаки за еднаквост и прав агол.

```asy
// PREAMBLE
settings.outformat = "pdf";
settings.prc = false;
import geometry;
defaultpen(linewidth(0.8pt) + fontsize(10pt));

// 1. SETUP & SCALE
unitsize(1.5cm);

// ANALYSIS:
// - Detected: Straight line with origin O.
// - Detected: Multiple rays from O.
// - Detected: Right angle marker in the center.
// - Detected: Congruence marks (dots on left, ticks on right).

// 2. DEFINITIONS (Law of Janet)
point O = (0,0);
point L = (-2,0);
point R = (2,0);
point A = 1.8*dir(155);
point B = 1.8*dir(130);
point C = 1.8*dir(50);
point D = 1.8*dir(25);

// 3. DRAWING
draw(L -- R, Arrows(TeXHead));
draw(O -- A, Arrow(TeXHead));
draw(O -- B, Arrow(TeXHead));
draw(O -- C, Arrow(TeXHead));
draw(O -- D, Arrow(TeXHead));

// 4. MARKERS & DECORATIONS
perpendicularmark(line(O,B), line(O,C), quarter=1, size=0.2cm);

// Angle markers with dots (left side)
markangle(n=1, radius=0.6cm, L, O, A);
markangle(n=1, radius=0.6cm, A, O, B);
dot(dir(167.5)*0.5); 
dot(dir(142.5)*0.5);

// Angle markers with ticks (right side)
markangle(n=1, radius=0.6cm, C, O, D);
markangle(n=1, radius=0.6cm, D, O, R);
add(StickIntervalMarker(1, 2, size=3pt, space=2pt).frame(arc(O, 0.6, 25, 50)));
add(StickIntervalMarker(1, 2, size=3pt, space=2pt).frame(arc(O, 0.6, 0, 25)));

// 5. POINTS
dot(O, dotfactor=4);
dot(L*0.8, dotfactor=4);
dot(R*0.8, dotfactor=4);
```

### 2. Концепт на симетрала (Açıortay)
Приказ на агол со испрекината линија како симетрала.

```asy
// PREAMBLE
settings.outformat = "pdf";
settings.prc = false;
import geometry;
defaultpen(linewidth(0.8pt) + fontsize(10pt));

// 1. SETUP & SCALE
unitsize(1.5cm);

// ANALYSIS:
// - Detected: Angle ABC.
// - Detected: Ray BD as angle bisector (dashed).
// - Detected: Angle marks with dots for congruence.

// 2. DEFINITIONS
point B = (0,0);
point C = (2,0);
point A = 2*dir(-60);
line bise = bisector(line(B,C), line(B,A));
point D = 2*dir(degrees(bise));

// 3. DRAWING
draw(B -- 2.5*C, Arrow(TeXHead));
draw(B -- 2.5*A, Arrow(TeXHead));
draw(B -- 2.5*D, dashed, Arrow(TeXHead));

// 4. MARKERS
markangle(n=1, radius=0.5cm, D, B, C);
markangle(n=1, radius=0.5cm, A, B, D);
dot(dir(-15)*0.4);
dot(dir(-45)*0.4);

// 5. LABELS
label("$B$", B, W, UnFill(1mm));
label("$C$", 2*C, N, UnFill(1mm));
label("$D$", 2*D, NE, UnFill(1mm));
label("$A$", 2*A, NW, UnFill(1mm));

dot(2*C, dotfactor=4);
dot(2*D, dotfactor=4);
dot(2*A, dotfactor=4);
```

### 3. Линеарен распоред со зрак (A, B, C doğrusal)
Илустрација на точка на права со дополнителен зрак.

```asy
// PREAMBLE
settings.outformat = "pdf";
settings.prc = false;
import geometry;
defaultpen(linewidth(0.8pt) + fontsize(10pt));

// 1. SETUP & SCALE
unitsize(1.5cm);

// ANALYSIS:
// - Detected: Line ABC.
// - Detected: Ray BD.

// 2. DEFINITIONS
point B = (0,0);
point A = (-1.5,0);
point C = (1.5,0);
point D = 1.5*dir(-40);

// 3. DRAWING
draw(1.8*A -- 1.8*C, Arrows(TeXHead));
draw(B -- 1.8*D, Arrow(TeXHead));

// 4. LABELS
label("$A$", A, N, UnFill(1mm));
label("$B$", B, N, UnFill(1mm));
label("$C$", C, N, UnFill(1mm));
label("$D$", D, W, UnFill(1mm));

dot(A, dotfactor=4);
dot(B, dotfactor=4);
dot(C, dotfactor=4);
dot(D, dotfactor=4);
```

### 4. Геометриски модел на закачалка (Задача 3)
Реконструкција на геометриските односи од илустрацијата со закачалката.

```asy
// PREAMBLE
settings.outformat = "pdf";
settings.prc = false;
import geometry;
defaultpen(linewidth(0.8pt) + fontsize(10pt));

// 1. SETUP & SCALE
unitsize(1.5cm);

// ANALYSIS:
// - Detected: Origin O.
// - Detected: Horizontal line (ground parallel).
// - Detected: Rays OA, OB, OD.
// - Detected: Angle mark 130 degrees.

// 2. DEFINITIONS
point O = (0,0);
point C = (1.5,0);
point B = 1.8*dir(-50); // m(BOC) = 130 reflected
point A = 1.8*dir(180);
point D = 1.8*dir(-130);

// 3. DRAWING
draw((-2,0) -- (2,0), linewidth(1.5pt) + gray); // Ground reference
draw(O -- 2*dir(110), linewidth(1pt)); 
draw(O -- 2*dir(70), linewidth(1pt));
draw(O -- 2*dir(-60), linewidth(1pt));

// 4. MARKERS
markangle("$130^\circ$", C, O, B, radius=0.4cm, filltype=UnFill(1mm));
perpendicularmark(line(O,C), line(O,(0,1)), size=0.2cm);

dot(O, dotfactor=4);
```

### 5. Решение на Köşetaşı 1.3
Комплексен систем на зраци со варијабли $a$ и $b$ за аглите.

```asy
// PREAMBLE
settings.outformat = "pdf";
settings.prc = false;
import geometry;
defaultpen(linewidth(0.8pt) + fontsize(10pt));

// 1. SETUP & SCALE
unitsize(1.5cm);

// ANALYSIS:
// - Detected: Straight line A-O-F.
// - Detected: Perpendicular rays OC and OD.
// - Detected: Bisectors OB and OE.
// - Detected: Variable labels a and b.

// 2. DEFINITIONS
point O = (0,0);
point A = (-2,0);
point F = (2,0);
point C = 1.8*dir(120);
point D = 1.8*dir(30); // OC perp OD
point B = 1.8*dir(150); // Bisects AOC
point E = 1.8*dir(15);  // Bisects DOF

// 3. DRAWING
draw(A -- F, Arrows(TeXHead));
draw(O -- C, Arrow(TeXHead));
draw(O -- D, Arrow(TeXHead));
draw(O -- B, Arrow(TeXHead));
draw(O -- E, Arrow(TeXHead));

// 4. MARKERS
perpendicularmark(line(O,C), line(O,D), quarter=1, size=0.2cm);

// Labels for variables
label("$b$", dir(165)*0.6, UnFill(1mm));
label("$b$", dir(135)*0.6, UnFill(1mm));
label("$a$", dir(45)*0.6, UnFill(1mm));
label("$a$", dir(10)*0.6, UnFill(1mm));

// 5. LABELS
label("$A$", A, S, UnFill(1mm));
label("$O$", O, S, UnFill(1mm));
label("$F$", F, S, UnFill(1mm));
label("$B$", B, NW, UnFill(1mm));
label("$C$", C, NW, UnFill(1mm));
label("$D$", D, NE, UnFill(1mm));
label("$E$", E, NE, UnFill(1mm));

dot(O, dotfactor=4);
```.