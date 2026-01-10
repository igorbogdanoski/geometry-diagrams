if(!settings.multipleView) settings.batchView=false;
settings.tex="pdflatex";
defaultfilename="test_zadacha_4-1";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

import geometry;
import markers;

unitsize(1cm);
dotfactor = 4;
defaultpen(linewidth(0.8pt) + fontsize(10pt));

point O = (0,0);
real x = 18;
real angleA = 0;
real angleB = 90;
real angleC = 3*x;
real angleD = angleC - 90;

pair A = dir(angleA) * 3;
pair B = dir(angleB) * 3;
pair C = dir(angleC) * 3;
pair D = dir(angleD) * 3;

draw(O--A, black + linewidth(1pt));
draw(O--B, black + linewidth(1pt));
draw(O--C, black + linewidth(1pt));
draw(O--D, black + linewidth(1pt));

markrightangle(A, O, B, size=0.3cm);
markrightangle(C, O, D, size=0.3cm);

markangle("$3x^\circ$", A, O, C, radius=0.7cm, p=red);
markangle("$7x^\circ$", B, O, D, radius=1cm, p=blue);

dot(O); label("$O$", O, SW, filltype=Fill(white));
label("$A$", A, E, filltype=Fill(white));
label("$B$", B, N, filltype=Fill(white));
label("$C$", C, NE, filltype=Fill(white));
label("$D$", D, SE, filltype=Fill(white));
