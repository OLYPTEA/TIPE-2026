#  Détermination de π par l’étude de collisions successives d’un système dynamique

---

##  Présentation du projet

Ce dépôt regroupe l’ensemble de mon **TIPE 2026**, consacré à la détermination de π à partir de l’étude théorique et expérimentale d’un système de collisions élastiques successives.

Le projet s’appuie sur la modélisation d’un système dynamique composé de deux blocs en interaction, dont le nombre total de collisions encode les décimales de π lorsque le rapport des masses est judicieusement choisi.

Les objectifs sont :

- Comprendre le cadre théorique du phénomène (conservation de l’énergie et de la quantité de mouvement)
- Mettre en œuvre une modélisation numérique et expérimentale du système

---

##  Contenu du dépôt

Vous trouverez dans ce repository :

-  La **MCOT**
-  Le **code Python** utilisé pour les simulations
-  Les **expériences réalisées** ainsi que leurs rapports
-  Les **sources**
-  Le PDF original de l’article de Gregory Galperin (dans le dossier `sources`)

Tous les fichiers présents correspondent à la **version finale et à jour** du projet.

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
