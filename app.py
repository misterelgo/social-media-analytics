import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Growth Analytics — @mr.elgo",
    page_icon="📱",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("data/processed/monthly_stats.csv")

df = load_data()

# ── Titre ─────────────────────────────────────────────────────────────
st.title("📱 Growth Analytics — @mr.elgo")
st.markdown("Analyse de la croissance organique Instagram · Déc. 2024 – Mai 2026")

# ── KPIs ──────────────────────────────────────────────────────────────
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Abonnés totaux", f"{int(df['cumulative_followers'].max()):,}".replace(",", " "))
col2.metric("Meilleur mois", df.loc[df['new_followers'].idxmax(), 'month'])
col3.metric("Pic d'abonnés", f"+{int(df['new_followers'].max()):,}".replace(",", " "))
col4.metric("Commentaires reçus", f"{int(df['comments_received'].sum()):,}".replace(",", " "))

# ── Graphique 1 : Courbe de croissance cumulée ────────────────────────
st.markdown("---")
st.subheader("Courbe de croissance des abonnés")

fig1 = px.area(
    df, x="month", y="cumulative_followers",
    labels={"month": "Mois", "cumulative_followers": "Abonnés cumulés"},
    color_discrete_sequence=["#E1306C"]
)
fig1.update_layout(showlegend=False)
st.plotly_chart(fig1, use_container_width=True)

# ── Graphique 2 : Nouveaux abonnés vs contenu publié ─────────────────
st.markdown("---")
st.subheader("Nouveaux abonnés vs contenu publié par mois")

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=df["month"], y=df["new_followers"],
    name="Nouveaux abonnés", marker_color="#E1306C"
))
fig2.add_trace(go.Scatter(
    x=df["month"], y=df["total_content"],
    name="Contenus publiés", mode="lines+markers",
    line=dict(color="#405DE6", width=2),
    yaxis="y2"
))
fig2.update_layout(
    yaxis=dict(title="Nouveaux abonnés"),
    yaxis2=dict(title="Contenus publiés", overlaying="y", side="right"),
    legend=dict(orientation="h", y=1.1)
)
st.plotly_chart(fig2, use_container_width=True)

# ── Graphique 3 : Posts vs Reels ──────────────────────────────────────
st.markdown("---")
st.subheader("Répartition Posts vs Reels par mois")

fig3 = go.Figure()
fig3.add_trace(go.Bar(
    x=df["month"], y=df["post"],
    name="Posts", marker_color="#FCAF45"
))
fig3.add_trace(go.Bar(
    x=df["month"], y=df["reel"],
    name="Reels", marker_color="#E1306C"
))
fig3.update_layout(
    barmode="stack",
    xaxis_title="Mois",
    yaxis_title="Nombre de contenus"
)
st.plotly_chart(fig3, use_container_width=True)

# ── Graphique 4 : Commentaires reçus ─────────────────────────────────
st.markdown("---")
st.subheader("Engagement — Commentaires reçus par mois")

fig4 = px.bar(
    df, x="month", y="comments_received",
    labels={"month": "Mois", "comments_received": "Commentaires reçus"},
    color="comments_received",
    color_continuous_scale=["#FCAF45", "#E1306C"]
)
fig4.update_layout(coloraxis_showscale=False)
st.plotly_chart(fig4, use_container_width=True)

# ── Footer ────────────────────────────────────────────────────────────
st.markdown("---")
st.caption("Source : Export de données Instagram · Analyse Python · pandas · Plotly · Streamlit")