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

## Analyse géométrique

D'après le programme Python présent dans le dossier **CODE**, on peut tracer la vitesse du bloc 1 en fonction de la vitesse du bloc 2 *(ici $m_1 = 1\,kg$ et $m_2 = 100\,kg$)*.

On obtient la figure ci-dessous :

<p align="center">
  <img src="../ImagePythonTIPE.png" width="600">
</p>

Les points représentent les collisions successives entre les deux blocs.  
Le but est donc de **compter ces points** afin de déterminer le nombre total de collisions.





