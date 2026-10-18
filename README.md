# ETLia: AI-Assisted Data Extraction, Transformation & Loading Interface

> **Cadre académique** : ENSIIE — Projet Ingénierie Logicielle & Systèmes Décisionnels  
> **Auteur** : Mohamed Nourou Dine CISSE  
> **Domaine** : `Data Engineering & Interactive Web Interfaces`  
> **Stack Technique** : `Python` `Streamlit` `SQL Server (T-SQL)` `PyODBC` `React` `TypeScript` `TailwindCSS` `Vite`

---

## 📌 Présentation Réelle du Projet (Honest Overview)

**ETLia** est un prototype d'application conçu pour simplifier les opérations d'extraction, de transformation et de chargement (ETL) à destination des équipes data et des analystes métier. Le projet explore deux approches complémentaires :
1. Une **application interactive Python / Streamlit** (`backend/appETLia.py`) connectée à Microsoft SQL Server, permettant l'exploration du schéma de base de données, la configuration de règles de validation et la visualisation des flux de données.
2. Une **interface vitrine web moderne** (`frontend/`) développée sous React / Vite / TailwindCSS présentant le produit et ses fonctionnalités d'automatisation ETL.

---

## 🏗️ Structure du Dépôt

```text
02_ETLia_AI_Data_Wizard/
├── README.md                      # Présentation et documentation
├── backend/
│   ├── appETLia.py                # Application Streamlit principale avec design personnalisé
│   ├── config.py                  # Identifiants et paramètres de connexion SQL Server
│   └── load.py                    # Script d'inspection des tables et colonnes (schéma dbo)
├── frontend/                      # Interface web React / TypeScript
│   ├── index.html
│   ├── package.json
│   ├── vite.config.ts
│   └── src/
│       ├── App.tsx
│       ├── components/            # Composants (Hero, Features, Navigation, Contact, UI Radix)
│       └── pages/                 # Index.tsx, NotFound.tsx
└── assets/
    ├── ensiie_logo_fx_RVB_0.png   # Logo institutionnel ENSIIE
    └── Designsanstitre.png        # Bannière visuelle ETLia
```

---

## ⚙️ Fonctionnalités Développées

1. **Exploration du Schéma Relationnel** :
   - Requêtage dynamique des tables et métadonnées via `INFORMATION_SCHEMA.TABLES` et `COLUMNS`.
2. **Interface Streamlit Personnalisée** :
   - Mode clair / sombre avec thémage CSS injecté dynamiquement.
   - Sélection interactive des tables sources, prévisualisation des lignes et suivi des statuts de chargement.
3. **Application Web Moderne** :
   - Composants réutilisables basés sur TailwindCSS et Radix UI pour la présentation du pipeline de données.

---

## 🚀 Guide d'Exécution

### 1. Lancement du Backend Streamlit
```bash
# Installation des dépendances
pip install streamlit pyodbc pandas

# Exécution de l'application
cd backend
streamlit run appETLia.py
```
> *Remarque : La connexion à SQL Server requiert le pilote ODBC (ex. `msodbcsql18`) configuré localement ou via Docker.*

### 2. Lancement du Frontend React
```bash
cd frontend
npm install
npm run dev
```
L'interface est accessible sur `http://localhost:5173`.

---

## 🔍 Limites Honnêtes (Honest Assessment)
- Ce projet est un **prototype d'interface** (Proof of Concept) développé dans un cadre académique.
- La persistance SQL s'appuie sur une instance locale de SQL Server.

---

## 📬 Profil de l'Auteur
- **Mohamed Nourou Dine CISSE**
- **ENSIIE** & **Université Paris-Saclay** — Double diplôme, Master 2 Intelligence Artificielle (M2IA)
- Échange académique : **McMaster University** (Canada)
- **GitHub** : [@nourou-dine-cisse](https://github.com/nourou-dine-cisse)
