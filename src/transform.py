import pandas as pd
import os

def transform():
    # Chargement
    followers = pd.read_csv("data/processed/followers.csv", parse_dates=["date"])
    posts     = pd.read_csv("data/processed/posts.csv", parse_dates=["date"])
    reels     = pd.read_csv("data/processed/reels.csv", parse_dates=["date"])
    comments  = pd.read_csv("data/processed/comments.csv", parse_dates=["date"])

    # ── Nouveaux abonnés par mois ─────────────────────────────────────
    followers_by_month = (
        followers.groupby("month")
        .size()
        .reset_index(name="new_followers")
    )

    # ── Publications par mois (posts + reels) ────────────────────────
    content = pd.concat([posts, reels], ignore_index=True)
    content_by_month = (
        content.groupby(["month", "type"])
        .size()
        .unstack(fill_value=0)
        .reset_index()
    )
    content_by_month.columns.name = None

    # Assure que les deux colonnes existent
    for col in ["post", "reel"]:
        if col not in content_by_month.columns:
            content_by_month[col] = 0

    content_by_month["total_content"] = (
        content_by_month["post"] + content_by_month["reel"]
    )

    # ── Commentaires par mois ─────────────────────────────────────────
    comments_by_month = (
        comments.groupby("month")
        .size()
        .reset_index(name="comments_received")
    )

    # ── Merge tout sur le mois ────────────────────────────────────────
    df = followers_by_month.merge(content_by_month, on="month", how="outer")
    df = df.merge(comments_by_month, on="month", how="outer")
    df = df.fillna(0)
    df = df.sort_values("month").reset_index(drop=True)

    # ── Abonnés cumulés ───────────────────────────────────────────────
    df["cumulative_followers"] = df["new_followers"].cumsum()

    print(df.to_string(index=False))
    print(f"\n✓ {len(df)} mois analysés")

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/monthly_stats.csv", index=False)
    print("✓ Sauvegardé : data/processed/monthly_stats.csv")
    return df

if __name__ == "__main__":
    transform()