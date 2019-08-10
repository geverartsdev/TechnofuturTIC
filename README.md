# Contenu éducatif pour les stages d'été TechnofuturTIC
Ce répo contient des documents, codes, ressources utilisées lors de stages d'été à TechnofuturTIC.

#### Contributeurs :
Everarts de Velp Guillaume, Ody Lucas

## Cloner le repo
```Bash
git clone https://github.com/geverartsdev/TechnofuturTIC.git
```

## Installer le jeu sur windows

Pensez à retirer toute référence au capteur (Sensor.py) de votre code; en effet, celui-ci ne fonctionnne que sous Raspberry Pi.

Le passage par clé usb, internet ou autre peut avoir ENLEVÉ le status d'éxécutable à launch.bat; assurez-vous de restaurer cette permission.

## Première méthode
####  1. Installer python.
Pensez à cocher la case PATH lors de l'installation!
pour vérifier que l'installation c'est bien déroulée, ouvrez l'invite de commande windows (win + R => cmd, ou simplement cherchez "cmd" dans la barre de recherce du menu démarrer) et entrez-y la commande suivante: 

    python

 Si l'interpreteur python s'ouvre, tout va bien! (vous pouvez fermer python avec "exit()")
#### 2. Installer pygame
Dans l'invite de commande, entrez la commande suivante : 

    pip install pygame
    
Attendez la fin de l'installation
#### 3. Lancer le script "launcher.bat"
Et voilà! si tout fonctionne, le jeu se lance!

#### 4. Si launch.bat ne fait rien...
essayer de lancer launch.bat depuis l'invite de commande, utilisez
    
    cd <sous-dossier>
    
pour naviger vers un <sous-dossier>. une fois arrivé dans le dossier TechnofuturTIC/python, lancez launch.bat en tapant son nom, et l'erreur devrait s'afficher!

## Deuxième méthode
Déplacez le contenu de tous les fichiers sources python (vaisseau.py, Explosion.py, Constants.py, etc...) dans \__init__.py, en remplacant la ligne 

    from ... import ...
    
corespondante. Ensuite, après installation de python et pygame ( voir méthode 1), le jeu devrait se lancer en executant \__init__.py seul (par exemple dans IDLE, l'éditeur de code python: Run -> run module)
## Pour obtenir un executable windows (.exe)
http://www.py2exe.org/index.cgi/Tutorial

Il s'agit d'un outil Python pour transformer d'autres programmes python en executable! avec un peu d'aide d'une personne comprenant l'anglais, ce tutoriel vous permettera de produire un executable windows.

## License
Copyright 2019 Everarts de Velp Guillaume, Ody Lucas

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
