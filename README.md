# Growth Analytics — @mr.elgo

La compréhension ne découle pas simplement de l'analyse de données;
elle résulte de l'analyse de ces données dans un contexte particulier.
L'information n'a aucune utilité tant que l'on ne sait pas ce qu'elle signifie.

Pour en saisir le sens, il ne suffit pas de poser les bonnes questions, 
il faut également disposer d'outils appropriés pour analyser les données dans le cadre d'un processus pertinent de tri et de description.

## Contexte
"L'homme reste prisonnier de son ignorance de lui-même tant qu'il n'apprend pas à voir au-delà des causes apparentes. L'histoire de l'humanité nous montre que les réponses ne découlent jamais de l'identification de "causes" dans le monde.
Il faut au contraire identifier les conditions qui sous-tendent ces causes apparentes, or, ces conditions n'existent qu'au sein même de la conscience humaine."
Ces observations m'ont plongé dans le monde de la spiritualité, qui a clarifié bon nombre de questionnements que j'avais sur la vie et sa nature profonde.
Ce soulagement existentiel ma poussé à faire le pont entre spiritualité et science afin d'aider les gens à mieux se connaitre et par conséquent mieux vivre à travers le concept Amul-Xalaat.

## Questions clés: Formats et Structure du Contenu
Qu'est ce qui explique la croissance organique sur mes réseaux au delà du contenu des posts?
- Qu'est ce qui a renforcé la montée en engagement (Likes et commentaires et abonnés): le format de la publication, la durée des vidéos, le thème du post, l'heure de publication?
- Quels types de posts ont créé plus d'engagements
- Quels facteurs garantissent le maintient de la croissance organique?


🔗 **[Voir le dashboard en live](https://misterelgo-growth-analytics.streamlit.app/)**

Analyse de la croissance organique Instagram de 0 à 10K abonnés
en 17 mois, sans budget publicitaire.

## Insights clés

- **10K abonnés** acquis organiquement de déc. 2024 à mai 2026
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