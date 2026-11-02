// Exemple pédagogique en millimètres. Adapter les paramètres avant usinage.
layer("Contour");
let contour = rect(0, 0, 100, 70);
layer("Poche");
let poche = rect(20, 20, 80, 50);
let ilot = circle(50, 35, 6);
layer("Percage");
let trous = [circle(10, 10, 2), circle(90, 10, 2), circle(90, 60, 2), circle(10, 60, 2)];
layer("Gravure");
let texte = text("FabLabCAM", 22, 7, 6);
tool("Fraise 3 mm", 3);
drill_tool("Foret 4 mm", 4);
pocket("Poche avec ilot", [poche, ilot], "Fraise 3 mm", -2);
drill("Quatre trous", trous, "Foret 4 mm", -4);
engrave("Marquage", texte, "Fraise 3 mm", -0.3);
profile("Contour exterieur", contour, "Fraise 3 mm", -4);
print("Plaque creee : quatre operations a verifier avant export.");
