# Journaux et rapports de panne

Disponible depuis [FabLabCAM 0.7.2](https://github.com/FabLabCAM/core/releases/tag/v0.7.2),
avec le correctif de l'[issue #24](https://github.com/FabLabCAM/core/issues/24).
Ces options sont conservées dans la version **0.7.3**. La procédure ci-dessous
distingue les rapports texte, disponibles dans les paquets standards, et le core
dump macOS, qui nécessite l’application **FabLabCAM Diagnostic**.

## Activer les diagnostics dans l’interface

1. Ouvrez **Outils → Préférences → Diagnostics**.
2. Sélectionnez **Détaillé** dans **Niveau du journal** pour enregistrer les
   calculs : opération, formes, nombre de sommets, côté, diamètre, décalage et durée.
3. Gardez **Traces complètes lors d’une erreur fatale** cochée pour enregistrer
   la pile d’une panique Rust, y compris après un lancement depuis Finder.
4. Reproduisez le problème, puis utilisez **Ouvrir le dossier des diagnostics**
   ou **Exporter le rapport…**. Après un crash, relancez d’abord le Studio.

Ces deux réglages sont appliqués immédiatement et mémorisés. Le niveau Normal
conserve les événements de session et les erreurs de calcul. Le journal détaillé
n’enregistre pas les échanges réseau ni les clés de l’assistant.

[![Préférences de diagnostic sur une plaque de démonstration](../assets/screenshots/54-diagnostics.png)](../assets/screenshots/54-diagnostics.png)

Capture réelle du binaire de développement 0.7.1, macOS Apple Silicon, avec
[plaque.rhai](../examples/plaque.rhai) et stockage de test isolé. Le bundle de
cette capture est signé pour diagnostic ; le mode core reste désactivé.

## Retrouver les fichiers

| Système | Dossier par défaut |
|---|---|
| macOS | `~/Library/Logs/FabLabCAM` |
| Windows | `%LOCALAPPDATA%\FabLabCAM\Diagnostics` |
| Linux | `$XDG_STATE_HOME/fablabcam/diagnostics`, sinon `~/.local/state/fablabcam/diagnostics` |

Les fichiers `session-*.jsonl` contiennent les événements horodatés, version,
identifiant de build et PID. Les fichiers `panic-*.txt` conservent séparément
chaque panique : une seconde erreur ne remplace pas la première. Une compilation
locale sans identifiant explicite indique `local`.

Le journal dispose de huit emplacements pour plusieurs instances. Chacun garde
un fichier de 1 Mio et trois rotations, soit au plus 32 Mio de journaux. Au
lancement, les vingt derniers rapports de panique sont conservés. Un dossier
inaccessible produit un message visible ; le terminal reste un repli pour les
pannes d’écriture.

L’export rassemble les journaux et rapports texte, **sans projet, préférences ni
core dump**. Relisez-le avant de le joindre à une issue : un message de panique
ou une pile peut contenir un chemin privé. L’export n’envoie rien sur Internet.

## Core dump sur macOS

Un core contient la mémoire du processus, peut occuper plusieurs Gio et inclure
des données de projet ou des clés API. Il reste local et ne fait jamais partie
de l’export texte. Sa collecte est utile quand une pile seule ne suffit pas.

### Quelle application ouvrir ?

| Application | Journaux et rapports texte | Capture core intégrée |
|---|---|---|
| **FabLabCAM Studio**, installée depuis le DMG ou ZIP standard | Oui | Indisponible : signature sans autorisation de débogage |
| **FabLabCAM Diagnostic**, compilée séparément sur macOS | Oui | Disponible sous préconditions, puis armement explicite |

Si la version de diagnostic est déjà installée dans Applications, ouvrez
**FabLabCAM Diagnostic.app**. Sinon, suivez la
[préparation de la compilation](#preparer-une-compilation-de-diagnostic).
Son nom de fenêtre reste « FabLabCAM Studio » : repérez l’application choisie
dans Finder. Par défaut, les deux applications utilisent les mêmes dossiers
de préférences et de journaux ; le nom distinct du bundle n’isole pas ces données.

### Armer, reproduire et terminer le test

1. Enregistrez le projet avant l’essai, puis ouvrez-le dans **FabLabCAM Diagnostic**.
2. Allez dans **Outils → Préférences → Diagnostics**. Choisissez **Détaillé**
   et gardez **Traces complètes lors d’une erreur fatale** cochée pour disposer
   aussi des paramètres du calcul et du rapport texte.
3. Dans **Core dump — mode avancé**, cliquez **Vérifier les préconditions**.
   Lisez le résultat et notez la **Destination attendue** avant de reproduire
   la panne : le PID, et donc le nom du fichier, change à chaque lancement.
4. Cliquez **Armer pour cette session**. L’état doit devenir
   **Armé pour la prochaine panique de cette session**. Le niveau Détaillé
   et la case Traces complètes n’arment pas le core à eux seuls.
5. Reproduisez le problème. Si une panique Rust survient, le Studio écrit son
   rapport puis s’arrête volontairement pour demander un core à macOS.
6. Si le calcul réussit et que l’application reste ouverte, **aucun core n’est
   attendu**. Cliquez **Désarmer**, ou fermez la version Diagnostic, puis revenez
   au Studio standard pour l’usage habituel. Notez le résultat du test et les
   versions comparées dans le suivi du problème.

### Préconditions et portée des réglages

Le bouton **Armer pour cette session** est disponible seulement si les
préconditions sont satisfaites : binaire signé pour diagnostic, capture autorisée
par macOS, dossier accessible, limite système suffisante et au moins 10 Gio libres.
L’interface affiche le motif d’un refus et le chemin attendu, habituellement
`/cores/core.<PID>`. **Vérifier les préconditions** actualise cet état.

| Option | Effet | Après relance |
|---|---|---|
| **Niveau du journal : Normal / Détaillé** | Choisit les événements et paramètres consignés dans les journaux texte | Choix mémorisé |
| **Traces complètes lors d’une erreur fatale** | Ajoute la pile complète au rapport de panique Rust | Choix mémorisé |
| **Vérifier les préconditions** | Relit signature, réglages macOS, destination, limites et espace disponible | Aucun armement |
| **Armer pour cette session** | Autorise la demande de core pour ce processus ; une panique entraîne son arrêt, même si le calcul aurait pu la récupérer | Désarmé au prochain lancement |
| **Désarmer** | Restaure la limite souple initiale du processus | Reste désarmé |

macOS peut encore refuser la capture ; un état « armé » ne prouve pas qu’un
fichier a été créé. Le core ne capture pas un simple message d’erreur, un calcul
réussi, un blocage sans arrêt fatal ou une fermeture forcée par `SIGKILL`.

La limite noyau porte sur la mémoire virtuelle : elle vaut 1 Tio pour couvrir les
réservations de macOS. **Ce n’est pas un plafond d’occupation disque**. Les paquets
normaux n’activent pas l’autorisation de débogage `get-task-allow` ; leur interface
indique qu’une compilation de diagnostic est nécessaire. Aucun réglage global
macOS ni permission de dossier n’est changé par le Studio.

### Si le bouton est grisé ou si aucun core n’apparaît

| Message ou situation | Vérification à effectuer |
|---|---|
| « Ce binaire n’autorise pas les core dumps » | Ouvrir **FabLabCAM Diagnostic**, compilée avec le script ci-dessous ; les installateurs standards ne suffisent pas |
| « Espace disque insuffisant » | Conserver au moins **10 Gio libres** sur le volume de destination, puis vérifier à nouveau ; un core peut en consommer plusieurs |
| Capture désactivée par macOS, dossier inaccessible ou limite dure insuffisante | Faire vérifier la configuration système par l’administrateur ; le Studio affiche le refus et ne modifie pas ces réglages globaux |
| Chemin système non pris en charge ou fichier déjà présent | Le chemin doit être absolu ; le jeton pris en charge est `%P`. Conserver un éventuel core existant avant de faire examiner la destination |
| Limite actuelle « 0 octets » avant armement | Cet état désarmé est normal si les préconditions sont validées ; le bouton relève la limite du processus pour la session |
| Le profil fonctionne après la mise à jour | Aucun core n’est attendu : noter que le problème n’est plus reproduit et désarmer la capture |
| Le Studio s’est arrêté, mais le fichier est absent | Chercher le chemin et le PID de la session arrêtée, lire `panic-*.txt` et les rapports macOS dans Console ; l’armement ne garantit pas la création du core |

### Récupérer le core après une panne

Dans Finder, utilisez **Aller → Aller au dossier…** et ouvrez `/cores` si c’était
la destination affichée. Recherchez `core.<PID>` pour le processus arrêté et
attendez la fin de son écriture avant de le copier. Après relance du Studio,
**Exporter le rapport…** rassemble les journaux et rapports texte, **pas le core**.

Conservez le core avec la version, l’identifiant de build, le binaire exact et
son `dSYM`. Ne joignez pas cette image mémoire à une issue publique : elle peut
contenir les données et clés présentes dans le processus. Privilégiez le rapport
texte relu ; convenez d’un transfert privé si l’analyse du core est nécessaire.

### Préparer une compilation de diagnostic

Sur macOS, avec **Python 3.12**, Rust et les outils Xcode installés, partez du
tag correspondant à la version à examiner. Exemple pour **0.7.3**, dans un
nouveau dossier :

```sh
git clone --branch v0.7.3 --depth 1 \
  https://github.com/FabLabCAM/core.git fablabcam-diagnostic-0.7.3
cd fablabcam-diagnostic-0.7.3
python3.12 packaging/diagnostic_macos.py
```

Le script produit un bundle distinct, optimisé, signé pour diagnostic et accompagné
par `fablabcam-studio-ui.dSYM` dans `target/diagnostic-app/`. Il affiche les UUID
du binaire et des symboles : ils doivent correspondre. La commande `python3`
de macOS peut être trop ancienne et échouer avec « No module named tomllib » ;
utilisez bien `python3.12`.

Dans Finder, copiez **FabLabCAM Diagnostic.app** depuis ce dossier vers
**Applications**, puis ouvrez cette application. Vous pouvez aussi la lancer
directement depuis la compilation :

```sh
open "target/diagnostic-app/FabLabCAM Diagnostic.app"
```

Conservez une copie du bundle **et** de son `fablabcam-studio-ui.dSYM` ensemble,
dans un dossier d’archive identifié par la version et l’UUID. Le script remplace
ses sorties lors d’une nouvelle compilation : cette archive permet de garder
les symboles du binaire effectivement utilisé pour la capture. L’installation
du bundle seule ne conserve pas le `dSYM` dans Applications.

### Analyser avec les symboles correspondants

Depuis le dossier de compilation ou une archive contenant le même couple
binaire/dSYM, vérifiez les UUID puis ouvrez le core. Remplacez `PID` par celui
de la session arrêtée et adaptez les chemins si les fichiers ont été archivés :

```sh
diagnostic_app="target/diagnostic-app/FabLabCAM Diagnostic.app"
diagnostic_symbols="target/diagnostic-app/fablabcam-studio-ui.dSYM"
dwarfdump --uuid "$diagnostic_app/Contents/MacOS/fablabcam-studio-ui"
dwarfdump --uuid "$diagnostic_symbols"
lldb "$diagnostic_app/Contents/MacOS/fablabcam-studio-ui" \
  --core /cores/core.PID
```

Dans LLDB :

```text
target symbols add target/diagnostic-app/fablabcam-studio-ui.dSYM
thread backtrace all
```

Les UUID doivent correspondre. Une reconstruction ultérieure de la même version
ne suffit pas à garantir la correspondance des symboles. Pour une panne native
sans panique Rust, consultez aussi les rapports macOS dans Console.

### Vérification en 0.7.3

Le 6 novembre 2026, la compilation de diagnostic du tag `v0.7.3` a été installée
sur macOS Apple Silicon : signature, UUID du `dSYM` et préconditions dans
l’interface vérifiés. L’utilisateur ne reproduit plus le crash des profils après
les derniers correctifs. Aucun nouveau core n’a été généré pendant cet essai ;
la capture contrôlée et l’analyse LLDB réalisées pendant le développement restent
décrites dans le [rapport de validation](https://github.com/FabLabCAM/core/blob/v0.7.2/docs/qa/0.7.2.md).

## Équivalents en ligne de commande

```sh
fablabcam-studio-ui dessin.dxf --diagnostics --backtrace full
fablabcam-studio-ui --tab diagnostics --log-level debug
fablabcam-studio-ui --diagnostics-dir /tmp/fablabcam-diagnostic
```

`--log-level normal|debug`, `--backtrace off|full` et `--diagnostics` remplacent les
réglages pour cette session seulement. `--core-on-panic` demande l’armement sous
les mêmes préconditions que l’interface. `FABLABCAM_DIAGNOSTICS_DIR` permet aussi
d’isoler le stockage. Ces options appartiennent au **Studio graphique**.

## Profil de lettres DXF

Le correctif #24 retire, sur une copie utilisée pour l’offset, les positions
répétées et sommets redondants. Le dessin original reste inchangé. Le cas signalé
était une lettre E fermée dont le dernier sommet répétait le premier.

Une erreur de calcul est affichée et le projet reste éditable. Un ancien parcours
peut rester visible pour comparaison ; l’export du projet est bloqué tant qu’une
opération active est en erreur. Corrigez ou désactivez cette opération avant
l’export. Les paniques récupérables ne couvrent pas l’épuisement mémoire, SIGKILL,
les blocages ni toutes les erreurs natives.
