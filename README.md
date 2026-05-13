# Growth Analytics — @mr.elgo

🔗 **[Voir le dashboard en live](COLLE-TON-URL-ICI)**

Analyse de la croissance organique Instagram de 0 à 9 852 abonnés
en 17 mois, sans budget publicitaire.

## Insights clés

- **9 852 abonnés** acquis organiquement de déc. 2024 à mai 2026
- **Septembre 2025** — pic de croissance : +2 453 abonnés en un mois
- **1 796 commentaires** reçus — taux d'engagement élevé
- Corrélation identifiée entre volume de reels et acquisition d'abonnés

## Pipeline
Export JSON Instagram
↓
extract.py  → parsing followers, posts, reels, commentaires
↓
transform.py → agrégation mensuelle, abonnés cumulés
↓
app.py → dashboard Streamlit interactif déployé en live

## Stack

Python · pandas · Streamlit · Plotly

## Source des données

Export personnel Instagram — données privées non incluses dans le repo.