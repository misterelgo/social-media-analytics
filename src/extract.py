import json
import pandas as pd
from datetime import datetime
import os

BASE = "data/instagram"

def load_followers():
    with open(f"{BASE}/connections/followers_and_following/followers_1.json", 
              "r", encoding="utf-8") as f:
        data = json.load(f)
    
    records = []
    for item in data:
        ts = item["string_list_data"][0]["timestamp"]
        records.append({
            "date": datetime.fromtimestamp(ts),
            "type": "follower"
        })
    
    df = pd.DataFrame(records)
    df["month"] = df["date"].dt.to_period("M").astype(str)
    print(f"Followers chargés : {len(df)}")
    return df

def load_posts():
    with open(f"{BASE}/your_instagram_activity/media/posts_1.json",
              "r", encoding="utf-8") as f:
        data = json.load(f)
    
    records = []
    for item in data:
        ts = item["media"][0]["creation_timestamp"]
        records.append({
            "date": datetime.fromtimestamp(ts),
            "type": "post",
            "title": item.get("title", "")
        })
    
    df = pd.DataFrame(records)
    df["month"] = df["date"].dt.to_period("M").astype(str)
    print(f"Posts chargés : {len(df)}")
    return df

def load_reels():
    with open(f"{BASE}/your_instagram_activity/media/reels.json",
              "r", encoding="utf-8") as f:
        data = json.load(f)
    
    records = []
    for item in data.get("ig_reels_media", []):
        ts = item["media"][0]["creation_timestamp"]
        records.append({
            "date": datetime.fromtimestamp(ts),
            "type": "reel",
            "title": item.get("title", "")
        })
    
    df = pd.DataFrame(records)
    df["month"] = df["date"].dt.to_period("M").astype(str)
    print(f"Reels chargés : {len(df)}")
    return df

def load_comments():
    with open(f"{BASE}/your_instagram_activity/comments/post_comments_1.json",
              "r", encoding="utf-8") as f:
        data = json.load(f)
    
    records = []
    for item in data:
        media_owner = item.get("string_map_data", {}).get("Media Owner", {}).get("value", "")
        if media_owner == "mr.elgo":
            ts = item["string_map_data"]["Time"]["timestamp"]
            records.append({
                "date": datetime.fromtimestamp(ts),
                "type": "comment"
            })
    
    df = pd.DataFrame(records)
    df["month"] = df["date"].dt.to_period("M").astype(str)
    print(f"Commentaires reçus chargés : {len(df)}")
    return df

def extract_all():
    followers = load_followers()
    posts     = load_posts()
    reels     = load_reels()
    comments  = load_comments()
    
    os.makedirs("data/processed", exist_ok=True)
    
    followers.to_csv("data/processed/followers.csv", index=False)
    posts.to_csv("data/processed/posts.csv", index=False)
    reels.to_csv("data/processed/reels.csv", index=False)
    comments.to_csv("data/processed/comments.csv", index=False)
    
    print("\n✓ Tous les fichiers sauvegardés dans data/processed/")
    return followers, posts, reels, comments

if __name__ == "__main__":
    extract_all()