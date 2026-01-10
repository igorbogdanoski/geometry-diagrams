// Test SVG output
settings.outformat = "svg";
size(200);
draw((0,0)--(1,0)--(1,1)--(0,1)--cycle, blue);
dot((0.5,0.5), red);
label("$Test$", (0.5,0.5));