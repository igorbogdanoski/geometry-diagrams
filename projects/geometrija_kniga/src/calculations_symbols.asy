/* 
   Professional Asymptote Header 
   Standards: Olympiad Math Archive
*/

// settings.outformat = "pdf";
settings.prc = false;
settings.render = 16;

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