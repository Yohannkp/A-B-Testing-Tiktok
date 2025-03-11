import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Configuration de la page
st.set_page_config(page_title="Analyse A/B Testing TikTok", layout="wide")

# Titre de l'application
st.title("📊 Analyse A/B Testing sur TikTok")

# Chargement du dataset directement depuis le fichier local
DATA_PATH = "data/tiktok_dataset.csv"  # 👉 Remplacez par votre fichier
data = pd.read_csv(DATA_PATH)
st.success("✅ Fichier chargé avec succès !")

# Nettoyage des données
data = data.dropna()  # Suppression des valeurs manquantes
data = data.drop_duplicates()  # Suppression des doublons

# Sélection des variables clés
verified = data[data["verified_status"] == "verified"]["video_view_count"]
not_verified = data[data["verified_status"] == "not verified"]["video_view_count"]

# Test A/B - Vérification et Vues
st.subheader("🔍 Impact du statut vérifié sur les vues")
t_stat, p_value = stats.ttest_ind(not_verified, verified, equal_var=False)
st.write(f"**t-statistic:** {t_stat:.2f}, **p-value:** {p_value:.5f}")

fig, ax = plt.subplots()
sns.boxplot(x=data["verified_status"], y=data["video_view_count"], palette="coolwarm", ax=ax)
ax.set_title("Distribution des vues par statut de vérification")
ax.set_yscale("log")  # Échelle logarithmique
st.pyplot(fig)

# Test A/B - Durée et Vues
st.subheader("⏳ Impact de la durée des vidéos sur les vues")
short_videos = data[data["video_duration_sec"] < data["video_duration_sec"].median()]["video_view_count"]
long_videos = data[data["video_duration_sec"] > data["video_duration_sec"].median()]["video_view_count"]
t_stat, p_value = stats.ttest_ind(short_videos, long_videos, equal_var=False)
st.write(f"**t-statistic:** {t_stat:.2f}, **p-value:** {p_value:.5f}")

fig, ax = plt.subplots()
sns.histplot(data, x="video_duration_sec", bins=30, kde=True, hue="verified_status", palette="coolwarm", ax=ax)
ax.set_title("Répartition des vues selon la durée des vidéos")
st.pyplot(fig)

# Test A/B - Partages et Vues
st.subheader("📢 Impact du nombre de partages sur les vues")
data["comment_view_ratio"] = data["video_comment_count"] / data["video_view_count"]
data["share_view_ratio"] = data["video_share_count"] / data["video_view_count"]

fig, ax = plt.subplots()
sns.scatterplot(x=data["video_share_count"], y=data["video_view_count"], alpha=0.5, ax=ax)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_title("Corrélation entre le nombre de partages et les vues")
st.pyplot(fig)

# Test A/B - Ratio Commentaires/Vues
st.subheader("💬 Ratio Commentaires/Vues")
fig, ax = plt.subplots()
sns.histplot(data["comment_view_ratio"], bins=50, kde=True, color="purple", ax=ax)
ax.set_title("Distribution du ratio Commentaires/Vues")
st.pyplot(fig)

st.success("🎯 Analyse terminée !")
