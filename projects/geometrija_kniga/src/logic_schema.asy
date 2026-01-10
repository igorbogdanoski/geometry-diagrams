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

// PROBLEM: logic_schema
// ANALYSIS: Angle transformations diagram
path curlybrace(pair a, pair b, real amplitude=0.3) {
    pair mid = (a + b) / 2;
    pair v = unit(b - a);
    pair n = (v.y, -v.x);
    pair p2 = mid + amplitude * n;
    return a .. (a + 0.2*v + 0.2*n) .. p2 .. (b - 0.2*v + 0.2*n) .. b;
}
unitsize(1cm);
draw(shift(0,2)*rotate(90)*Label("\{", position=Relative(0.5)), (0,2.5)--(2,2.5), p=magenta+linewidth(1.5pt));
draw((2.5, 2.7)--(3.5, 2.7), Arrow(TeXHead));
draw(shift(4,2)*rotate(90)*Label("\{", position=Relative(0.5)), (4,2.5)--(5.5,2.5), p=magenta+linewidth(1.5pt));
draw(shift(0,0.5)*rotate(90)*Label("\{", position=Relative(0.5)), (0,1)--(2,1), p=magenta+linewidth(1.5pt));
draw((2.5, 1.2)--(3.5, 1.2), Arrow(TeXHead));
draw(shift(4,0.5)*rotate(90)*Label("\{", position=Relative(0.5)), (4,1)--(5.5,1), p=magenta+linewidth(1.5pt));