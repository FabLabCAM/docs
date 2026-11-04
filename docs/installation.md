# Installation

La [release 0.6.0](https://github.com/FabLabCAM/core/releases/tag/v0.6.0)
contient Studio, la CLI et le viewer dans chaque distribution. Aucun compte
n’est nécessaire pour utiliser le logiciel localement.

## Choisir le bon paquet

| Système et processeur | Installation | Archive portable |
|---|---|---|
| macOS Apple Silicon (M1 et suivants) | [DMG ARM64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-macos-arm64.dmg) | [ZIP ARM64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-macos-arm64.zip) |
| macOS Intel | [DMG x64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-macos-x64.dmg) | [ZIP x64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-macos-x64.zip) |
| Windows Intel/AMD 64 bits | [Setup x64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-windows-x64-Setup.exe) | [ZIP x64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-windows-x64.zip) |
| Windows ARM64 | [Setup ARM64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-windows-arm64-Setup.exe) | [ZIP ARM64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-windows-arm64.zip) |
| Linux Intel/AMD 64 bits | [DEB amd64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-linux-x64.deb) | [tar.gz x64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-linux-x64.tar.gz) |
| Linux ARM64 | [DEB arm64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-linux-arm64.deb) | [tar.gz ARM64](https://github.com/FabLabCAM/core/releases/download/v0.6.0/FabLabCAM-0.6.0-linux-arm64.tar.gz) |

Les binaires macOS ciblent macOS 11 ou supérieur. La construction et les tests
utilisent macOS 15. Windows x64 vise Windows 10/11 ; ARM64 vise Windows 11 ARM64.
Les vérifications automatisées Windows tournent sur Windows Server 2025 x64 et
Windows 11 ARM64. Linux nécessite **glibc 2.35 ou supérieure** ; les paquets sont
construits sur Ubuntu 22.04. Un Raspberry Pi nécessite un système **64 bits**
et un environnement graphique pour Studio. Les versions 32 bits, Android, iOS
et Linux musl ne sont pas distribuées.

## macOS

1. Téléchargez le DMG correspondant à votre processeur.
2. Ouvrez le disque et déplacez **FabLabCAM Studio.app** dans **Applications**.
3. Lancez l’application depuis Applications.
4. Pour la version portable, décompressez le ZIP et ouvrez l’application incluse.

L’application dispose d’une signature ad hoc ; elle n’est pas notariée par
Apple. macOS peut demander une autorisation explicite pour une application
 téléchargée. Vérifiez sa provenance et utilisez les réglages de sécurité
standard de votre système si nécessaire ; aucune désactivation globale de
protection n’est requise par le logiciel.

Les exécutables supplémentaires sont dans le bundle :

```sh
"/Applications/FabLabCAM Studio.app/Contents/MacOS/fablabcam" help
"/Applications/FabLabCAM Studio.app/Contents/MacOS/fablabcam-view" programme.nc
```

Pour désinstaller, retirez l’application d’Applications. Vos projets et
préférences sont séparés de l’application.

## Windows

1. Lancez le fichier **Setup.exe** de votre architecture.
2. Choisissez la langue et le dossier proposé dans votre profil utilisateur.
3. Terminez l’installation et ouvrez **FabLabCAM Studio** dans le menu Démarrer.

L’installation est propre à l’utilisateur courant. Les exécutables ne sont pas
signés avec un certificat commercial ; Windows peut afficher un avertissement
sur l’éditeur. Les ZIP permettent une utilisation sans installateur : extrayez
le dossier complet puis lancez `fablabcam-studio-ui.exe`.

Dans PowerShell, depuis le dossier installé ou extrait :

```powershell
.\fablabcam.exe help
.\fablabcam-view.exe programme.nc
```

Le runtime C est lié statiquement. Aucun environnement Rust ou Python n’est
requis pour utiliser l’application. Désinstallez depuis les applications Windows
ou le raccourci de désinstallation. Les fichiers de projet et les préférences
personnelles ne sont pas effacés par l’installateur.

## Linux — Debian, Ubuntu et dérivés

Téléchargez le DEB approprié puis, dans le dossier de téléchargement :

```sh
sudo apt install ./FabLabCAM-0.6.0-linux-x64.deb
fablabcam-studio-ui
fablabcam help
```

Sur ARM64, remplacez `x64` par `arm64` dans le nom du fichier. Le paquet installe
le lanceur graphique, les trois exécutables et les dépendances de bureau.
**Zenity** fournit les dialogues de fichiers et **DejaVu** une police pour le
texte vectorisé. Pour désinstaller : `sudo apt remove fablabcam`.

## Linux — archive portable

```sh
tar -xzf FabLabCAM-0.6.0-linux-x64.tar.gz
cd FabLabCAM-0.6.0-linux-x64
./fablabcam-studio-ui
./fablabcam help
```

L’archive ne fournit pas les bibliothèques système. Il faut glibc 2.35+, les
bibliothèques X11 (Xcursor, Xi, Xrandr), xkbcommon, Wayland (client/cursor/EGL),
OpenGL/EGL, libstdc++ et libgcc. Installez également Zenity et une police TrueType.
Sur Ubuntu/Debian :

```sh
sudo apt install libx11-6 libxcursor1 libxi6 libxrandr2 libxkbcommon0 \
  libwayland-client0 libwayland-cursor0 libwayland-egl1 libegl1 libgl1 \
  libstdc++6 libgcc-s1 zenity fonts-dejavu-core
```

Les autres distributions doivent fournir leurs paquets équivalents. Il n’y a
pas de paquet RPM, Flatpak ou AppImage dans cette release.

## Vérifier le téléchargement

Récupérez [SHA256SUMS.txt](https://github.com/FabLabCAM/core/releases/download/v0.6.0/SHA256SUMS.txt)
sur la même release et comparez la somme de votre fichier :

```sh
# macOS
shasum -a 256 FabLabCAM-0.6.0-macos-arm64.dmg
# Linux
sha256sum FabLabCAM-0.6.0-linux-x64.deb
```

```powershell
Get-FileHash .\FabLabCAM-0.6.0-windows-x64-Setup.exe -Algorithm SHA256
```

Une somme confirme l’intégrité du fichier par rapport à la release ; elle ne
remplace pas une signature d’éditeur. Conservez les notices de licences avec
une copie redistribuée du logiciel.

## Premier lancement et mise à jour

Ouvrez la [plaque d’exemple](guide/premier-projet.md). Le résultat attendu est
un projet comportant quatre opérations. Pour mettre à jour, sauvegardez vos
projets `.cb`, installez le nouveau paquet et consultez ses notes de version.
Il n’existe pas de mise à jour automatique dans 0.6.0.
