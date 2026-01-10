/* 
   Professional Asymptote Header 
   Standards: Olympiad Math Archive
*/

settings.outformat = "pdf";
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

// PROBLEM: zadaca_4
unit// size removed
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
dot(O);