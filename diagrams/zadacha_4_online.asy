// Professional version for online testing
settings.prc = false;
defaultpen(linewidth(1pt) + fontsize(10pt));
import geometry;

dotfactor = 4;
size(250);

point O = (0, 0);

real len = 4;
pair A = O + len * dir(0);
pair B = O + len * dir(90);
pair C = O + len * dir(54);
pair D = O + len * dir(324);

draw(O--A, black + linewidth(1.2pt));
draw(O--B, black + linewidth(1.2pt));
draw(O--C, black + linewidth(1.2pt));
draw(O--D, black + linewidth(1.2pt));

markrightangle(A, O, B, size=0.25cm);
markrightangle(C, O, D, size=0.25cm);

markangle("$3x°$", n=1, A, O, C, radius=35, p=red, StickIntervalMarker(1,2,size=4));
markangle("$7x°$", n=1, B, O, D, radius=35, p=blue, StickIntervalMarker(1,2,size=4));

dot(O); label("$O$", O, SW, UnFill(1mm));
dot(A); label("$A$", A, E, UnFill(1mm));
dot(B); label("$B$", B, N, UnFill(1mm));
dot(C); label("$C$", C, NE, UnFill(1mm));
dot(D); label("$D$", D, NW, UnFill(1mm));

// Simplified problem description
label("Problem 4: Four rays from O with perpendicular pairs", (0, -2), S, UnFill);