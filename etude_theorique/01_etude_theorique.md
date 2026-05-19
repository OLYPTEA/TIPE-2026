##  Modélisation théorique du système

Considérons deux blocs de masses respectives $m_1$ et $m_2$ en translation rectiligne suivant l’axe des $x$, avec :

$$
m_1 < m_2
$$

On suppose que :

- Les deux blocs glissent parfaitement sur le sol (absence de frottements)
- Les collisions sont parfaitement élastiques
- Il n’y a aucune dissipation d’énergie

---

##  Théorèmes et relations fondamentales

### 🔹 Conservation de l’énergie cinétique

$$
\frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2 = E
$$

avec $E$ constante.

---

###  Conservation de la quantité de mouvement

$$
m_1 v_1 + m_2 v_2 = P
$$

avec $P$ constante.

---

###  Théorème des angles inscrits

Soient $A$, $B$ et $M$ trois points distincts, et $\Gamma$ un cercle de centre $O$ passant par $A$ et $B$.

Le point $M$ appartient à $\Gamma$ si et seulement si :

$$
(OA, OB) \equiv 2 (MA, MB) \pmod{2\pi}
$$

Autrement dit, l’angle au centre est égal au double de l’angle inscrit.

---

##  Idée clé : représentation géométrique

L’idée fondamentale consiste à représenter la vitesse du bloc 1 en fonction de la vitesse du bloc 2.

En effet, d’après la conservation de l’énergie :

$$
\frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2 = E
$$

Ce qui donne :

$$
m_1 v_1^2 + m_2 v_2^2 = 2E
$$

On peut alors écrire :

$$
(\sqrt{m_1} v_1)^2 + (\sqrt{m_2} v_2)^2 = 2E
$$

En posant :

$$
x = \sqrt{m_1} v_1
\quad \text{et} \quad
y = \sqrt{m_2} v_2
$$

On obtient :

$$
x^2 + y^2 = 2E
$$

---

##  Interprétation géométrique

L’équation obtenue est celle d’un **cercle** dans le plan $(x, y)$.

Ainsi, la dynamique des collisions peut être interprétée comme une succession de réflexions sur un cercle, ce qui établit un lien direct entre :

- la géométrie du cercle  
- les rotations successives  
- et l’apparition du nombre $\pi$

Cette reformulation géométrique constitue le cœur du lien entre le nombre total de collisions et les décimales de $\pi$.

## Résultats numérique

D'après le programme Python présent dans le dossier **CODE**, on peut tracer la vitesse du bloc 1 en fonction de la vitesse du bloc 2 *(ici m1 = 1Kg et m2 = 100Kg)*.

On obtient la figure ci-dessous :

<p align="center">
  <img src="../Picture\ImagePythonTIPE.png" width="600">
</p>

Les points représentent les collisions successives entre les deux blocs.  
Le but est donc de **compter ces points** afin de déterminer le nombre total de collisions.

## Interpretation géometrique

Maintenant expliquons plus en details cette figure :
  -Au debut, le bloc 2 a une vitesse négative donc on se situe sur la partie gauche du plan, le bloc 1 quant à lui est immobile donc v1 = 0, on par donc du point le plus à gauche du cercle (angle de pi).

 <p align="center">
  <img src="../Picture\ETAPE1.png" width="600">
</p>


  -Lors de la première collision le bloc 1 prend une certaine vitesse *(négative car vers la gauche)* donc le point va se deplacer quelque part la où y est négatif, tandis que le bloc 2 perd un peu de vitesse donc la coordonnée x va se rapprocher un peu de 0 :

<p align="center">
  <img src="../Picture\ETAPE2.png" width="600">
</p>

  On peux trouver sa position exact à partir de la conservation de quantité de mouvement, avec les changement de coordonnées :

$$
  m_1 v_1 + m_2 v_2 = P
$$

$$
  (\sqrt{m_1})*(\sqrt{m_1} v_1) + (\sqrt{m_2})*(\sqrt{m_2} v_2) = P
$$

$$
  (\sqrt{m_1})*x + (\sqrt{m_2})*y = P
$$


On a ici une **équation linéaire** en x et y  :

<p align="center">
  <img src="../Picture\ETAPE3.png" width="600">
</p>

Cette droite a pour pente :

$$
y = (-\sqrt{m_1/m_2})*x
$$

Les points du cercle formés par l'intersection entre la droite et le cercle reprénsentent un couple de vitesses qui ont à la fois la meme énergie cinétique et la meme quantité de mouvement. Ainsi quand les deux blocs s'entrechoquent ont sautent d'un point à l'autre.

<p align="center">
  <img src="../Picture\ETAPE4.png" width="600">
</p>

  Et ansi de suite...


Maintenant il faut compter le nombre de segments que l'on trace avant la **zone d'arrivé**, c'est à dire quand la vitesse du bloc1 est inferieur à la vitesse du bloc 2 :

<p align="center">
  <img src="../Picture\ETAPE5.png" width="600">
</p>


On peux **decouper** le cercle en plusieurs arcs de cercles, ces arcs semblent tous égaux en longeurs et ils le sont :

<p align="center">
  <img src="../Picture\ETAPE6.png" width="600">
</p>

On le montre avec le théorme des angles inscrits :

<p align="center">
  <img src="../Picture\ETAPE7.png" width="600">
</p>

Chaque arc a donc une longueur de 2θ, et on compte le nombre d'arcs de longueur 2θ que l'on peut mettre pour recouvrir le périmètre du cercle de sorte à ce qu'en ajouter un de plus nous ferait dépasser le périmètre du cercle. Cette derniere proposition est équivalente à :

$$
\sum_{k=1}^{N} 2\theta \<\ 2\pi
$$

C'est à dire :

$$
 N\theta \<\ 2\pi
$$



