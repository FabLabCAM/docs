# Dépannage et limites connues

## Résoudre les problèmes courants

| Symptôme | Vérification et solution |
|---|---|
| Mauvaise architecture | Télécharger ARM64 ou x64 selon le processeur et l’OS |
| Linux refuse un binaire avec une erreur GLIBC | Utiliser glibc 2.35+ ou compiler depuis les sources sur le système cible |
| Fenêtre graphique absente sous Linux | Vérifier session graphique, OpenGL/EGL, pilotes et bibliothèques X11/Wayland |
| Dialogue de fichier absent | Installer Zenity sous Linux ; utiliser le panneau de saisie par chemin ou la CLI |
| Texte absent | Installer une police compatible et vérifier son chemin et ses glyphes |
| Import incomplet | Lire les éléments ignorés, vectoriser le texte et exporter un dessin 2D plus simple |
| Poche impossible | Fermer les contours, retirer les doublons et vérifier que la fraise passe dans les régions |
| Parcours ancien encore visible | Corriger l’erreur de calcul avant de se fier au dernier résultat affiché |
| Modification sans effet | Terminer la saisie ; cliquer **Appliquer** quand le formulaire l’exige |
| Suppression d’outil refusée | Sélectionner un outil de remplacement pour les opérations utilisatrices |
| Objet invisible | Vérifier calque visible, cadrage et filtre de trajectoires |
| Simulation lente | Commencer avec une maille de 1 ou 0,5 mm avant d’affiner |
| Export différent sur un autre ordinateur | Comparer version, police, préférences et fichier de post-processeur |
| `--help` demande une valeur | Utiliser `fablabcam help` dans la version 0.2.0 |

## Périmètre de la première version

FabLabCAM est un outil de **dessin 2D et FAO 2.5D**. Il ne propose pas de
modélisation paramétrique de solides, d’usinage 5 axes, de tournage, de calcul de
bridage ni de commande directe de la machine. Le viewer de G-code et les pages
HTML sont des outils d’inspection, pas un contrôleur CNC.

Les importeurs DXF/SVG et le post-processeur XML couvrent un sous-ensemble.
Les contours doivent être examinés après conversion. Le texte devient une
collection de formes ; les polices peuvent changer l’apparence lors d’une
régénération par script.

La simulation utilise une grille de hauteurs. Elle ne détecte pas toutes les
collisions de machine et ne modélise pas les brides ou le porte-outil complet.
La fraise torique est assimilée à une fraise droite. Les limites de coupe et
plusieurs dimensions de l’outil sont informatives, sans contrainte automatique.

Les paquets macOS ne sont pas notariés et les exécutables Windows ne sont pas
signés commercialement. Les tests automatisés couvrent les calculs et les
installations ; les captures et la vérification manuelle du Studio de cette
version ont été réalisées sur macOS Apple Silicon. Cela ne constitue pas une
validation visuelle exhaustive sur tous les bureaux et pilotes graphiques.

## Signaler un problème

Ouvrez une [issue dans core](https://github.com/FabLabCAM/core/issues) avec la
version, l’OS, l’architecture, les étapes, le résultat attendu et le message
observé. Joignez un exemple minimal sans données confidentielles. Pour une erreur
dans ce guide, utilisez [le dépôt docs](https://github.com/FabLabCAM/docs/issues).
Les vulnérabilités peuvent être signalées via le canal de sécurité privé de
GitHub, lorsqu’il est proposé dans l’onglet Security.

## Meubles et dalles CNC

Une dimension impossible, une dalle plus grande que la course déclarée ou une
pièce hors zone utile bloque le dossier de fabrication. Vérifiez les limites du
modèle, marges, espacement, diamètre de fraise et rotations. Le placement ne
raccorde pas les pièces trop grandes. Les courses d'exemple ne complètent pas les
limites inconnues du profil machine. Un export G-code de dalle reste bloqué tant
que sa configuration et son analyse sont incomplètes.

Lorsqu'un document a été modifié ailleurs, rechargez-le ou importez une copie ;
les données récentes ne sont pas écrasées. Un export exige un nouveau nom de
fichier. Voir les [formats et limites du module](../guide/meubles.md).


## Composition et assemblages

- Pour ajouter un élément, activez **Composer le meuble**, puis sélectionnez une
  case dans **Structure et cases**. Le nombre de tablettes du gabarit historique
  ne pilote plus une composition déjà activée.
- Une valeur temporairement invalide conserve le formulaire. Corrigez le champ
  indiqué ; l'ancien aperçu affiché pendant la frappe ne peut pas être exporté.
- Un dos de 1 000 × 1 200 mm ne rentre pas sur 1 500 × 800 mm. Retirez-le
  explicitement ou utilisez une machine et une dalle adaptées ; aucun raccord
  automatique n'est généré.
- Des tenons opposés dans une paroi partagée peuvent entrer en collision.
  Corrigez la liaison concernée, son type ou sa profondeur ; le moteur n'efface
  pas silencieusement une mortaise.
- Une rainure trop étroite demande une fraise plus petite ou une géométrie adaptée.
  Vérifiez aussi la matière restante et les montages verso.
- Un CB de meuble conserve les opérations requises : créez les poches/profils
  avec leurs faces, profondeurs et côtés attendus avant le G-code. Le profil
  machine doit lui aussi être complet et l'analyse valide.

Voir le [guide du compositeur](../guide/composer-meubles.md) pour les conventions,
les huit familles disponibles et les limites de fabrication.

## Diagnostics

Le correctif de profil et les [options de diagnostic de la version 0.7.2](diagnostics.md)
sont disponibles depuis la version 0.7.2.
