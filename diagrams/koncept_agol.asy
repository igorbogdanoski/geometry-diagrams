settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

size(200, 150);

// Точки според Source
point B = (0,0);
point C = (100, 0);
point A = 100*dir(-60);
point D = 80*dir(-25);

// Цртање зраци со стрелки (Source)
draw(B--C, Arrow(TeXHead));
draw(B--A, Arrow(TeXHead));
draw(B--D, dashed+blue, Arrow(TeXHead)); // Испрекината линија (симетрала)

// Лабели
label("$B$", B, NW);
label("$C$", C, E);
label("$A$", A, S);
label("$D$", D, E);

// Означување агли со точки (Source)
markangle(n=1, C, O=B, D, radius=20, p=red, marker(scale(0.5)*unitcircle, Fill));
markangle(n=1, D, O=B, A, radius=20, p=red, marker(scale(0.5)*unitcircle, Fill));

dot(B);