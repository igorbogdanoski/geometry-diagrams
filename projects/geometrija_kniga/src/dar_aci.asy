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

// PROBLEM: dar_aci
unit// size removed
point O = (0,0);
point A = 1.5*dir(20);
point B = 1.5*dir(70);
draw(O -- A, Arrow(TeXHead));
draw(O -- B, Arrow(TeXHead));
markangle("$\alpha$", A, O, B, radius=0.4cm, filltype=UnFill(1mm));
dot(O);