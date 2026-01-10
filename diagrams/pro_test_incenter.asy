/* 
   Professional Asymptote Header 
   Standards: Olympiad Math Archive
*/

settings.outformat = "pdf";
settings.prc = false;

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
  return pt + dist*unit(currentprojection.camera - (currentprojection.infinity ? O : pt));
}

// Label Masking Styling
filltype label_mask = Fill(white);

// --- Construction: Triangle Incenter Construction ---
point O = (0,0);

pair A = (0, 4);
pair B = (-2, 0);
pair C = (5, 0);
triangle t = triangle(A, B, C);
pair I = incenter(t);
circle inc = incircle(t);


// --- Drawing ---

draw(t, black + linewidth(1.2pt));
draw(inc, blue + dashed);
dot(I, red);


// --- Labels ---

label("$A$", A, N, label_mask);
label("$B$", B, SW, label_mask);
label("$C$", C, SE, label_mask);
label("$I$", I, S, label_mask);

