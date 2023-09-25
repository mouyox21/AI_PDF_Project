import streamlit as st
import subprocess

st.title("Affichage de la commande ls -ltr")

# Utilisation de subprocess pour exécuter la commande ls -ltr
result = subprocess.run(["ls", "-ltr"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if result.returncode == 0:
    # Affichage de la sortie de la commande
    st.code(result.stdout)
else:
    # Affichage de l'erreur s'il y en a une
    st.error("Une erreur s'est produite lors de l'exécution de la commande ls -ltr.")
    st.code(result.stderr)
