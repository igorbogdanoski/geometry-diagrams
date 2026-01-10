settings.outformat = "pdf";
settings.prc = false; 
import geometry;

// Professional configuration from the guide
unitsize(1.5cm);
dotfactor = 4;
defaultpen(linewidth(0.8pt) + fontsize(10pt));

// Point O at origin
point O = (0, 0);

// Ray directions - mathematically precise using unitsize
real len = 3; 
path rayA = O -- (O + len * dir(0));
path rayB = O -- (O + len * dir(90));
path rayC = O -- (O + len * dir(54));
path rayD = O -- (O + len * dir(324));

// Draw rays
draw(rayA, black + linewidth(1pt));
draw(rayB, black + linewidth(1pt));
draw(rayC, black + linewidth(1pt));
draw(rayD, black + linewidth(1pt));

// Right angle markers (Group 5)
markrightangle(point(rayA, 1), O, point(rayB, 1), size=0.3cm);
markrightangle(point(rayC, 1), O, point(rayD, 1), size=0.3cm);

// Angle markings
markangle(n=1, point(rayA, 1), O, point(rayC, 1), radius=0.8cm, p=red);
markangle(n=1, point(rayB, 1), O, point(rayD, 1), radius=0.9cm, p=blue);

// Dots at key points
dot(O);
dot(point(rayA, 1));
dot(point(rayB, 1));
dot(point(rayC, 1));
dot(point(rayD, 1));

// Note: Labels are currently disabled due to system limitations
// label("$O$", O, SW); 
