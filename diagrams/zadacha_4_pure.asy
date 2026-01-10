/* 
   Professional Asymptote Header 
   Standards: Olympiad Math Archive
*/

settings.outformat = "pdf";
settings.prc = false;
settings.render = 16;
settings.resample = true;

// Preamble for Macedonian Cyrillic support
texpreamble("\usepackage[utf8]{inputenc}");
texpreamble("\usepackage[T2A]{fontenc}");
texpreamble("\usepackage[macedonian]{babel}");

// Professional Modules
import graph;
import geometry;
import markers;

// Scale and Pen Standards
unitsize(1cm);
real truecm = cm / 1; // Base unit 1cm
dotfactor = 4;
defaultpen(linewidth(0.8pt) + fontsize(10pt));

// Utility Functions
triple towardcamera(triple pt, real dist=1) {
  return pt + dist*unit(currentprojection.camera - (currentprojection.infinity ? (0,0,0) : pt));
}

// Label Masking Styling
filltype label_mask = Fill(white);

// --- Construction: Задача 4 - Агли помеѓу четири полуправи ---
point O = (0,0);

// Пресметка: 3x + 90 - 3x + 7x = 180 (бидејќи OA perp OB и OC perp OD)
// Резултат: x = 18
real x = 18;
real angleA = 0;
real angleB = 90;
real angleC = 3*x; // 54 degrees
real angleD = angleC - 90; // -36 degrees (или 324)

pair A = dir(angleA) * 3;
pair B = dir(angleB) * 3;
pair C = dir(angleC) * 3;
pair D = dir(angleD) * 3;


// --- Drawing ---

draw(O--A, black + linewidth(1pt));
draw(O--B, black + linewidth(1pt));
draw(O--C, black + linewidth(1pt));
draw(O--D, black + linewidth(1pt));

markrightangle(A, O, B, size=0.3cm);
markrightangle(C, O, D, size=0.3cm);

markangle("$3x^\circ$", A, O, C, radius=0.7cm, p=red);
markangle("$7x^\circ$", B, O, D, radius=1cm, p=blue);


// --- Labels ---

dot(O); label("$O$", O, SW, label_mask);
label("$A$", A, E, label_mask);
label("$B$", B, N, label_mask);
label("$C$", C, NE, label_mask);
label("$D$", D, SE, label_mask);

