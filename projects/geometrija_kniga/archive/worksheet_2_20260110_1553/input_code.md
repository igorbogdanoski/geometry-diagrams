### 1. Логичка шема (Брејс)
```asy
// PROBLEM: logic_schema
// ANALYSIS: Angle transformations diagram
path curlybrace(pair a, pair b, real amplitude=0.3) {
    pair mid = (a + b) / 2;
    pair v = unit(b - a);
    pair n = (v.y, -v.x);
    pair p2 = mid + amplitude * n;
    return a .. (a + 0.2*v + 0.2*n) .. p2 .. (b - 0.2*v + 0.2*n) .. b;
}
unitsize(1cm);
draw(shift(0,2)*Label("{", position=Relative(0.5), rotate(90)), (0,2.5)--(2,2.5), p=magenta+linewidth(1.5pt));
draw((2.5, 2.7)--(3.5, 2.7), Arrow(TeXHead));
draw(shift(4,2)*Label("{", position=Relative(0.5), rotate(90)), (4,2.5)--(5.5,2.5), p=magenta+linewidth(1.5pt));
draw(shift(0,0.5)*Label("{", position=Relative(0.5), rotate(90)), (0,1)--(2,1), p=magenta+linewidth(1.5pt));
draw((2.5, 1.2)--(3.5, 1.2), Arrow(TeXHead));
draw(shift(4,0.5)*Label("{", position=Relative(0.5), rotate(90)), (4,1)--(5.5,1), p=magenta+linewidth(1.5pt));
```

### 2. Дијаграм со симболи
```asy
// PROBLEM: symbols_diagram
unitsize(1cm);
path tri = polygon(3);
path square = unitsquare;
path star = (0,1)--(0.2,0.3)--(1,0.3)--(0.4,-0.1)--(0.6,-0.8)--(0,-0.4)--(-0.6,-0.8)--(-0.4,-0.1)--(-1,0.3)--(-0.2,0.3)--cycle;
fill(shift(3, 5)*scale(0.3)*rotate(180)*tri, palegreen); 
draw(shift(3, 5)*scale(0.3)*rotate(180)*tri, black);
fill(shift(4, 5)*scale(0.15)*star, pink);
draw(shift(4, 5)*scale(0.15)*star, black);
fill(shift(5, 4.85)*scale(0.3)*square, palecyan);
draw(shift(5, 4.85)*scale(0.3)*square, black);
draw((2, 4)--(2.8, 4), Arrow(TeXHead)); 
draw((3.2, 4)--(4.2, 4), Arrows(TeXHead), cyan); 
draw((4.8, 4)--(5.8, 4), Arrows(TeXHead), heavygreen); 
fill(shift(3, 1)*scale(0.2)*rotate(180)*tri, palegreen);
fill(shift(3.8, 0.9)*scale(0.3)*square, palecyan);
fill(shift(4.6, 1)*scale(0.3)*unitcircle, orange);
fill(shift(5.4, 1)*scale(0.15)*star, pink);
```

### 3. Задача 3: Пресметки
```asy
// PROBLEM: calculations_symbols
unitsize(1.2cm);
pair P1 = (0,2);
pair P2 = (2,2);
pair P3 = (4,2);
fill(shift(P1)*scale(0.3)*rotate(180)*polygon(3), palegreen);
label("$50^\circ$", P1, S, UnFill(1mm));
draw(P1+(0.5,0)--P2+(-0.5,0), Arrow(TeXHead));
fill(shift(P2)*scale(0.3)*unitsquare, palecyan);
fill(shift(P3)*scale(0.3)*unitsquare, palecyan);
label("$80^\circ$", P3, S, UnFill(1mm));
draw(P3+(0.5,0)--(5,2), Arrow(TeXHead));
fill(shift(5.5,2)*scale(0.3)*unitcircle, orange);
fill(shift(1,-1)*scale(0.3)*rotate(180)*polygon(3), palegreen);
label("$+$", (1.7, -1));
fill(shift(2.5,-1)*scale(0.3)*unitsquare, palecyan);
label("$+$", (3.2, -1));
fill(shift(4,-1)*scale(0.15)* ( (0,1)--(0.2,0.3)--(1,0.3)--(0.4,-0.1)--(0.6,-0.8)--(0,-0.4)--(-0.6,-0.8)--(-0.4,-0.1)--(-1,0.3)--(-0.2,0.3)--cycle ), pink);
```
