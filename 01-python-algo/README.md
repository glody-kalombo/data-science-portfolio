# Analyse de Complexité Algorithmique : Boucle `for` vs `set`

Ce projet illustre l'impact du choix des structures de données et de la complexité algorithmique sur les performances d'un programme Python (recherche de doublons / éléments uniques). Il compare une approche naïve par double boucle avec une approche optimisée utilisant une table de hachage (`set`).

## Objectif

Mesurer et comparer le temps d'exécution de deux méthodes résolvant le même problème sur des listes de tailles croissantes (n = 1_000, n = 5_000, n = 10_000), afin de vérifier expérimentalement les prédictions de la notation Big-O.

## Algorithmes comparés

### 1. Méthode naïve : Boucles `for` imbriquées — $O(n^2)$
* Principe : Pour chaque élément de la liste, on parcourt le reste de la liste pour vérifier s'il est déjà présent.
* Analyse : La double boucle effectue environ n^2/2 comparaisons (n-1, puis n-2, puis n-3). Pour 10_000 éléments, cela représente près de 50 millions de comparaisons.

### 2. Méthode optimisée : Utilisation d'un `set` — $O(n)
* Principe : On parcourt la liste une seule fois en stockant les éléments déjà rencontrés dans un ensemble (`set`).
* Analyse : Chaque vérification (`in seen`) et chaque insertion (`seen.add()`) s'effectue en temps constant O(1) en moyenne grâce au hachage (Python calcule directement l'adresse mémoire de la valeur sans parcourir les éléments).

##  Résultats expérimentaux

Les tests ont été exécutés sur des listes de tailles n = 1_000, n = 5_000 et n = 10_000 :

| Taille de l'entrée (n) | Méthode boucle `for` (O(n^2)) | Méthode avec `set` (O(n)) |
| :--- | :---: | :---: |
| n = 1_000 | `0.042961 s` | `0.000124 s` |
| n = 5_000 | `1.077782 s` | `0.001342 s` |
| n = 10_000 | `3.924097 s` | `0.001066 s` |

## Analyse et cohérence théorique


Lorsque la taille des données n est multipliée par 10 (passage de n = 1_000 à n = 10_000) :

* Pour la boucle `for` :
  3.924097/0.042961 = 91.3
  Le temps d'exécution est multiplié par environ 91, ce qui est cohérent avec la complexité quadratique O(n^2) qui prédit un facteur 10^2 = 100.

* Pour la méthode `set` :
  0.001066/0.000124 = 8.6
  Le temps d'exécution est multiplié par environ 8.6, ce qui correspond à la complexité linéaire O(n) qui prédit un facteur 10.

## Exécution

Assurez-vous d'avoir Python 3 installé sur votre machine, puis lancez le script depuis votre terminal avec la commande suivante :

```bash
python 01-python-algo/duplicates.py
```
