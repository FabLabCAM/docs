// Vérification avec FabLabCAM 0.6.1 ou plus récent : échec attendu.
let id = circle(0, 0, 2);
delete(id + 4294967296);
