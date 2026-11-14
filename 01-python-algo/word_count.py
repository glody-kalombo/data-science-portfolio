"""Compte la fréquence des mots d'un texte et affiche les k les plus fréquents."""

import string
from collections import Counter

def normalize(text):
    """Met le texte en minuscules, retire la ponctuation et retourne la liste des mots"""
    text = text.lower()
    spaces = " " * len(string.punctuation)
    translator = str.maketrans(string.punctuation, spaces)

    return text.translate(translator).split()


def count_words(words):
    """Retourne un dictionnaire {mot: nombre d'occurrences}"""
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_k(counts, k):
    """Retourne les k mots les plus fréquents, sous forme de
    liste de tuples (mot, nombre), triés par nombre décroissant puis par ordre alphabétique
    en cas d'égalité."""
    sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_items[:k]


def main():
    """Application des fonctions dans un paragraphe et affichage des resultats"""
    text = """
    L'intelligence artificielle transforme profondément notre façon de travailler et de coder.
    Aujourd'hui, les développeurs utilisent des outils intelligents pour analyser des données,
    automatiser des tâches répétitives et résoudre des problèmes complexes plus rapidement.
    Cependant, comprendre les bases de l'algorithmique reste essentiel pour tout bon développeur.
    Savoir manipuler des structures de données simples comme les listes et les dictionnaires
    permet d'écrire du code clair, rapide et facile à maintenir. En Python, la simplicité
    du langage aide à se concentrer sur la logique plutôt que sur la syntaxe. C'est pourquoi
    Python est devenu le langage de référence pour l'analyse de données et le développement
    d'applications modernes. La pratique régulière est la clé pour maîtriser ces concepts
    et progresser chaque jour dans le monde du développement logiciel.
    """
    k = 5

    # Nettoyage et découpage du texte
    words = normalize(text)

    # Comptage des occurrences
    counts = count_words(words)

    # Récupération des k mots les plus fréquents
    top_words = top_k(counts, k)

    # Affichage des résultats
    print("=== Résultat avec nos fonctions ===")
    print(f"Nombre total de mots : {len(words)}")
    print(f"Top {k} des mots les plus fréquents : ")
    for word, count in top_words:
        print(f"    - {word} : {count}")

    # Vérification avec collections.Counter
    counter_top = Counter(words).most_common(k)

    print(f"\n=== Vérification avec Counter.most_common({k}) ===")
    for word, freq in counter_top:
        print(f"    - {word} : {freq}")

    # Vérification si les 2 listes sont identiques
    assert top_k(counts, k) == Counter(words).most_common(k), "Les résultats diffèrent"


if __name__ == "__main__":
    main()
