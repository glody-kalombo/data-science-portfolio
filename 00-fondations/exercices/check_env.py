
"""Vérifie la version de Python et de requests dans l'environnement actif."""

import sys
import requests

print(f"Version de Python : {sys.version}")
print(f"Version de requests : {requests.__version__}")
