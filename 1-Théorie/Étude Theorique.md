# Étude Théorique Approfondie : Du Billard de Galperin à l'Analogie Optomécanique

## 1. Introduction et Hypothèses Fondamentales du Modèle Idéal

L'objectif de cette étude est d'analyser la dynamique d'un système discret à deux corps en présence d'une frontière rigide, afin d'expliciter le mécanisme mathématique par lequel le nombre total de collisions isole les décimales de $\pi$. Le système d'étude est modélisé sous les hypothèses restrictives suivantes :
* **Unidimensionnalité :** Les mouvements du bloc 1 (masse $m$) et du bloc 2 (masse $M$) sont purement rectilignes le long d'un axe horizontal $(Ox)$.
* **Contrainte de masse :** Les masses vérifient la stricte inégalité $m < M$. Le rapport des masses est paramétré sous la forme $M/m = 100^n$ avec $n \in \mathbb{N}$ afin d'étudier la convergence vers $\pi$.
* **Absence de dissipation :** Le contact entre les blocs et le sol est supposé parfait (liaison glissière sans frottement).
* **Elasticité parfaite :** Les chocs (bloc-bloc et bloc-paroi) sont considérés comme instantanés et parfaitement élastiques, impliquant la conservation intégrale de l'énergie cinétique du système.

Le système est initialisé ainsi : le petit bloc de masse $m$ est immobile ($u_0 = 0$) à une position $x_1 > 0$, tandis que le grand bloc de masse $M$ est situé en $x_2 > x_1$ et possède une vitesse initiale négative $v_0 < 0$ dirigée vers l'origine, où se situe une paroi fixe invisible et infiniment rigide (en $x = 0$).

---

## 2. Formulation Mathématique dans l'Espace des Vitesses Réduites

La dynamique du système entre deux chocs est triviale (mouvement rectiligne uniforme). L'intérêt réside dans la modélisation des transitions discrètes lors des événements de collision.

### 2.1. Équations de Conservation
Pour toute collision entre les deux blocs, deux invariants physiques fondamentaux régissent le changement d'état :
1. **Conservation de l'énergie cinétique ($E$) :**
$$\frac{1}{2} m u^2 + \frac{1}{2} M v^2 = E_0 \quad \text{(constante)}$$

2. **Conservation de la quantité de mouvement ($P$) :**
$$m u + M v = P \quad \text{(constante temporaire durant le choc bloc-bloc)}$$

Lors d'un choc avec la paroi, seule l'énergie cinétique est conservée, la quantité de mouvement du système variant sous l'effet de l'impulsion de la force de réaction de la paroi.

### 2.2. Le Changement de Variables Bijectif (Espace des Phases)
Afin de symétriser l'équation quadratique de l'énergie, on introduit un espace de configuration abstrait, appelé espace des vitesses réduites, via le changement de variables suivant :
$$X = \sqrt{m} u \quad \text{et} \quad Y = \sqrt{M} v$$

En substituant ces expressions dans l'équation de conservation de l'énergie, on obtient immédiatement :
$$X^2 + Y^2 = 2E_0$$

D'un point de vue topologique, cette équation est celle d'un **cercle parfait** $\Gamma$ de rayon $R = \sqrt{2E_0}$ dans le plan $(X, Y)$. Par conséquent, l'état cinématique global du système à tout instant est astreint à se déplacer exclusivement sur le périmètre de ce cercle. Chaque collision induit un saut discret d'un point à un autre de la courbe.

---

## 3. Analyse Géométrique des Collisions

L'évolution du système se décompose en une alternance stricte de deux types d'opérations géométriques sur le cercle d'énergie $\Gamma$.

### 3.1. Choc Bloc-Paroi (Transformation $T_{\text{paroi}}$)
Lorsque le petit bloc frappe la paroi fixe à l'origine, sa vitesse s'inverse instantanément par élasticité ($u \to -u$), tandis que la vitesse du grand bloc $M$ demeure inchangée ($v \to v$). Dans l'espace des vitesses réduites, cette transformation se traduit par :
$$X_{\text{après}} = -X_{\text{avant}} \quad \text{et} \quad Y_{\text{après}} = Y_{\text{avant}}$$

Géométriquement, l'opérateur $T_{\text{paroi}}$ correspond à une **symétrie axiale par rapport à l'axe des ordonnées $(OY)$**.

### 3.2. Choc Bloc-Bloc (Transformation $T_{\text{bloc}}$)
Lors du contact entre les deux masses, la quantité de mouvement se conserve. Exprimons cette contrainte dans notre système de coordonnées réduites :
$$\sqrt{m}X + \sqrt{M}Y = P \implies Y = -\sqrt{\frac{m}{M}} X + \frac{P}{\sqrt{M}}$$

Cette relation définit une famille de droites parallèles de pente fixe $a = -\sqrt{\frac{m}{M}}$. L'état du système doit satisfaire simultanément la conservation de l'énergie et celle de la quantité de mouvement. Le passage de l'état initial à l'état final lors d'un choc se fait donc le long de cette droite sécante au cercle. 

Par propriété des cordes d'un cercle, l'application successive de la contrainte linéaire de mouvement et de la contrainte quadratique d'énergie équivaut à une **symétrie axiale par rapport à une droite orthogonale à la droite de quantité de mouvement**, passant par l'origine. Sa pente est inclinée d'un angle $\theta$ par rapport à l'horizontale, tel que :
$$\tan(\theta) = \sqrt{\frac{m}{M}}$$

### 3.3. Composition des Mouvements et Théorème de l'Angle Inscrit
La dynamique globale est la composition alternée de deux réflexions axiales : $R_{\text{bloc}}$ (par rapport à la droite inclinée d'un angle $\theta$) et $R_{\text{paroi}}$ (par rapport à l'axe vertical, incliné à $\pi/2$). 

D'après le cours de géométrie euclidienne, la composition de deux réflexions axiales dont les axes s'intersectent en l'origine avec un angle conceptuel $\Delta \phi$ engendre une **rotation pure** autour de l'origine d'un angle égal à $2\Delta \phi$. Ici, l'angle entre l'axe vertical et la droite de choc est directement lié à $\theta$.

En appliquant le **Théorème de l'angle inscrit**, on démontre que chaque paire de collisions (un choc bloc-bloc suivi d'un choc bloc-paroi) déplace le point représentatif le long du cercle d'un arc de longueur angulaire constante et égale à $2\theta$.

### 3.4. Condition d'Arrêt et Isolement de $\pi$
Le processus de collision s'interrompt définitivement lorsque les conditions cinématiques n'autorisent plus aucun contact futur. Cela se produit lorsque les deux blocs se dirigent vers la droite ($u \ge 0$ et $v \ge 0$) et que le grand bloc s'éloigne plus vite que le petit ne peut le suivre, soit la condition de fuite :
$$v \ge u \implies \frac{Y}{\sqrt{M}} \ge \frac{X}{\sqrt{m}} \implies Y \ge \sqrt{\frac{M}{m}} X$$

Dans l'espace des phases, cette condition délimite une "zone d'arrivée". Le point d'état commence sa course tout à gauche du cercle (vitesse initiale du grand bloc négative, $u_0 = 0$) et progresse par rotations successives d'angle $2\theta$. Le nombre maximal de réflexions $N$ correspond au nombre d'arcs de longueur $\theta$ nécessaires pour balayer le demi-périmètre du cercle (soit un angle plat de $\pi$ radians) sans basculer dans la zone de non-collision.

On obtient mathématiquement :
$$N = \left\lfloor \frac{\pi}{\theta} \right\rfloor = \left\lfloor \frac{\pi}{\arctan\left(\sqrt{\frac{m}{M}}\right)} \right\rfloor$$

Au voisinage des grands rapports de masse ($M \gg m$), on peut effectuer un développement limité à l'ordre 1 de la fonction arc-tangente :
$$\arctan\left(\sqrt{\frac{m}{M}}\right) \approx \sqrt{\frac{m}{M}} = \frac{1}{10^n}$$

En injectant cette approximation dans l'expression de $N$, il vient :
$$N \approx \left\lfloor \pi \times 10^n \right\rfloor$$

Pour $n=1$ ($M = 100m$), $N = \lfloor 31,415... \rfloor = 31$ collisions.

---

## 4. Extension : Les Limites de l'Approche Mécanique et l'Effet de la Dissipation

Pour élever cette étude aux standards d'une démarche de recherche, il est indispensable d'analyser le comportement du système en présence de non-idéalités, ce qui justifie scientifiquement ton changement de paradigme vers l'optique.

### 4.1. Modélisation de la Perte d'Énergie (Invariance de jauge brisée)
Introduisons un coefficient de restitution cinématique $e \in [0, 1[$ pour caractériser l'inélasticité des chocs (où $e = 1$ est le cas idéal). Lors d'un choc, la vitesse relative après impact est amortie :
$$(u_{\text{après}} - v_{\text{après}}) = -e (u_{\text{avant}} - v_{\text{avant}})$$

À chaque transition discrète, l'énergie cinétique totale $E$ décroit d'une quantité $\Delta E$ proportionnelle à $(1-e^2)$. 

### 4.2. Conséquence Topologique : La Spirale Logarithmique Rentrante
Dans l'espace des phases $(X,Y)$, le rayon du cercle est directement lié à l'énergie par $R = \sqrt{2E}$. Puisque $E$ diminue strictement à chaque choc bloc-bloc et bloc-paroi, le point représentatif du système ne saute plus sur un cercle invariant, mais migre vers des orbites de rayons de plus en plus faibles. 

L'analogie géométrique montre que la trajectoire décrit une **spirale rentrante (ou discontinue) convergeant vers l'origine $(0,0)$**. 

**Conséquence métrologique :** À cause de cette contraction géométrique, l'angle effectif balayé change et le système atteint la condition d'arrêt prématurément, ou s'amortit complètement avant d'avoir pu effectuer le nombre requis de rotations. Il est donc impossible en pratique d'extraire proprement les décimales de $\pi$ avec des masses macroscopiques subissant le frottement sec et l'inélasticité.

---

## 5. Le Changement de Paradigme : L'Isomorphisme de l'Analogie Optique

Pour contourner la barrière physique de la dissipation mécanique, la démarche consiste à projeter le problème mathématique dans l'espace des positions et à exploiter la propagation de la lumière, par nature exempte de dégradation de type *stick-slip*.

### 5.1. Espace Configurationnel Réduit
Considérons les positions instantanées du petit bloc ($x_1$) et du grand bloc ($x_2$) le long du rail. De la même manière que pour les vitesses, on applique un redimensionnement pondéré par la racine carrée des masses afin de préserver l'isométrie du système :
$$X_{\text{pos}} = \sqrt{m} x_1 \quad \text{et} \quad Y_{\text{pos}} = \sqrt{M} x_2$$

Dans cet espace $(X_{\text{pos}}, Y_{\text{pos}})$, le mouvement libre du système entre deux chocs se traduit par un déplacement rectiligne uniforme, représenté par une **ligne droite continue**.

### 5.2. Formalisation des Frontières Physiques en Frontières Optiques
Les contraintes d'espace du problème mécanique se traduisent par deux frontières géométriques infranchissables :
1. **La présence de la paroi en $x_1 = 0$ :** En coordonnées réduites, cela correspond strictement à la droite verticale d'équation :
$$X_{\text{pos}} = 0 \quad \text{(Axe des ordonnées)}$$
2. **L'impénétrabilité des blocs ($x_2 \ge x_1$) :** En injectant les variables réduites, on obtient la condition $ \frac{Y_{\text{pos}}}{\sqrt{M}} \ge \frac{X_{\text{pos}}}{\sqrt{m}} $, ce qui définit une droite frontière d'équation :
$$Y_{\text{pos}} = \sqrt{\frac{M}{m}} X_{\text{pos}}$$

Ces deux droites s'intersectent à l'origine $(0,0)$ et forment une ouverture angulaire en "V", appelée un **dièdre de réflexion**. L'angle au sommet $\alpha$ de ce coin est le complémentaire de la pente de la seconde droite, ce qui redonne précisément :
$$\tan(\alpha) = \sqrt{\frac{m}{M}} \implies \alpha = \theta = \arctan\left(\sqrt{\frac{m}{M}}\right)$$

### 5.3. Équivalence avec la Loi de Descartes (Réflexion Spéculaire)
La conservation de l'énergie et de la quantité de mouvement impose que le vecteur vitesse du point représentatif dans l'espace $(X_{\text{pos}}, Y_{\text{pos}})$ conserve sa norme lors d'un impact sur l'une des deux frontières, et que l'angle d'incidence par rapport à la normale de la frontière soit strictement égal à l'angle de réflexion.

Ce comportement est l'analogue mathématique exact de la **loi de Snell-Descartes pour la réflexion spéculaire d'un rayon lumineux**. Le système mécanique de Galperin est donc mathématiquement isomorphe à un rayon de lumière piégé à l'intérieur d'un angle formé par deux miroirs plans parfaits inclinés d'un angle $\theta$.

Le nombre de chocs physiques des blocs est rigoureusement égal au nombre de réflexions optiques du faisceau laser avant qu'il ne ressorte du dièdre. L'optique géométrique permet d'éliminer la flèche temporelle de la dissipation mécanique et d'obtenir un calcul stationnaire pur, ouvrant la voie à une mesure expérimentale de haute précision par imagerie.
