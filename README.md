# 📊 A/B Testing et Analyse Statistique sur TikTok 🎯  
🚀 _Analyse des facteurs influençant la viralité des vidéos TikTok_  

## Dashboard

lien : https://a-b-testing-tiktok-app.streamlit.app/
![Screenshot](./images/capture.png)


## 📌 Présentation du Projet  
Dans ce projet, nous avons effectué des **tests A/B** et une **analyse statistique avancée** pour identifier les facteurs qui influencent la viralité des vidéos sur **TikTok**.  

🔍 **Objectifs :**  
✅ Déterminer si certains critères (durée, commentaires, partages, statut de vérification...) influencent les vues.  
✅ Tester des hypothèses avec des **tests de Student (t-test)**.  
✅ Extraire des **insights exploitables** pour optimiser la performance des vidéos.  

---

## 📊 Données Utilisées  
📁 _Fichier :_ `tiktok_dataset.csv`  
📝 **Colonnes clés :**  
- `video_id` : Identifiant unique des vidéos  
- `video_duration_sec` : Durée des vidéos (en secondes)  
- `video_view_count` : Nombre de vues  
- `video_like_count` : Nombre de likes  
- `video_share_count` : Nombre de partages  
- `video_download_count` : Nombre de téléchargements  
- `video_comment_count` : Nombre de commentaires  
- `verified_status` : Statut de vérification du compte  

---

## 🔬 Méthodologie  
1️⃣ **Préparation des données** :  
   - Suppression des valeurs manquantes et doublons  
   - Exploration et visualisation des distributions  

2️⃣ **Tests A/B effectués :**  
   - 📌 **Impact du statut vérifié sur les vues** ✅  
   - 📌 **Impact de la durée de la vidéo sur les vues** ❌  
   - 📌 **Impact du nombre de commentaires sur les vues** ✅  
   - 📌 **Impact du nombre de partages sur les vues** ✅  
   - 📌 **Impact de la durée sur le nombre de commentaires** ❌  

---

## 📈 Résultats et Insights Clés  

✅ **Le statut vérifié influence fortement le nombre de vues** 📊  
✅ **Le nombre de commentaires et de partages booste la viralité** 🔥  
❌ **La durée des vidéos n’a aucun impact sur les vues ou les commentaires**  


💡 **Conclusion** :  
Les vidéos virales ne sont pas forcément plus longues, mais elles génèrent plus d’engagement (commentaires, partages). _L’algorithme TikTok semble privilégier l’interaction plutôt que la simple durée._  

---

