# Éxperience 

---

### Construction d'un banc de test 

#### 1. Première itération : Banc de test initial

Dans un premier temps, j'ai modélisé un **banc de test classique** (Banc1) utilisant des liaisons mécaniques traditionnelles. Cependant, l'analyse géométrique du système a mis en évidence une limitation critique : le manque de résolution et la présence de jeu mécanique au niveau du guidage de l'axe. 

Pour atteindre notre objectif de **31 réflexions** (permettant d'approximer $\pi \approx 3.1$), une précision angulaire de l'ordre du milliradian est requise. Avec l'impression 3D standard, le jeu inhérent aux pièces assemblées aurait rendu le faisceau instable en sortie, chaque micro-vibration modifiant le nombre de rebonds.

<p align="center">
  <img src="Picture/Banc5.png" width="600" alt="Première modélisation du banc de test">
</p>

#### 2. Deuxième itération : Guidage par liaison compliante ("Flexure")

Pour nous affranchir des frottements (phénomène de *stick-slip*) et du jeu mécanique, j'ai réorienté la conception vers une **liaison compliante par guidage flexible (flexure)**, après étude de la documentation technique dédiée à l'optonique de haute précision.

En plus de pousser la précision au niveau micrométrique, cette approche simplifie considérablement la fabrication :
* **Monolithisme :** Le support fixe et le bras mobile sont fusionnés en une seule pièce, ce qui élimine les tolérances d'assemblage et facilite l'impression 3D.
* **Rotation pure :** Le mouvement est obtenu exclusivement par la **déformation élastique** d'une fine membrane de plastique, supprimant tout composant mécanique en friction.
* **Choix du matériau :** Le **PETG** a été sélectionné à la place du PLA standard pour ses excellentes propriétés mécaniques et sa résistance supérieure au fluage (*creep*), évitant que la charnière ne se déforme de manière permanente sous la contrainte de la vis.

#### 3. Mécanisme de réglage et annulation du Backlash

La cinématique a été optimisée en plaçant la charnière flexible à l'apex (la pointe fermée) du V, maximisant ainsi le bras de levier. Le réglage fin de l'angle se fait à l'entrée de la cavité via une vis de pression. 

Bien que la déformation élastique du PETG offre une force de rappel naturelle, j'ai intégré **deux ressorts de compression en opposition**. Ce système applique une précharge constante qui annule le jeu de fond de filet (*backlash*) de la vis et garantit un contact mécanique optimal, fluide et répétable lors des phases de calibration.

<p align="center">
  <img src="Picture/Banc4.png" width="600" alt="Première modélisation du banc de test">
</p>


### Réalisation du banc de test 

Dans un premier temps j'ai découpé des "tranches" de miroirs (20cm*3cm) reprenants les cotes de la modélisation Fusion 


---