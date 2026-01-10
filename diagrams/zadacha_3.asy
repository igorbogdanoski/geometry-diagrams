settings.outformat = "pdf";
defaultpen(linewidth(1pt));
import geometry;

size(200, 200);

// Главни точки на конструкцијата
point O = (0,0);
point C = (-80, 0); // Паралелно со земјата
point A = 80*dir(230);
point B = 80*dir(50); // A, O, B се колинеарни
point D = 80*dir(310); // m(AOC) = m(AOD)

// Цртање на линиите (Source)
draw(C--O, black+linewidth(1.5pt));
draw(A--B, black+linewidth(1.5pt));
draw(O--D, black+linewidth(1.5pt));

// Помошна линија за земја (паралелна)
draw(shift(0,-20)*(-100,0--100,0), gray+dashed);

// Лабели
label("$C$", C, W);
label("$O$", O, NE);
label("$A$", A, SW);
label("$B$", B, NE);
label("$D$", D, SE);

// Означување на еднакви агли m(AOC) = m(AOD)
markangle(n=1, C, O, A, radius=15, p=red, StickIntervalMarker(1,1));
markangle(n=1, A, O, D, radius=15, p=red, StickIntervalMarker(1,1));

// Означување на BOC = 130 степени
markangle("$130^\circ$", B, O, C, radius=25, p=blue);

dot(O);