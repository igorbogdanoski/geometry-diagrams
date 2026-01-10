settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

// Димензии на платното
size(200, 100);

// Дефинирање на точките на главната права
point O = (0,0);
point A = (-100, 0);
point F = (100, 0);

// Поставување на зраците според аглите од задачата
// OC и OD се под прав агол (90 степени)
point C = 80*dir(135);
point D = 80*dir(45);
point B = 80*dir(157.5); // Симетрала на AOC
point E = 80*dir(22.5);  // Симетрала на DOF

// Цртање на главната права и зраците
draw(A--F, black);
draw(O--B, black);
draw(O--C, black);
draw(O--D, black);
draw(O--E, black);

// Додавање ознаки за темињата (Source)
label("$A$", A, W);
label("$O$", O, S);
label("$F$", F, E);
label("$B$", B, NW);
label("$C$", C, N);
label("$D$", D, N);
label("$E$", E, NE);

// Означување на прав агол (Source)
perpendicularmark(line(O,C), line(O,D), size=0.2cm);

// Означување на еднакви агли (Симетрали) (Source)
// Агли означени со точки
markangle(n=1, C, O, B, radius=15, p=red, marker(scale(0.5)*unitcircle, Fill));
markangle(n=1, B, O, A, radius=15, p=red, marker(scale(0.5)*unitcircle, Fill));

// Агли означени со цртички
markangle(n=1, F, O, E, radius=15, p=blue, StickIntervalMarker(1,1,size=3));
markangle(n=1, E, O, D, radius=15, p=blue, StickIntervalMarker(1,1,size=3));

dot(O);