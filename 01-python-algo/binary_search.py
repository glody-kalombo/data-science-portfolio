"""Execute la recherche dichotomique"""

import time


def linear_search(items, target):
    """Retourne l'indice de target dans un items"""
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def binary_search(items, target):
    """Retourne l'indice de target dans un items"""
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = items[mid]

        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def measure(func, *args):
    """Mesure le temps d'exécution d'une fonction"""
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start


def main():
    """Fait une comparaison entre la recherche linéaire et dichotomique"""
    numbers = [10, 20, 30, 40, 50]

    # Tests des assert pour binary_search

    # La cible est le premier élément
    assert binary_search(numbers, 10) == 0

    # La cible est le dernier élément
    assert binary_search(numbers, 50) == 4

    # La cible est au milieu
    assert binary_search(numbers, 30)  == 2

    # La cible est absente et plus petite que tout
    assert binary_search(numbers, 4) == -1

    # la cible est absente et plus grande que tout
    assert binary_search(numbers, 99) == -1

    # La cible est absente mais entre deux
    assert binary_search(numbers, 35) == -1

    # La liste est vide
    assert binary_search([], 85) == -1

    # La liste ne contient qu'un seul élément (présent)
    assert binary_search([86], 86) == 0

    # La liste ne contient qu'un seul élément (absent)
    assert binary_search([48], 50) == -1

    # Tests des assert avec linear_search

    # La cible est le premier élément
    assert linear_search(numbers, 10) == 0

    # La cible est le dernier élément
    assert linear_search(numbers, 50) == 4

    # La cible est au milieu
    assert linear_search(numbers, 30)  == 2

    # La cible est absente et plus petite que tout
    assert linear_search(numbers, 4) == -1

    # la cible est absente et plus grande que tout
    assert linear_search(numbers, 99) == -1

    # La cible est absente mais entre deux
    assert linear_search(numbers, 35) == -1

    # La liste est vide
    assert linear_search([], 85) == -1

    # La liste ne contient qu'un seul élément (présent)
    assert linear_search([86], 86) == 0

    # La liste ne contient qu'un seul élément (absent)
    assert linear_search([48], 50) == -1

    print("Toutes les vérifications assert ont réussi avec succès.\n")

    # La mesure des performances
    sizes = [1_000, 100_000, 1_000_000]

    # En-tête du tableau aligné
    print(f"{'Taille (n)':>12} | {'Linear Search (s)':>18} | {'Binary Search (s)':>18}")
    print("-" * 54)

    for n in sizes:
        items = list(range(n))
        target = n

        t_linear = measure(linear_search, items, target)
        t_binary = measure(binary_search, items, target)

        print(f"{n:12,d} | {t_linear:18.6f} | {t_binary:18.6f}")


if __name__ == "__main__":
    main()
measure
