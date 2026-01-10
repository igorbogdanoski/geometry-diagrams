settings.outformat = "pdf";
settings.prc = false; // Better LaTeX compatibility
defaultpen(linewidth(1pt) + fontsize(10pt)); // LaTeX font consistency
import geometry;

// Professional dot sizing (Group 13)
dotfactor = 4;

// Canvas size for optimal display
size(250);

// Point O at origin
point O = (0, 0);

// Ray directions (angles in degrees) - mathematically precise
real len = 4; // Extended length for clarity
pair A = O + len * dir(0);   // 0° - x-axis
pair B = O + len * dir(90);  // 90° - y-axis
pair C = O + len * dir(54);  // 54° = 3×18°
pair D = O + len * dir(324); // 324° = 90° - 7×18°

// Draw rays with professional styling
draw(O--A, black + linewidth(1.2pt));
draw(O--B, black + linewidth(1.2pt));
draw(O--C, black + linewidth(1.2pt));
draw(O--D, black + linewidth(1.2pt));

// Right angle markers - automatic and precise (Group 5)
markrightangle(A, O, B, size=0.25cm);
markrightangle(C, O, D, size=0.25cm);

// Enhanced angle markings with markangle (Group 9)
markangle("$3x^\circ$", n=1, A, O, C, radius=35, p=red, StickIntervalMarker(1,2,size=4));
markangle("$7x^\circ$", n=1, B, O, D, radius=35, p=blue, StickIntervalMarker(1,2,size=4));

// Professional labels with UnFill masking (Group 6, 13)
dot(O); label("$O$", O, SW, UnFill(1mm));
dot(A); label("$A$", A, E, UnFill(1mm));
dot(B); label("$B$", B, N, UnFill(1mm));
dot(C); label("$C$", C, NE, UnFill(1mm));
dot(D); label("$D$", D, NW, UnFill(1mm));

// Add mathematical context with minipage (Group 11, 13)
label(minipage("\centering Задача 4:\\Во точката $O$ се спојуваат четири полуправи $OA, OB, OC, OD$.\\Познато е дека $OA \\perp OB$ и $OC \\perp OD$.\\Аглите: $\\angle AOC = 3x^\\circ$, $\\angle BOD = 7x^\\circ$.\\Одреди $x$ и аглите.", 6cm),
      (0, -2.5), UnFill);