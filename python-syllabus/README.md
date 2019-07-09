# Syllabus pour le stage de python

## Génération du pdf sur linux
### Dépendances
Pour compiler ce projet certains packages sont nécessaires, pour les installer entrez les commandes suivantes dans un terminal :
```Bash
sudo apt install latexila
sudo apt install texlive-lang-french
sudo apt install texlive-latex-extra
```
Notez qu'exécuter ces commandes installera aussi un editeur de texte spécialement taillé pour LaTeX et très agréable à utiliser : LaTeXila.

### Compilation
#### LaTeXila
Si vous utilisez LaTeXila, vous pouvez soit cliquer sur les boutons prévus pour la compilation soit utiliser le raccourci clavier F2.
#### Ligne de commande
Un makefile a été créé pour vous, il ne reste qu'à exécuter la commande suivante dans un terminal ouvert dans le dossier du projet, le pdf attendu s'appelle `main.tex`.
```Bash
make
```

Pour supprimer les fichiers générés par la compilation (dont le pdf!) vous pouvez exécuter cette commande :
```Bash
make clean
```
