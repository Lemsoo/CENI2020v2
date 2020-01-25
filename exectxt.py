import sys

orig = sys.stdout
with open("output.txt", "wb") as f:
    sys.stdout = f
    try:
        execfile("le_fichier_py_à_exécuter", {})
    finally:
        sys.stdout = orig
