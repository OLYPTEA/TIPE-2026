#  Détermination de π par l’étude de collisions successives d’un système dynamique

---

##  Présentation du projet

Ce dépôt regroupe l’ensemble de mon **TIPE 2026**, consacré à la détermination de π à partir de l’étude théorique et expérimentale d’un système de collisions élastiques successives.

Le projet s’appuie sur la modélisation d’un système dynamique composé de deux blocs en interaction, dont le nombre total de collisions encode les décimales de π lorsque le rapport des masses spécifiques.

Les objectifs sont :

- Comprendre le cadre théorique du phénomène (conservation de l’énergie et de la quantité de mouvement)
- Mettre en œuvre une modélisation numérique et expérimentale du système

---

##  Contenu du dépôt

---

##  Interface de simulation

<p align="center">
  <img src="Picture\ImageLogicielTIPE.png" width="700">
</p>

Cette interface permet de modifier les paramètres du système (masses, vitesses initiales) et d’observer dynamiquement le nombre de collisions obtenues.

---

Vous trouverez dans ce repository :

-  La **MCOT**
-  Le **code Python** utilisé pour les simulations
-  Les **expériences réalisées** ainsi que leurs rapports
-  Les **sources**
-  Le PDF original de l’article de Gregory Galperin (dans le dossier `sources`)

Tous les fichiers présents correspondent à la **version finale et à jour** du projet, (à part le logiciel de simulation où il reste quelques modifications à faire).

---

##  Cadre scientifique

Le phénomène étudié repose sur :

- La conservation de l’énergie cinétique  
- La conservation de la quantité de mouvement  
- Une interprétation géométrique dans l’espace des vitesses réduites  

Lorsque le rapport des masses vaut :

$$
\frac{M}{m} = 100^n
$$

le nombre total de collisions correspond aux premières décimales de π.

---

##  Résultats numériques

Graphe obtenu dans les variables réduites :

<p align="center">
  <img src="Picture\ImagePythonTIPE.png" width="600">
</p>

On observe que la trajectoire dans l’espace $(\sqrt{m}u, \sqrt{M}v)$ suit une structure circulaire, traduisant la conservation de l’énergie.

-> Prise en compte de la dissipation de l'énergie ????? Coming Soon

---

## Éxperience 

### Principe 
<p align="center">
  <img src="Picture\ModelTIPE2026OPTIQUE.png" width="600">
</p>

### Construction d'un banc de test 

#### 1. Première itération : Banc de test initial
Dans un premier temps, j'ai modélisé un **banc de test classique** (Banc1) utilisant des liaisons mécaniques traditionnelles. Cependant, l'analyse géométrique du système a mis en évidence une limitation critique : le manque de résolution et la présence de jeu mécanique au niveau du guidage de l'axe. 

Pour atteindre notre objectif de **31 réflexions** (permettant d'approximer $\pi \approx 3.1$), une précision angulaire de l'ordre du milliradian est requise. Avec l'impression 3D standard, le jeu inhérent aux pièces assemblées aurait rendu le faisceau instable en sortie, chaque micro-vibration modifiant le nombre de rebonds.

<img width="3840" height="2160" alt="banc5" src="https://github.com/user-attachments/assets/ab1e4e8b-f6e1-45a1-8258-9025134874df" />

#### 2. Deuxième itération : Guidage par liaison compliante ("Flexure")
Pour nous affranchir des frottements (phénomène de *stick-slip*) et du jeu mécanique, j'ai réorienté la conception vers une **liaison compliante par guidage flexible (flexure)**, après étude de la documentation technique dédiée à l'optonique de haute précision.

En plus de pousser la précision au niveau micrométrique, cette approche simplifie considérablement la fabrication :
* **Monolithisme :** Le support fixe et le bras mobile sont fusionnés en une seule pièce, ce qui élimine les tolérances d'assemblage et facilite l'impression 3D.
* **Rotation pure :** Le mouvement est obtenu exclusivement par la **déformation élastique** d'une fine membrane de plastique, supprimant tout composant mécanique en friction.
* **Choix du matériau :** Le **PETG** a été sélectionné à la place du PLA standard pour ses excellentes propriétés mécaniques et sa résistance supérieure au fluage (*creep*), évitant que la charnière ne se déforme de manière permanente sous la contrainte de la vis.

#### 3. Mécanisme de réglage et annulation du Backlash
La cinématique a été optimisée en plaçant la charnière flexible à l'apex (la pointe fermée) du V, maximisant ainsi le bras de levier. Le réglage fin de l'angle se fait à l'entrée de la cavité via une vis de pression. 

Bien que la déformation élastique du PETG offre une force de rappel naturelle, j'ai intégré **deux ressorts de compression en opposition**. Ce système applique une précharge constante qui annule le jeu de fond de filet (*backlash*) de la vis et garantit un contact mécanique optimal, fluide et répétable lors des phases de calibration.

<img width="3840" height="2160" alt="banc4" src="https://github.com/user-attachments/assets/2ea050de-1a6e-4214-8760-eae790947921" />

---

##  Sources

Les références principales sont les suivantes :

-  3Blue1Brown — *The most unexpected answer to a counting puzzle*  
  https://www.3blue1brown.com/?v=clacks  

-  Vidéo explicative sur les collisions et π  
  https://www.youtube.com/watch?v=brU5yLm9DZM  

-  Université de Bonn  
  https://www.uni-bonn.de/en  

---

##  Note importante

Le premier lien mentionné dans la MCOT (Étude originale de Gregory Galperin sur π) n’est malheureusement plus accessible en ligne.

Cependant, le **PDF original** de l’article est disponible dans le dossier `sources` de ce dépôt.

---

##  Exécution du code

Pour lancer la simulation :

```bash
python simulation.py
