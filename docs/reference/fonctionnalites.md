# Index des fonctionnalités et captures

Ce catalogue couvre les commandes exposées par le Studio 0.7.1 et les outils
complémentaires. Chaque lien ouvre une procédure ; la capture montre le panneau
réel de la famille concernée. Les capacités uniquement CLI sont documentées
par leur commande reproductible, sans inventer un écran qui n’existe pas.

| Famille | Fonctions documentées | Capture |
|---|---|---|
| [Assistant natif](../guide/assistant.md) | Ask, Plan, Agent, contexte choisi, aperçu, validation, annulation et quatre fournisseurs | [Voir](../assets/screenshots/50-assistant-meubles.png) |
| [Composition et assemblages](../guide/composer-meubles.md) | Arbre et vue de face, cases, bacs, épaisseurs, positions fixes/égales, huit familles, surcharges, schéma 2 et montages recto/verso | [Voir](../assets/screenshots/42-composition-structure.png) |
| [Meubles](../guide/meubles.md) | Modèles et projets, assistant, création/édition/duplication, historique, imports/exports JSON, placement, ZIP CB/DXF/SVG/CSV/PDF, passage en FAO | [Voir](../assets/screenshots/37-meubles-assistant.png) |
| [Fichiers](../guide/fichiers.md) | Nouveau, ouvrir, récents, enregistrer, enregistrer sous, import DXF/SVG, export CB/DXF/SVG, glisser-déposer, saisie par chemin | [Voir](../assets/screenshots/02-fichiers.png) |
| [Interface](../guide/interface.md) | Calques, visibilité, calque courant, sélection, propriétés, console, unités, magnétisme, cadrage et navigation | [Voir](../assets/screenshots/01-interface.png) |
| [Dessin](../guide/dessin.md) | Ligne, polyligne, rectangle, cercle, arc, sélection, copier/couper/coller et menu contextuel | [Voir](../assets/screenshots/03-dessin.png) |
| [Propriétés géométriques](../guide/objets.md) | Dimensions, coordonnées, rotation, rayon de coin, cercle, arc et conversion de rectangle | [Voir](../assets/screenshots/04-proprietes-rectangle.png) |
| [Sommets](../guide/objets.md) | Coordonnées, courbures, insertion, suppression, point de départ, ouvrir/fermer, inverser, nettoyer et poignées | [Voir](../assets/screenshots/21-sommets.png) |
| [Texte](../guide/texte.md) | Texte, hauteur, espacement, police système ou fichier, placement et vectorisation | [Voir](../assets/screenshots/06-texte.png) |
| [Transformations](../guide/transformations.md) | Déplacement, copie, rotation, échelle, miroirs, réseau rectangulaire/circulaire, décalages, rainure, division, arrondis, joindre/éclater, booléens | [Voir](../assets/screenshots/05-transformations.png) |
| [Table d’outils](../guide/outils.md) | Créer, renommer, numéroter, types, diamètre, dents, avances, broche, import de style XML | [Voir](../assets/screenshots/07-outils.png) |
| [Outils avancés et bibliothèque](../guide/outils.md) | Géométrie, limites, matière, revêtement, notes, changement G-code, suppression/remplacement et bibliothèque locale | [Voir](../assets/screenshots/09-outil-avance.png) |
| [Calculateur](../guide/calculateur.md) | Matière, Vc, fz, limite de broche, application des résultats à l’outil | [Voir](../assets/screenshots/08-calculateur.png) |
| [Opérations](../guide/operations.md) | Créer, activer, organiser par pièce, réordonner, dupliquer, supprimer et rattacher les formes | [Voir](../assets/screenshots/10-poche.png) |
| [Profil](../guide/profil.md) | Extérieur, intérieur, sur le trait et surépaisseur | [Voir](../assets/screenshots/13-profil.png) |
| [Ponts](../guide/profil.md) | Automatiques, extérieurs/intérieurs, manuels, dimensions, formes, nombres, distance et seuil | [Voir](../assets/screenshots/14-ponts.png) |
| [Poche](../guide/poche.md) | Contours, îlots, profondeur, incrément, pas latéral et matière laissée | [Voir](../assets/screenshots/10-poche.png) |
| [Perçage](../guide/percage.md) | Centres, outil, profondeur, temporisation ; picage et cycles via CLI | [Voir](../assets/screenshots/11-percage.png) |
| [Gravure](../guide/gravure.md) | Tracés ouverts/fermés, contours de texte et profondeur | [Voir](../assets/screenshots/12-gravure.png) |
| [Paramètres avancés](../guide/parametres.md) | Hauteurs, entrées, ordre des passes, finition, surcoupe, transitions, sens de broche, avances locales et G-code avant/après | [Voir](../assets/screenshots/15-passes-avances.png) |
| [Brut](../guide/simulation.md) | Automatique, limites manuelles et ajustement au trajet | [Voir](../assets/screenshots/18-brut.png) |
| [Vue 3D](../guide/simulation.md) | Matière usinée, trajectoires, rotation, zoom et cadrage | [Voir](../assets/screenshots/16-vue-3d.png) |
| [Simulation](../guide/simulation.md) | Lecture, pause, début, fin, curseur, maillage, volume et gouges | [Voir](../assets/screenshots/17-simulation.png) |
| [G-code et post-traitement](../guide/gcode.md) | Export NC, post-processeur intégré ou CBPP, contrôle, backplot et diagnostic Mach3 (mode IJ initial confirmé pour lyon3.v1, arcs dégénérés) | [Voir](../assets/screenshots/18-brut.png) |
| [Profils machine · Atelier](../guide/profils-studio.md) | Bibliothèque, création guidée, édition, duplication, import/export JSON, contrôles de configuration et protection des brouillons | [Voir](../assets/screenshots/29-profils-atelier.png) |
| [ID CNC PRO - Mach3](../guide/id-cnc-pro.md) | Modèle par défaut, initialisation d’une bibliothèque vide et création guidée préremplie | [Voir](../assets/screenshots/33-id-cnc-pro.png) |
| [Scripts](../reference/rhai.md) | Éditeur, ouverture, exécution, journal et API de projet | [Voir](../assets/screenshots/19-script.png) |
| [Préférences](../reference/raccourcis.md) | Magnétisme, pas, résolution, post-processeur et fichiers récents | [Voir](../assets/screenshots/20-preferences.png) |
| [Aide et raccourcis](../reference/raccourcis.md) | Aide intégrée, commandes clavier et console | [Voir](../assets/screenshots/22-aide.png) |

## Outils complémentaires

| Outil | Fonctions | Référence |
|---|---|---|
| CLI | Inventaire, styles, conversion, parcours directs, construction du projet, scripts, simulation, web et plot | [Commandes complètes](cli.md) |
| Meubles (CLI/API) | Gabarits, projets, validation, placement et dossier ZIP | [Exemple reproductible](../guide/meubles.md#exemple-reproductible-caisson-osb) |
| Profils de machine (CLI/API) | CRUD JSON, validation, statistiques, conversion compatible, archives et intégrité | [Guide et rapports reproductibles](../guide/machines.md) |
| Rhai | Création de formes, transformations, outils, opérations, journal et validation des identifiants | [API complète](rhai.md) |
| Post-processeur | Gabarits XML, macros, arcs, numérotation, modalités et changement d’outil | [Propriétés prises en charge](postprocesseurs.md) |
| Backplot HTML | Zoom, déplacements, animation, filtrage et inspection des trajectoires | [Exemple interactif](../examples/trajectoires.html), [capture](../assets/screenshots/23-backplot.png) |
| Viewer natif | Lecture G-code, zoom, profondeur et animation | [Utilisation](cli.md#viewer-natif) |

## Provenance et reproduction

Les captures 01 à 23 sont réalisées sur macOS Apple Silicon avec la version
0.2.0. Les captures 24 à 32 montrent l’Atelier de la version 0.4.0 sur la même
plateforme, avec des profils fictifs publics ; la capture 32 est recadrée sur le
dialogue de doublon. Les captures 33 et 34 montrent le modèle ID CNC PRO dans
le Studio 0.4.1 sur macOS Apple Silicon. Les captures 35 à 41 montrent le module
Meubles du Studio 0.5.0 installé depuis le DMG publié sur la même plateforme,
avec le caisson synthétique
du [guide meubles](../guide/meubles.md). Le projet de base, son script et ses exports sont disponibles dans le
[tutoriel](../guide/premier-projet.md). Les vues de ponts, de brut et de simulation
illustrent des modifications décrites dans le tutoriel. Les images sont des
captures de l’application ; elles ne sont pas des maquettes d’interface.

Après une modification du produit, mettez à jour la procédure et sa capture
ensemble. Une case disponible dans un panneau commun ne garantit pas un effet
sur toutes les stratégies : le guide distingue les réglages actifs des métadonnées
et des [limites de version](depannage.md).

## Modèle ID CNC PRO depuis 0.4.1

[ID CNC PRO - Mach3](../guide/id-cnc-pro.md) est proposé à la première ouverture
d’une bibliothèque vide, dans la création guidée et par `machine profile init`.
Les profils existants restent conservés. Exemple JSON, sources et paramètres
à confirmer sont décrits dans le guide dédié.

Les captures 42 à 47 documentent le compositeur du Studio 0.6.0, depuis le paquet
macOS Apple Silicon de cette release ; voir la [provenance et les limites](../guide/composer-meubles.md#validation-et-limites).

Les captures 49 à 54 documentent l’assistant du Studio 0.7.1 sur macOS Apple Silicon,
avec Mistral et des exemples synthétiques publics ; voir la
[provenance et la couverture réelle](../guide/assistant.md#validation-et-provenance).

## Diagnostics 0.7.1

[Procédure](diagnostics.md) · [Issue #24](https://github.com/FabLabCAM/core/issues/24)

Niveau du journal, piles complètes, ouverture du dossier, export texte et armement
core par session dans une compilation macOS de diagnostic. La
[capture 54](../assets/screenshots/54-diagnostics.png) provient du binaire local
0.7.1 sur macOS Apple Silicon avec la plaque synthétique. Les paquets publiés
conservent la signature normale ; la capture montre un bundle de diagnostic.
