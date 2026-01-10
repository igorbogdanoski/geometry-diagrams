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

// PROBLEM: symbols_diagram
unitsize(1cm);
path tri = polygon(3);
path square = unitsquare;
path star = (0,1)--(0.2,0.3)--(1,0.3)--(0.4,-0.1)--(0.6,-0.8)--(0,-0.4)--(-0.6,-0.8)--(-0.4,-0.1)--(-1,0.3)--(-0.2,0.3)--cycle;
fill(shift(3, 5)*scale(0.3)*rotate(180)*tri, palegreen); 
draw(shift(3, 5)*scale(0.3)*rotate(180)*tri, black);
fill(shift(4, 5)*scale(0.15)*star, pink);
draw(shift(4, 5)*scale(0.15)*star, black);
fill(shift(5, 4.85)*scale(0.3)*square, palecyan);
draw(shift(5, 4.85)*scale(0.3)*square, black);
draw((2, 4)--(2.8, 4), Arrow(TeXHead)); 
draw((3.2, 4)--(4.2, 4), cyan, Arrows(TeXHead)); 
draw((4.8, 4)--(5.8, 4), heavygreen, Arrows(TeXHead)); 
fill(shift(3, 1)*scale(0.2)*rotate(180)*tri, palegreen);
fill(shift(3.8, 0.9)*scale(0.3)*square, palecyan);
fill(shift(4.6, 1)*scale(0.3)*unitcircle, orange);
fill(shift(5.4, 1)*scale(0.15)*star, pink);