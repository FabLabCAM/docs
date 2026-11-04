# Exporter et contrôler le G-code

[![Accès aux opérations et à l’export G-code](../assets/screenshots/13-profil.png)](../assets/screenshots/13-profil.png)

## Export depuis le Studio

1. Vérifiez l’ordre et l’activation des opérations.
2. Corrigez toute erreur de calcul dans leurs propriétés.
3. Sélectionnez le post-processeur dans les propriétés du projet ou **Système**.
   Un chemin vide utilise le post-processeur intégré.
4. Cliquez **Générer le G-code** (ou le raccourci d’export) et choisissez le fichier `.nc`.
5. Lisez le message de résultat et ouvrez le fichier produit pour contrôle.

Le post-processeur sélectionné est conservé dans les préférences locales.
Transmettez son fichier avec le projet si une autre personne doit reproduire
le programme avec exactement les mêmes réglages.

## Export en ligne de commande

```sh
fablabcam build plaque.cb -o plaque.nc
fablabcam build plaque.cb --post machine.cbpp -o plaque-machine.nc
```

`build` exploite les opérations enregistrées dans le projet. La commande
`gcode` crée un parcours à partir du dessin et des options passées en ligne de
commande ; elle ne remplace pas `build` pour rejouer la liste du projet.

## Inspecter le résultat indépendamment

```sh
fablabcam plot plaque.nc -o trace.svg
fablabcam plot plaque.nc -o trace.html
fablabcam-view plaque.nc
```

Le SVG fournit une vue de dessus et un profil de profondeur. La page HTML
ajoute navigation, zoom, animation et survol. Le viewer natif fournit une vue
interactive du G-code relu. Les rapides, plongées, directions et profondeurs
peuvent être affichés séparément. Essayez l’[exemple interactif](../examples/trajectoires.html).

## Points à contrôler

Contrôlez les unités, les origines et le repère, le sens de broche, les numéros
d’outils, les avances, les profondeurs, les déplacements rapides et les hauteurs
de dégagement. Vérifiez aussi le dialecte des arcs et cycles avec votre contrôleur.
Le post-processeur intégré n’est pas une configuration validée pour toutes les
machines. Le logiciel exporte un fichier ; il ne pilote pas directement la CNC.

## Mach3 : fichier chargé, lancement bloqué

Le diagnostic de l'[issue #23](https://github.com/FabLabCAM/core/issues/23) reste
ouvert : la ligne d'arrêt et le message de l'installation concernée doivent être
confirmés. Le nombre de lignes ou la présence de nombreux arcs ne suffisent pas
à expliquer un refus.

Dans la version 0.7.0, le préambule intégré ne déclare pas le mode des centres IJ
et n'annule pas les compensations et cycles précédents. Pour rendre ces modes
explicites, le [post-processeur de diagnostic](../examples/mach3-explicit-modes.cbpp)
est utilisable avec cette version, dans **Système → Post-processeur** ou en CLI :

```sh
fablabcam build plaque.cb --post mach3-explicit-modes.cbpp -o plaque-modes.nc
```

Il conserve les réglages d'usinage et écrit avant mouvement
`G21 G90 G17 G94 G40 G49 G80 G91.1` (G20 en pouces). Il ne change ni l'origine
de travail, ni le numéro d'outil, ni la demande de changement M6. Le correctif
des valeurs intégrées est en cours dans #23 ; il n'est pas livré en 0.7.0.

**Limite de la 0.7.0 :** son backplot confond G91.1 avec G91, ce qui déforme
l'aperçu et la simulation d'un fichier contenant ce mode explicite. Le gabarit
ci-dessus est destiné au diagnostic de l'export ; la relecture doit être faite
dans un interpréteur qui distingue ces modes. La correction du backplot est
incluse dans le travail de #23 et n'est pas encore publiée.

Relevez la ligne et la barre d'état après **Cycle Start**, puis comparez au même
projet avec le préambule explicite. Un arrêt sur M6 peut être l'attente normale
de changement d'outil, définie par les macros M6Start/M6End et la configuration
Mach3. Conservez cette information dans le signalement.

Le [manuel Mach3 Mill](https://www.machsupport.com/wp-content/uploads/2013/02/Mach3Mill_1.84.pdf)
accepte LF et CRLF (§10.5) et distingue G90 de G90.1/G91.1 (§10.7.26).
Une analyse statique sans erreur de rayon ne prouve pas que Mach3 pourra lancer
le programme avec ses macros et ses paramètres locaux.

La simulation du projet et la relecture du G-code sont complémentaires : une
commande ajoutée par un post-processeur peut avoir un effet que le simulateur du
projet ne représente pas. Voir la [référence des post-processeurs](../reference/postprocesseurs.md).

## Commandes du backplot interactif

[![Backplot de la plaque](../assets/screenshots/23-backplot.png)](../assets/screenshots/23-backplot.png)

Les cases **rapides**, **flèches de sens** et **points de plongée** contrôlent
les annotations. La couleur peut représenter la profondeur ou le type de
mouvement. Pour isoler une passe, cliquez son niveau Z ou activez les bornes
**bas / haut** ; **tous** retire ce filtre.

Glissez pour déplacer la vue, utilisez la molette pour zoomer et `F` ou un
double-clic pour cadrer. Le profil inférieur représente Z au long du parcours ;
un clic permet de positionner l’animation. Les boutons début/fin et pas à pas,
le curseur et la vitesse en mm/s contrôlent la lecture. `Espace` lance ou arrête
la lecture ; les flèches gauche/droite avancent pas à pas. **suivre l’outil**
maintient la vue sur la position courante. Le panneau affiche les coordonnées,
le type de déplacement et la ligne G-code correspondante.

La durée affichée est une estimation à partir des mouvements et avances
interprétés ; elle ne représente pas les accélérations et toutes les pauses
d’un contrôleur réel.

## Contrôler un programme avec un profil de machine

Depuis la v0.3.0, la commande `fablabcam machine validate` produit un rapport
lié aux limites et au dialecte d’un profil JSON. Voir le [guide des machines](machines.md).
Le backplot conserve son rôle de visualisation ; l’analyse statique expose
séparément les erreurs et les constructions non interprétées.
