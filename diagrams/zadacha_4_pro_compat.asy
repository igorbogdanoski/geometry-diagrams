import geometry;
import markers;

// Compatibility settings for Web/Limited environments
settings.outformat = "pdf";
settings.tex = "none"; 

unitsize(1cm);
dotfactor = 4;
defaultpen(linewidth(0.8pt));

// Construction
point O = (0,0);
real x = 18;
pair A = dir(0) * 3;
pair B = dir(90) * 3;
pair C = dir(3*x) * 3;
pair D = dir(3*x - 90) * 3;

// Drawing
draw(O--A, black + linewidth(1pt));
draw(O--B, black + linewidth(1pt));
draw(O--C, black + linewidth(1pt));
draw(O--D, black + linewidth(1pt));

// Markers
markrightangle(A, O, B, size=0.3cm);
markrightangle(C, O, D, size=0.3cm);

markangle(n=1, A, O, C, radius=0.7cm, p=red);
markangle(n=1, B, O, D, radius=1cm, p=blue);

// Labels (Simple strings for maximum compatibility)
dot(O); label("O", O, SW);
label("A", A, E);
label("B", B, N);
label("C", C, NE);
label("D", D, SE);

// Annotation
label("Problem 4 (x=18)", (0,-4));
