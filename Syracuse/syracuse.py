## Initiation à python: problème de Syracuse et premiers jumeaux
## =============================================================

## Partie I: Syracuse
## ==================

## Dans le problème de Syracuse (aussi appelé $3n+1$), on part d'un entier $n$, et on passe
## à l'entier suivant par la règle suivante:
## * si $n$ est pair, l'entier suivant est $\frac{n}{2}$
## * si $n$ est impair, l'entier suivant est $3\times n + 1$
## Par exemple, si on part de l'entier $7$, la séquence est la suivante:
## $7 \to 22 \to 11 \to 34 \to 17 \to 52 \to 26 \to 13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$.
## Une fois que l'on arrive sur $1$, le processus boucle: $1 \to 4 \to 2 \to 1 \to \dots$
## On conjecture que pour tout les nombres entiers, ce processus tombe toujours sur $1$ au bout d'un moment.
## À ce jour, personne n'a réussi à le démontrer. Mais des ordinateurs très puissants ont vérifié cette
## conjecture pour des nombres très très grands et l'on n'a pas trouvé de contre-exemple.

## On va faire un petit programme en python pour tester la conjecture de Syracuse.

## Recommendation générale
## -----------------------

## * En cas d'erreur, lire le message d'erreur en anglais, en commançant par la fin
## * Testez toutes vos fonctions dans la console avant de passer à la question suivante.

## Question I.1
## ------------

## Écrire une fonction ``suivant_syracuse`` qui renvoie l'entier
## suivant dans le problème de Syracuse.
## indications pour se référer au cours:
## * Il faut ``def`` et ``return``
## * Il faut ``if`` et ``else``
## * Il faut le modulo $2$ (reste de la division par $2$) un entier $n$ est pair si et seulement si ``n % 2 == 0``
##   c'est à dire si le reste de la division par $2$ est 0
## * Il faut utiliser la division entière par $2$ et non pas la division réelle: ``6 // 2`` donne l'entier ``3``
##   alors que ``6 / 2`` donne le réel ``3.0``. Dans le problème de Syracuse, il faut rester avec des nombres entiers,
##   car sinon, avec les nombres réels, on risque d'avoir des erreurs d'arrondi.
## * N'oublier pas: le test d'égalité en python c'est ``n == 0`` et non ``n = 0``

def suivant_syracuse(n):
    """Donne le nombre suivant n dans le problème de Syracuse"""
    pass

## Question I.2
## ------------

## Écrire une fonction ``longueur_syracuse`` qui donne le nombre d'étapes pour arriver à $1$.
## Votre function appliquera la
## précédente à partir d'un entier initial fourni en argument et s'arrêtera en
## renvoyant le nombre d'étapes.
## Indications:
## * il vous faut une boucle ``while``.
## * il vous faut une variable pour compter le nombre d'étapes.

def longueur_syracuse(n):
    """Renvoie le nombre d'étapes de n à 1 dans le processus de Syracuse"""
    pass

## ``assert`` est une fonction qui vérifie qu'une condition est vraie et qui
## arrête le programme immédiatement dans le cas contraire. On l'utilise pour
## vérifier qu'un programme fait ce que l'on attend de lui.
## La fonction doit vérifier (décommenter ces lignes quand le code est fini):

## ``assert`` est une fonction qui vérifie qu'une condition est vraie et qui
## arrête le programme immédiatement dans le cas contraire. On l'utilise pour
## vérifier qu'un programme fait ce que l'on attend de lui.
## La fonction doit vérifier (décommenter ces lignes quand le code est fini):

## ``assert`` est une fonction qui vérifie qu'une condition est vraie et qui
## arrête le programme immédiatement dans le cas contraire. On l'utilise pour
## vérifier qu'un programme fait ce que l'on attend de lui.
## La fonction doit vérifier (décommenter ces lignes quand le code est fini):

## ``assert`` est une fonction qui vérifie qu'une condition est vraie et qui
## arrête le programme immédiatement dans le cas contraire. On l'utilise pour
## vérifier qu'un programme fait ce que l'on attend de lui.
## La fonction doit vérifier (décommenter ces lignes quand le code est fini):

## ``assert`` est une fonction qui vérifie qu'une condition est vraie et qui
## arrête le programme immédiatement dans le cas contraire. On l'utilise pour
## vérifier qu'un programme fait ce que l'on attend de lui.
## La fonction doit vérifier (décommenter ces lignes quand le code est fini):

#assert(longueur_syracuse(1)==0)
#assert(longueur_syracuse(2)==1)
#assert(longueur_syracuse(5)==5)
#assert(longueur_syracuse(7)==16)

## Question I.3
## ------------

## Écrire une fonction ``cherche_syracuse`` qui prend un entier $n$ en argument et calcule
## le premier entier qui met $n$ étapes ou plus pour arriver à $1$.
## Indication:
## * Il vous faut une boucle ``while``.

def cherche_syracuse(n):
    """Renvoie le premier entier qui met n étapes ou plus pour revenir à 1 dans Syracuse."""
    pass

## Question I.4
## ------------

## Écrire une fonction ``plus_long_syracuse`` qui prend un entier $n$ en argument et calcule
## l'entier entre $1$ et $n$ qui met le plus longtemps à arriver à $1$. Si deux entiers
## mettent le même nombre d'étapes pour arriver à $1$, on renvoie le plus petit.

## Indication:
## * Il vous faut une boucle ``for`` et un ``if`` dans le bloc du ``for``

def plus_long_syracuse(n):
    """Renvoie l'entier entre 1 et n qui met le plus de temps pour revenir à 1 dans Syracuse"""
    pass

## Partie II: Les jumeaux
## ======================

## Un entier premier est un nombre qui n'est divisible que par $1$ et lui même.
## C'est à dire que si $p$ est premier et que $p = a * b$ et que $a$ et $b$ sont
## des entiers positifs, on a forcément $a=1$ et $b=p$ ou l'inverse.
## Les premiers nombres premiers sont
## $2,3,5,7,11,13,17,19,23,29,31,\dots$.

## Une paire de nombres premiers jumeaux, ce sont deux nombres premiers $p_1$ et
## $p_2$ avec $p_2 - p_1 = 2$. Comme par exemple $(3,5), (5,7), (11,13),
## (17,19), (29,31),  \dots$

## On démontre assez facilement qu'il y a une infinité de nombres premiers. Par
## contre, on ne sait toujours pas si il y a une infinité de paires de nombres
## premiers jumeaux. Au fur et à mesure que la puissance de calcul des ordinateurs
## augmente on trouve des paires de jumeaux de plus en plus grande.

## Rappel: pour vérifier que $a$ divise $b$ is suffit de vérifier que le reste de
## le division de $b$ par $a$ est $0$, ce qui s'écrit en python:
## ``b % a == 0``

## Question II.1
## -------------

## Écrire une fonction ``divisible(b,a)`` qui renvoie ``True`` si $b$ est divisible
## par $a$

def divisible(b,a):
    """renvoie True si a divise b, sinon False."""
    pass

## Question II.2
## -------------

## Écrire une fonction ``est_premier`` qui renvoie True si son argument est premier.
## remarque: pour aller plus vite, on peut remarquer si si $n$ n'est pas premier,
## on peut toujours trouver un diviseur $a>1$ qui vérifie $a*a <= n$.

## Indication, on peut utiliser une boucle ``for`` si on test tous les diviseurs
## entre $2$ et $n-1$ ou une boucle ``while`` si on veut utiliser l'astuce ci-dessus.

def est_premier(n):
    """renvoie True si n est premier"""
    pass

## Question II.3
## -------------

## Écrire une fonction ``premier_suivant`` qui prend un argument $n$
## et renvoie le plus petit nombre premier plus grand que $n$.

def premier_suivant(n):
    """renvoie le plus petit nombre premier supérieur ou égal à n."""
    pass

## Question II.4
## -------------

## Écrire une fonction ``jumeaux_suivants`` qui prend un argument $n$
## et renvoie le plus petit nombre $p$ plus grand que $n$ tel que
## $p$ et $p+2$ soient premiers tous les deux.

def jumeaux_suivants(n):
    """renvoie le plus petit nombre premier supérieur ou égal à n."""
    pass

