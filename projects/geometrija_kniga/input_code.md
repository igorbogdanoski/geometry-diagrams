### 1. Тесен агол (Dar açı)
```asy
// PROBLEM: dar_aci
unitsize(1.5cm);
point O = (0,0);
point A = 1.5*dir(20);
point B = 1.5*dir(70);
draw(O -- A, Arrow(TeXHead));
draw(O -- B, Arrow(TeXHead));
markangle("$\alpha$", A, O, B, radius=0.4cm, filltype=UnFill(1mm));
dot(O, dotfactor=4);
```

### 2. Прав агол (Dik açı)
```asy
// PROBLEM: dik_aci
unitsize(1.5cm);
point O = (0,0);
point A = (1.5,0);
point B = (0,1.5);
draw(O -- A, Arrow(TeXHead));
draw(O -- B, Arrow(TeXHead));
perpendicularmark(line(O,A), line(O,B), quarter=1, size=0.3cm);
dot(dir(45)*0.2); 
dot(O, dotfactor=4);
```

### 3. Тап агол (Geniş açı)
```asy
// PROBLEM: genis_aci
unitsize(1.5cm);
point O = (0,0);
point A = 1.5*dir(0);
point B = 1.5*dir(110);
draw(O -- A, Arrow(TeXHead));
draw(O -- B, Arrow(TeXHead));
markangle("$\alpha$", A, O, B, radius=0.4cm, filltype=UnFill(1mm));
dot(O, dotfactor=4);
```

### 5. Рамен агол (Doğru açı)
```asy
// PROBLEM: dogru_aci
unitsize(1.5cm);
point O = (0,0);
point L = (-1.5,0);
point R = (1.5,0);
draw(L -- R, Arrows(TeXHead));
path a = arc(O, 0.4, 180, 360);
draw(a);
label("$180^\circ$", (0, -0.4), S, UnFill(1mm));
dot(O, dotfactor=4);
```

### 4. Полн агол (Tam açı)
```asy
// PROBLEM: tam_aci
unitsize(1.5cm);
point O = (0,0);
point A = (1.2,0);
path c = circle(O, 0.7);
draw(O -- A, Arrow(TeXHead));
draw(c, Arrow(TeXHead));
label("$360^\circ$", (0.7, 0.7), NE, UnFill(1mm));
dot(O, dotfactor=4);
```

### 6. Задача 4: Систем на вкрстени нормали
```asy
// PROBLEM: zadaca_4
unitsize(1.5cm);
point O = (0,0);
point B = dir(0);
point A = dir(90);
point C = dir(-40);
point D = dir(50); 
draw(O -- 1.8*A, Arrow(TeXHead));
draw(O -- 1.8*B, Arrow(TeXHead));
draw(O -- 1.8*C, Arrow(TeXHead));
draw(O -- 1.8*D, Arrow(TeXHead));
perpendicularmark(line(O,A), line(O,B), quarter=1, size=0.2cm);
perpendicularmark(line(O,C), line(O,D), quarter=1, size=0.2cm);
markangle("$3x$", B, O, C, radius=0.6cm, filltype=UnFill(1mm));
markangle("$7x$", D, O, A, radius=0.8cm, filltype=UnFill(1mm));
label("$O$", O, SW, UnFill(1mm));
label("$A$", 1.8*A, N, UnFill(1mm));
label("$B$", 1.8*B, E, UnFill(1mm));
label("$C$", 1.8*C, SE, UnFill(1mm));
label("$D$", 1.8*D, NE, UnFill(1mm));
dot(O, dotfactor=4);
```
