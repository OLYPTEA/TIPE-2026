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

Or, la pente de notre droite de quantité de mouvement nous donne la relation $\tan(\theta) = \sqrt{\frac{m_1}{m_2}}$. Pour des rapports de masses de la forme $\frac{m_2}{m_1} = 100^n$, l'angle $\theta$ devient très petit ($\theta \approx 10^{-n}$), ce qui permet au nombre $N$ d'encoder parfaitement les décimales de $\pi$.

---

## Les limites de l'approche mécanique

Bien que ce modèle théorique soit mathématiquement exact, sa mise en œuvre expérimentale se heurte rapidement à la réalité physique.

Le modèle suppose une absence totale de frottements et des chocs parfaitement élastiques ($E = constante$). Dans la réalité, une infime fraction de l'énergie cinétique est dissipée à chaque collision (frottements solides, déformation inélastique, bruit).

Dans l'espace des vitesses réduites, cette dissipation se traduit graphiquement : le point représentatif de l'état du système ne saute plus sur le même cercle, mais sur des cercles de plus en plus petits. Le beau cercle parfait de l'énergie conservée se transforme en une **spirale rentrante** convergeant vers l'origine.
Le système s'arrête alors bien avant d'avoir pu accumuler les rotations nécessaires pour former le nombre $\pi$.

---

## Le changement de paradigme : L'Analogie Optique

Pour contourner ce problème de dissipation mécanique, il est possible de changer d'espace de représentation, passant d'un problème de *dynamique des masses* à un problème de *géométrie pure*.

### 🔹 Passage à l'espace des positions

Appliquons le même redimensionnement (par la racine des masses) non plus aux vitesses, mais aux **positions** des deux blocs :

$$
X = \sqrt{m_1} x_1 \quad \text{et} \quad Y = \sqrt{m_2} x_2
$$

Dans cet espace $(X, Y)$, le mouvement des blocs entre deux chocs est rectiligne uniforme : le système est représenté par un point qui se déplace en **ligne droite**.

Les contraintes physiques du système deviennent des frontières géométriques :
1.  **Le mur fixe ($x_1 \ge 0$) :** Dans notre nouvel espace, cela correspond à l'axe vertical $X = 0$.
2.  **L'impénétrabilité des blocs ($x_2 \ge x_1$) :** En remplaçant par nos variables réduites, on obtient la droite d'équation $Y = \sqrt{\frac{m_2}{m_1}} X$.

### 🔹 Le dièdre de réflexion

Ces deux droites ($X=0$ et $Y = \sqrt{\frac{m_2}{m_1}} X$) se croisent à l'origine et forment un coin en forme de "V" (un dièdre). L'angle au sommet de ce dièdre est exactement l'angle $\theta$ défini précédemment :

$$
\theta = \arctan\left(\sqrt{\frac{m_1}{m_2}}\right)
$$

Puisque nous avons démontré (dans l'espace des vitesses) que l'énergie et la quantité de mouvement se conservent, la vitesse d'approche relative de notre point sur ces droites est égale à sa vitesse d'éloignement.
Le rebond du point représentatif du système sur ces frontières obéit donc strictement à la **loi de la réflexion spéculaire** (angle d'incidence = angle de réflexion).

### 🔹 Conclusion théorique

L'évolution de nos deux masses en collision est mathématiquement **strictement équivalente** au parcours d'un rayon lumineux projeté à l'intérieur d'un angle formé par deux miroirs plans.
Le nombre de chocs mécaniques devient alors le nombre de **réflexions optiques**. Cette analogie permet de s'affranchir totalement des problèmes de frottements solides et de pertes d'énergie inélastiques propres à la mécanique matérielle.



