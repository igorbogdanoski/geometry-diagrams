// PREAMBLE
settings.outformat = "pdf";
settings.prc = false;
settings.render = 16;
import geometry;

// Professional styling for consistent textbook look
defaultpen(linewidth(0.8pt) + fontsize(10pt));
texpreamble("\usepackage{amsmath}");

// 1. SETUP & SCALE
unitsize(1.5cm);

// 2. DEFINITIONS
pair O = (0,0);
real len = 1.2; // Length of rays

// Define direction vectors based on calculated geometry for precision
pair dirA = dir(180);
pair dirB = dir(90);
pair dirC = dir(36);  // 90 - 54
pair dirD = dir(-54); // 36 - 90

// Define endpoints for drawing
pair pA = O + len * dirA;
pair pB = O + len * dirB;
pair pC = O + len * dirC;
pair pD = O + len * dirD;

// 3. DRAWING RAYS
draw(O--pA, Arrow(TeXHead));
draw(O--pB, Arrow(TeXHead));
draw(O--pC, Arrow(TeXHead));
draw(O--pD, Arrow(TeXHead));

// 4. MARKERS & DECORATIONS
// Right Angle between OA and OB
perpendicularmark(line(O, pA), line(O, pB), size=0.2cm, quarter=1, filltype=Fill(lightgray));

// Right Angle between OC and OD
perpendicularmark(line(O, pD), line(O, pC), size=0.2cm, quarter=1, filltype=Fill(lightgray));

// Dots at specific points
real dot_dist = 0.9 * len;
dot(O, linewidth(4pt));
dot(O + dot_dist * dirA, linewidth(4pt));
dot(O + dot_dist * dirB, linewidth(4pt));
dot(O + dot_dist * dirC, linewidth(4pt));
dot(O + dot_dist * dirD, linewidth(4pt));

// 5. LABELS
label("$O$", O, SW + S*0.2, filltype=UnFill(1mm));
label("$A$", O + dot_dist * dirA, N);
label("$B$", O + dot_dist * dirB, E);
label("$C$", O + dot_dist * dirC, SE);
label("$D$", O + dot_dist * dirD, SW);
