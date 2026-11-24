"""Vérificateur de parenthèses et simulation de files d'attente."""

from collections import deque


def is_balanced(text):
    """Vérifie si les parenthèses, crochets et accolades sont fermés."""
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    opening = "([{"

    for char in text:

        # Cas 1 : symbole ouvrant
        if char in opening:
            stack.append(char)

        # Cas  : symbole fermant
        elif char in pairs:

            # Vérifie si la pile est vide
            if not stack:
                return False

            # Vérifie si le dernier ouvrant correspond
            if stack[-1] != pairs[char]:
                return False

            # Retirer le symbole ouvrant de la pile
            stack.pop()

    # Tous les symboles doivent avoir étés fermés
    return len(stack) == 0


def serve_all_list(n):
    """Sert n clients dans l'ordre d'arrivée avec une liste."""

    # Créer la file de clients
    queue = list(range(n))
    served = []

    # Servir les clients dans l'ordre d'arrivée
    while queue:
        client = queue.pop(0)
        served.append(client)

    return served


def serve_all_deque(n):
    """Sert n clients dans l'ordre d'arrivée avec un deque."""

    # Créer la file des clients
    queue = deque(range(n))
    served = []

    # Servir les clients dans l'ordre d'arrivée
    while queue:
        client = queue.popleft()
        served.append(client)

    return served

def run_checks():
    """Exécute les tests unitaires avec des assertions."""

    # Vérifier is_balanced()
    assert is_balanced("()") == True
    assert is_balanced("([])") == True
    assert is_balanced("{[()]}") == True
    assert is_balanced("([)]") == False
    assert is_balanced("(()") == False
    assert is_balanced(")") == False

    # Vérification des deux fils avec n = 10
    result_list = serve_all_list(10)
    result_deque = serve_all_deque(10)

    assert result_list == result_deque
    assert result_list == list(range(10))

    print("Tous les tests sont réussis !")


def main():
    """Orchestre les tests, démonstrations et mesures de temps."""

    print("=== VERIFICATION DES FONCTIONS ===")

    # Exécuter les tests
    run_checks()

    print("\n=== FILE AVEC LIST ===")

    # Servire 10 clients avec une liste
    result_list = serve_all_list(10)
    print("Clients servis :", result_list)

    print("\n=== FILE AVEC DEQUE ===")

    # Servire 10 clients avec deque
    result_deque = serve_all_deque(10)
    print("Clients servis :", result_deque)

    # Comparer les résultats
    if result_list == result_deque:
        print("Les 2 méthodes donnent le même résultat.")
    else:
        print("Les résultats sont différents")


if __name__ == "__main__":
    main()
