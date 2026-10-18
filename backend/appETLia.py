import streamlit as st
import requests
import numpy as np
import pandas as pd
import base64
import json

# Configuration de la page (doit être en premier)
st.set_page_config(page_title="ETLIA", initial_sidebar_state="expanded")

# Charger et encoder ton image
with open("Designsanstitre.png", "rb") as f:
   data = base64.b64encode(f.read()).decode("utf-8")


# Initialiser le state pour le mode sombre
if "dark_mode" not in st.session_state:
   st.session_state.dark_mode = False

# Initialiser le statut de connexion
if "connection_status" not in st.session_state:
   st.session_state.connection_status = "disconnected"  # disconnected, connected, error


# Injecter le CSS et l'image dans un conteneur fixe
st.markdown(
    f"""
    <style>
        /* Variables de couleurs */
        :root {{
            --bg-primary: {'#1a1d24' if st.session_state.dark_mode else '#ffffff'};
            --bg-secondary: {'#2d3139' if st.session_state.dark_mode else '#f0f2f6'};
            --bg-tertiary: {'#3a3f4b' if st.session_state.dark_mode else '#e6e9ef'};
            --text-primary: {'#e8eaed' if st.session_state.dark_mode else '#31333F'};
            --text-secondary: {'#9aa0a6' if st.session_state.dark_mode else '#69707f'};
            --border-color: {'#4a4f5c' if st.session_state.dark_mode else '#d0d5dd'};
            --input-bg: {'#16181d' if st.session_state.dark_mode else '#ffffff'};
            --success-color: {'#4caf50' if st.session_state.dark_mode else '#2e7d32'};
            --error-color: {'#f44336' if st.session_state.dark_mode else '#c62828'};
        }}

        /* Force le thème sur toute la page */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {{
            background-color: var(--bg-primary) !important;
            color: var(--text-primary) !important;
        }}

        /* Sidebar fixe */
        section[data-testid="stSidebar"] {{
            background-color: var(--bg-secondary) !important;
            width: 300px !important;
            min-width: 300px !important;
        }}

        /* ===== Logo derrière la sidebar ===== */
        #background-logo {{
            position: fixed;
            top: 70px;
            left: 0px; /* derrière la sidebar */
            width: 165px;
            height: 165x;
            margin: 20px auto; /* centre horizontalement */
            border-radius: 50%;
            border: 10px solid {'#4a4f5c' if st.session_state.dark_mode else '#e6e9ef'};
            overflow: hidden;
            text-align: center;
            margin-left: 50px;
        }}
        #background-logo img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
        }}

        /* Indicateur de statut de connexion */
        .connection-status {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            padding: 12px 16px;
            border-radius: 8px;
            font-size: 0.9em;
            font-weight: 500;
            margin-bottom: 15px;
        }}
        .status-indicator {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.5; }}
        }}
        .status-connected {{
            background-color: rgba(76, 175, 80, 0.2);
            color: var(--success-color);
            border: 1px solid var(--success-color);
        }}
        .status-connected .status-indicator {{
            background-color: var(--success-color);
        }}
        .status-disconnected {{
            background-color: rgba(158, 158, 158, 0.2);
            color: var(--text-secondary);
            border: 1px solid var(--border-color);
        }}
        .status-disconnected .status-indicator {{
            background-color: var(--text-secondary);
            animation: none;
        }}
        .status-error {{
            background-color: rgba(244, 67, 54, 0.2);
            color: var(--error-color);
            border: 1px solid var(--error-color);
        }}
        .status-error .status-indicator {{
            background-color: var(--error-color);
        }}

        /* Inputs */
        .stTextInput > div > div > input {{
            background-color: var(--input-bg) !important;
            color: var(--text-primary) !important;
            border: 2px solid var(--border-color) !important;
            border-radius: 6px !important;
        }}
        .stTextInput > div > div > input:focus {{
            border-color: {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
            box-shadow: 0 0 0 1px {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
        }}
        .stTextInput label, .stTextArea label {{
            color: var(--text-primary) !important;
        }}
        .stTextArea textarea {{
            background-color: var(--input-bg) !important;
            color: var(--text-primary) !important;
            border: 2px solid var(--border-color) !important;
            border-radius: 6px !important;
        }}

        /* Chat */
        [data-testid="stChatInput"] textarea {{
            background-color: var(--input-bg) !important;
            color: var(--text-primary) !important;
            caret-color: var(--text-primary) !important;
        }}
        [data-testid="stChatInput"] button {{
            background-color: var(--bg-tertiary) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
        }}
        [data-testid="stChatInput"] button:hover {{
            background-color: {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
            border-color: {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
        }}
        [data-testid="stChatMessage"] {{
            background-color: var(--bg-tertiary) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 8px !important;
            color: var(--text-primary) !important;
        }}

        /* Boutons */
        .stButton > button {{
            background-color: var(--bg-secondary) !important;
            color: var(--text-primary) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 6px !important;
            transition: all 0.2s ease !important;
        }}
        .stButton > button:hover {{
            background-color: var(--bg-tertiary) !important;
            border-color: {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
        }}

        /* Titres et textes */
        h1,h2,h3,h4,h5,h6,p,span,div {{
            color: var(--text-primary) !important;
        }}
        /* Indicateur de statut de connexion */
       .connection-status {{
           display: flex;
           align-items: center;
           justify-content: center;
           gap: 8px;
           padding: 12px 16px;
           border-radius: 8px;
           font-size: 0.9em;
           font-weight: 500;
           margin-bottom: 15px;
       }}
       
       .status-indicator {{
           width: 10px;
           height: 10px;
           border-radius: 50%;
           animation: pulse 2s infinite;
       }}
       
       @keyframes pulse {{
           0%, 100% {{ opacity: 1; }}
           50% {{ opacity: 0.5; }}
       }}
       
       .status-connected {{
           background-color: rgba(76, 175, 80, 0.2);
           color: var(--success-color);
           border: 1px solid var(--success-color);
       }}
       
       .status-connected .status-indicator {{
           background-color: var(--success-color);
       }}
       
       .status-disconnected {{
           background-color: rgba(158, 158, 158, 0.2);
           color: var(--text-secondary);
           border: 1px solid var(--border-color);
       }}
       
       .status-disconnected .status-indicator {{
           background-color: var(--text-secondary);
           animation: none;
       }}
       
       .status-error {{
           background-color: rgba(244, 67, 54, 0.2);
           color: var(--error-color);
           border: 1px solid var(--error-color);
       }}
       
       .status-error .status-indicator {{
           background-color: var(--error-color);
       }}
      
       /* Inputs - Meilleur contraste */
       .stTextInput > div > div > input {{
           background-color: var(--input-bg) !important;
           color: var(--text-primary) !important;
           border: 2px solid var(--border-color) !important;
           border-radius: 6px !important;
       }}
      
       .stTextInput > div > div > input:focus {{
           border-color: {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
           box-shadow: 0 0 0 1px {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
       }}
      
       /* Labels */
       .stTextInput label, .stTextArea label {{
           color: var(--text-primary) !important;
       }}
      
       /* Text areas */
       .stTextArea textarea {{
           background-color: var(--input-bg) !important;
           color: var(--text-primary) !important;
           border: 2px solid var(--border-color) !important;
           border-radius: 6px !important;
       }}
      
       /* ===== ZONE DE CHAT EN BAS ET AUTOUR ===== */
       /* Conteneur de la zone de chat fixe en bas */
       [data-testid="stBottom"] {{
           background-color: var(--bg-primary) !important;
           border-top: 2px solid var(--border-color) !important;
           padding: 16px !important;
       }}
      
       /* Tous les divs autour du chat input */
       [data-testid="stBottom"] > div {{
           background-color: var(--bg-primary) !important;
       }}
      
       /* Container parent du chat input */
       [data-testid="stChatInputContainer"] {{
           background-color: var(--bg-primary) !important;
       }}
      
       /* Input de chat (st.chat_input) */
       [data-testid="stChatInput"] {{
           background-color: var(--input-bg) !important;
           border: 2px solid var(--border-color) !important;
           border-radius: 8px !important;
       }}
      
       [data-testid="stChatInput"] > div {{
           background-color: var(--input-bg) !important;
       }}
      
       [data-testid="stChatInput"] textarea {{
           background-color: var(--input-bg) !important;
           color: var(--text-primary) !important;
           caret-color: var(--text-primary) !important;
       }}
      
       [data-testid="stChatInput"] textarea::placeholder {{
           color: var(--text-secondary) !important;
           opacity: 0.7 !important;
       }}
      
       /* Bouton d'envoi du chat */
       [data-testid="stChatInput"] button {{
           background-color: var(--bg-tertiary) !important;
           color: var(--text-primary) !important;
           border: 1px solid var(--border-color) !important;
       }}
      
       [data-testid="stChatInput"] button:hover {{
           background-color: {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
           border-color: {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
       }}
      
       /* Icône du bouton d'envoi */
       [data-testid="stChatInput"] button svg {{
           fill: var(--text-primary) !important;
       }}
      
       /* Chat messages */
       [data-testid="stChatMessage"] {{
           background-color: var(--bg-tertiary) !important;
           border: 1px solid var(--border-color) !important;
           border-radius: 8px !important;
           color: var(--text-primary) !important;
       }}
      
       [data-testid="stChatMessage"] p,
       [data-testid="stChatMessage"] span,
       [data-testid="stChatMessage"] div {{
           color: var(--text-primary) !important;
       }}
      
       /* Avatar du chat */
       [data-testid="chatAvatarIcon-user"],
       [data-testid="chatAvatarIcon-assistant"] {{
           background-color: var(--bg-secondary) !important;
       }}
      
       /* Conteneur des messages de chat */
       [data-testid="stChatMessageContainer"] {{
           background-color: var(--bg-primary) !important;
       }}
      
       /* Scrollbar pour le chat */
       [data-testid="stChatMessageContainer"]::-webkit-scrollbar {{
           width: 8px;
           background-color: var(--bg-secondary);
       }}
      
       [data-testid="stChatMessageContainer"]::-webkit-scrollbar-thumb {{
           background-color: var(--border-color);
           border-radius: 4px;
       }}
      
       /* Boutons */
       .stButton > button {{
           background-color: var(--bg-secondary) !important;
           color: var(--text-primary) !important;
           border: 1px solid var(--border-color) !important;
           border-radius: 6px !important;
           transition: all 0.2s ease !important;
       }}
      
       .stButton > button:hover {{
           background-color: var(--bg-tertiary) !important;
           border-color: {'#5b9bd5' if st.session_state.dark_mode else '#0066cc'} !important;
       }}
       /* Header Streamlit */
       header[data-testid="stHeader"] {{
           background-color: var(--bg-primary) !important;
       }}
             
    </style>

    <div id="background-logo">
        <img src="data:image/png;base64,{data}" alt="Logo ETLIA">
    </div>
    """,
    unsafe_allow_html=True
)

# Titre sans bouton mode sombre
st.title("Par quoi commençons-nous ?")


# Side bar connection a la base de donnees
with st.sidebar:
  # Indicateur de statut de connexion en haut
  with st.sidebar:
    st.markdown(
        f"""
        <style>
            .sidebar-logo {{
                width: 165px;
                height: 165x;
                margin: 20px auto; /* centre horizontalement */
                border-radius: 50%;
                border: 10px solid {'#4a4f5c' if st.session_state.dark_mode else '#e6e9ef'};
                overflow: hidden;
                text-align: center;
            }}

            .sidebar-logo img {{
                width: 100%;
                height: 100%;
                object-fit: cover;
                display: block;
            }}
        </style>

        <div class="sidebar-logo">
            <img src="data:image/png;base64,{data}" alt="Logo ETLIA">
        </div>
        """,
        unsafe_allow_html=True
    )


  status_class = f"status-{st.session_state.connection_status}"
  status_text = {
      "connected": "✓ Connecté",
      "disconnected": "○ Déconnecté", 
      "error": "✗ Erreur de connexion"
  }
  
  st.markdown(f"""
      <div class="connection-status {status_class}">
          <div class="status-indicator"></div>
          <span>{status_text.get(st.session_state.connection_status, "○ Déconnecté")}</span>
      </div>
  """, unsafe_allow_html=True)
  
  # Bouton du mode sombre
  if st.button("🌓 Mode sombre" if not st.session_state.dark_mode else "☀️ Mode clair", use_container_width=True):
      st.session_state.dark_mode = not st.session_state.dark_mode
      st.rerun()
      
  st.markdown("---")  # Séparateur
  
  st.header("Connexion à la base de données")
  db_host = st.text_input("Hôte SQL", value="sql")
  db_user = st.text_input("Utilisateur", value="sa")
  db_pass = st.text_input("Mot de passe", value="MyStrongPass123", type="password")
  db_name = st.text_input("Base de données", value="master")
  webhook_url = st.text_input("URL Webhook n8n", value="https://c40693b742e6.ngrok-free.app/webhook/etlia-chat\"")


# Historique des messages
if "history" not in st.session_state:
  st.session_state.history = []


# Affiche l'historique
for msg in st.session_state.history:
  st.chat_message(msg["role"]).markdown(msg["content"])
import pyodbc
from config import UID, PWD  # identifiants SQL Server

# --- Connexion SQL Server ---
DRIVER = '/opt/homebrew/lib/libmsodbcsql.18.dylib'
SERVER = 'localhost,1433'  # ou 'host.docker.internal' si Docker
DATABASE = 'master'

conn_str = (
    f"DRIVER={DRIVER};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={UID};"
    f"PWD={PWD};"
    "Encrypt=no;"
    "TrustServerCertificate=yes;"
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# --- Récupération des tables ---
cursor.execute("""
SELECT TABLE_NAME
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE='BASE TABLE' AND TABLE_SCHEMA='dbo'
""")
tables = [row[0] for row in cursor.fetchall()]

# --- Récupération des colonnes par table ---
schema = {}
for table in tables:
    cursor.execute(f"""
    SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME='{table}' AND TABLE_SCHEMA='dbo'
    """)
    cols = [row[0] for row in cursor.fetchall()]
    schema[table] = cols

cursor.close()
conn.close()

# --- Préparation du prompt complet ---
preprompt = f"""
You are ETLIA, an intelligent agent specialized in the analysis, transformation, and automation of data flows (ETL).
You always respond professionally in french, concisely, and precisely in pure JSON format.

Your mission is to handle the full ETL process, including:
- Extract: interact with the SQL Server database to retrieve or filter relevant data.
- Transform: propose or describe data cleaning, aggregation, normalization, and transformation operations.
- Load: create or update datamarts or summarized tables, always safely and based on existing data.

Your specific abilities:
- Formulate optimized and secure SQL queries.
- Propose ETL transformations clearly before generating SQL.
- Create datamarts when needed (e.g., for KPIs, summaries, reporting).
- Never execute dangerous commands (DROP, DELETE without WHERE, TRUNCATE, etc.).
- Always use only the tables and columns listed in the schema reference.
- When creating a datamart, you can introduce a new table name only if it is derived from existing data (example: Datamart_Ventes_2025 built from ventes).

You always return strictly a JSON object with the two following fields:
- "message": short and clear description of the ETL logic or purpose.
- "sql": the pure SQL query to execute if applicable (no formatting, no ```sql``` fences).

If no SQL is needed, "sql" must be an empty string.

Examples:

1. Data extraction
{{
  "message": "",
  "sql": "SELECT * FROM clients WHERE date_creation >= '2024-01-01';"
}}

2. Transformation step
{{
  "message": "Normalize text fields and remove duplicates from the clients table.",
  "sql": ""
}}

3. Datamart creation
{{
  "message": "Create a sales datamart aggregating total revenue by month and product.",
  "sql": "CREATE TABLE Datamart_Ventes AS SELECT DATEPART(MONTH, DateVente) AS Mois, ProduitID, SUM(Total) AS CA_Mensuel FROM ventes GROUP BY DATEPART(MONTH, DateVente), ProduitID;"
}}

Schema reference:
{schema}
"""
# Entrée utilisateur
user_input = st.chat_input("Faites parler vos données")

# Initialisation du DataFrame et de l'historique
if "df_result" not in st.session_state:
    st.session_state.df_result = None
if "history" not in st.session_state:
    st.session_state.history = []

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})

    payload = {
        "message": preprompt + "\n\nUser request: " + user_input,
        "server": db_host,
        "name": db_name,
        "user": db_user,
        "password": db_pass   
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=60)
        if response.status_code == 200:
            assistant_reply = response.json()
            st.session_state.connection_status = "connected"

            # Cas où le webhook renvoie une liste
            if isinstance(assistant_reply, list):
                if not assistant_reply:
                    st.session_state.history.append({
                        "role": "assistant",
                        "content": "Aucun résultat trouvé pour votre requête."
                    })
                    st.session_state.df_result = None
                else:
                    first_item = assistant_reply[0]
                    # Message simple
                    if isinstance(first_item, dict) and "message" in first_item and len(assistant_reply) == 1:
                        st.session_state.history.append({
                            "role": "assistant",
                            "content": first_item["message"]
                        })
                        st.session_state.df_result = None
                    else:
                        # Tableau SQL
                        df = pd.DataFrame(assistant_reply)
                        if "message" in df.columns:
                            message = df['message'][0]
                            st.session_state.history.append({
                            "role": "assistant",
                            "content": f"{message}"
                        })
                            df = df.drop(columns=["message"])
                        st.session_state.df_result = df
                        st.session_state.history.append({
                            "role": "assistant",
                            "content": "Voici les résultats SQL sous forme de tableau."
                        })

            # Cas dictionnaire {message, sql}
            elif isinstance(assistant_reply, dict):
                message = assistant_reply.get("message", "")
                sql_query = assistant_reply.get("sql", "")
                
                if message:
                    st.session_state.history.append({"role": "assistant", "content": message})
                if sql_query:
                    st.session_state.history.append({"role": "assistant", "content": f"Requête SQL générée: `{sql_query}`"})

            else:
                st.session_state.history.append({"role": "assistant", "content": str(assistant_reply)})

        else:
            st.session_state.history.append({
                "role": "assistant",
                "content": f"Erreur n8n ({response.status_code}): {response.text}"
            })
            st.session_state.connection_status = "error"

    except Exception as e:
        st.session_state.history.append({
            "role": "assistant",
            "content": f"Erreur de connexion ou exécution: {e}"
        })
        st.session_state.connection_status = "error"

# Afficher l’historique
for msg in st.session_state.history:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Afficher le DataFrame si présent
if st.session_state.df_result is not None:
    st.dataframe(st.session_state.df_result)
    csv = st.session_state.df_result.to_csv(index=False).encode("utf-8")
    st.download_button("Télécharger CSV", csv, "resultats.csv", "text/csv")
