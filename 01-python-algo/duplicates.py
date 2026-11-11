"""Vérifie le temps d'exécution des fonctions et décrit la différence entre ces temps"""

import time


def has_duplicates_naive(items):
    """Retourne True si une valeur se répète en comparant chaque élément à tous ceux qui le suivent"""
    # deux boucles imbriquées
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True  # doublon trouvé, on arrête tout
    return False


def has_duplicates_fast(items):
    """Retourne True si une valeur se répète, parcourt la liste une seule fois et retient dans un set les éléments déjà vus"""
    # Un set des éléments déjà vus
    seen = set()

    for item in items:
        if item in seen:
            return True  # Doublon trouvé, on s'arrête ici
        seen.add(item)

    return False


def measure(func, items):
    """Retourne le temps d'exécution de func(items), en secondes."""
    start = time.perf_counter()
    func(items)
    elapsed = time.perf_counter() - start
    return elapsed


def main():
    """Vérifie les deux fonctions, puis mesure leur temps d'exécution."""
    for n in (1_000, 5_000, 10_000):
        items = list(range(n))
        print(f"Le calcul du temps d'exécution avec n = {n}")
        print(f"Méthode avec la boucle for : {measure(has_duplicates_naive, items):.6f} secondes")
        print(f"Méthode avec set : {measure(has_duplicates_fast, items):.6f} secondes")


if __name__ == "__main__":
    main()
