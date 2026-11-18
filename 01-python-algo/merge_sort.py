"""Exécute la récursivité et le tri fusion"""

import random
import time

def factorial(n):
    """Execute la réursivité sur un entier positif"""
    if n < 0:
        raise ValueError("Le nombre doit être positif ou nul.")

    # cas de base
    if n == 0:
        return 1

    # cas reursif
    return n * factorial(n - 1)


def merge(left, right):
    """Retourne une liste triée à partir des 2 listes triées"""
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Ajouter les éléments restants de left
    while i < len(left):
            result.append(left[i])
            i += 1

    # Ajouter les éléments restants de right
    while j < len(right):
            result.append(right[j])
            j += 1

    return result


def merge_sort(items):
     """Divise la liste en 2 et fait la fusion après le tri"""
     if len(items) <= 1:
          return items.copy()

     # Diviser la liste en 2 parties
     mid = len(items) // 2
     left = items[:mid]
     right = items[mid:]

     # Trier récursivement les deux parties
     left_sorted = merge_sort(left)
     right_sorted = merge_sort(right)

     # Fusionner les 2 listes triées
     return merge(left_sorted, right_sorted)


def main():
     """Effectue des tests des fonctions du programme"""
     # Vérifications avec assert
     random.seed(42)

     # Tests de factorial
     assert factorial(0) == 1
     assert factorial(1) == 1
     assert factorial(5) == 120

     # Tests de merge
     assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
     assert merge([], [1, 2, 3]) == [1, 2, 3]
     assert merge([1, 2, 3], []) == [1, 2, 3]

     # Test merge_sort
     assert merge_sort([]) == []
     assert merge_sort([5]) == [5]
     assert merge_sort([1, 2, 3, 4]) == [1, 2, 3, 4]
     assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
     assert merge_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]
     assert merge_sort([-5, 3, -1, 0, -10]) == [-10, -5, -1, 0, 3]

     # Vérifier que la liste originale n'est pas modifiée
     original = [5, 2, 8, 1, 3]
     copy_original = original.copy()

     result = merge_sort(original)

     assert original == copy_original
     assert result == [1, 2, 3, 5, 8]

     # Test avec 1000 nombres aléatoires
     items = [random.randint(-10_000, 100_000) for _ in range(1_000)]

     assert merge_sort(items) == sorted(items)

     print("Tous les tests sont réussis !")

     # ===================================
     # 2. MESURE DES PERFORMANCES
     # ===================================

     sizes = [1_000, 100_000, 1_000_000]

     print("\nComparaison des performances :")
     print("-" * 65)
     print(f"{'Taille (n)':15}{'merge_sort (s)':<25}{'sorted() (s)':<20}")
     print("-" * 65)

     for n in sizes:
          # Créer une liste mélangée
          items =  list(range(n))
          random.shuffle(items)

          # Mesurer merge_sort
          start = time.perf_counter()
          merge_sort(items)
          end = time.perf_counter()

          merge_time = end - start

          # Mesurer sorted()
          start = time.perf_counter()
          sorted(items)
          end = time.perf_counter()

          sorted_time = end - start

          # Afficher les resultats
          print(f"{n:<15}{merge_time:<25.6f}{sorted_time:<20.6f}")



if __name__ == "__main__":
     main()
    