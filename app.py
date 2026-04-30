import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Config
st.set_page_config(page_title="TANAP - Guide Cameroun", page_icon="🇨🇲", layout="wide")

# Image de fond (Monument de la Réunification)
BG_IMAGE = "https://i.imgur.com/8QxZK5q.jpeg"

# CSS UNIQUE - Design humain et chaleureux
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap');
    
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.7)), url("{BG_IMAGE}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Nunito', sans-serif;
    }}
    
    section[data-testid="stSidebar"] {{
        background: rgba(255,255,255,0.95);
        border-right: 3px solid #d4a017;
    }}
    
    .landing-container {{
        background: rgba(255,255,255,0.92);
        border-radius: 20px;
        padding: 3rem;
        max-width: 800px;
        margin: 2rem auto;
        box-shadow: 0 15px 50px rgba(0,0,0,0.3);
        border: 2px solid #d4a017;
    }}
    
    .app-title {{
        color: #1a472a;
        font-size: 3.5rem;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.5rem;
    }}
    
    .app-subtitle {{
        color: #5a5a5a;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 2rem;
    }}
    
    .choice-card {{
        background: white;
        border: 2px solid #e0e0e0;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s;
        margin: 1rem 0;
    }}
    
    .choice-card:hover {{
        border-color: #1a472a;
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }}
    
    .choice-icon {{
        font-size: 4rem;
        margin-bottom: 1rem;
    }}
    
    .choice-title {{
        color: #1a472a;
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}
    
    .choice-desc {{
        color: #666;
        font-size: 0.95rem;
    }}
    
    .content-box {{
        background: rgba(255,255,255,0.95);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border-left: 4px solid #d4a017;
    }}
    
    .site-card {{
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #1a472a;
        box-shadow: 0 3px 15px rgba(0,0,0,0.08);
    }}
    
    .footer-box {{
        background: #1a472a;
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 2rem;
    }}
    
    .gold-badge {{
        background: #d4a017;
        color: white;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-weight: 600;
        display: inline-block;
    }}
    
    .green-badge {{
        background: #1a472a;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        font-size: 0.85rem;
    }}
    
    h1, h2, h3 {{
        color: #1a472a !important;
    }}
    
    .stButton > button {{
        background: #1a472a !important;
        color: white !important;
        border-radius: 25px !important;
        padding: 0.6rem 2rem !important;
        font-weight: 600 !important;
        border: none !important;
    }}
    
    .stButton > button:hover {{
        background: #d4a017 !important;
    }}
</style>
""", unsafe_allow_html=True)

# Données réalistes
SITES_DATA = [
    {"id": 1, "nom": "Monument de la Réunification", "region": "Centre", "ville": "Yaoundé", 
     "categorie": "Monument", "description": "Symbole de l'unité nationale camerounaise, érigé en 1972.", 
     "prix_entree": 500, "horaires": "08h - 17h", "contact": "+237 677 12 34 56",
     "email": "info@monument-yaounde.cm", "note": 4.5, "avis": 47, "date": "2024-01-15"},
    {"id": 2, "nom": "Chutes de la Lobé", "region": "Sud", "ville": "Kribi",
     "categorie": "Nature", "description": "Magnifiques chutes se jetant directement dans l'océan.",
     "prix_entree": 1000, "horaires": "07h - 18h", "contact": "+237 699 45 67 89",
     "email": "lobe.kribi@gmail.com", "note": 4.8, "avis": 32, "date": "2024-02-01"},
    {"id": 3, "nom": "Palais Royal Bamoun", "region": "Ouest", "ville": "Foumban",
     "categorie": "Culture", "description": "Palais historique du Sultan, musée d'art traditionnel.",
     "prix_entree": 2000, "horaires": "09h - 16h", "contact": "+237 655 78 90 12",
     "email": "palais.foumban@yahoo.fr", "note": 4.6, "avis": 28, "date": "2024-02-15"},
    {"id": 4, "nom": "Mont Cameroun", "region": "Sud-Ouest", "ville": "Buéa",
     "categorie": "Nature", "description": "Plus haut sommet d'Afrique de l'Ouest, randonnées guidées.",
     "prix_entree": 5000, "horaires": "06h - 15h", "contact": "+237 670 23 45 67",
     "email": "montcameroun.guide@gmail.com", "note": 4.7, "avis": 19, "date": "2024-03-01"},
    {"id": 5, "nom": "Parc de Waza", "region": "Extrême-Nord", "ville": "Waza",
     "categorie": "Safari", "description": "Réserve naturelle avec éléphants, girafes et lions.",
     "prix_entree": 3000, "horaires": "06h - 18h", "contact": "+237 622 56 78 90",
     "email": "parcwaza@tourisme.cm", "note": 4.4, "avis": 15, "date": "2024-03-10"},
]

# Session
if 'sites' not in st.session_state:
    st.session_state.sites = SITES_DATA.copy()
if 'role' not in st.session_state:
    st.session_state.role = None
if 'page' not in st.session_state:
    st.session_state.page = 'accueil'

def get_df():
    return pd.DataFrame(st.session_state.sites)

# ============ PAGE D'ACCUEIL - CHOIX DU RÔLE ============
if st.session_state.role is None:
    st.markdown("""
    <div class="landing-container">
        <div class="app-title">🇨🇲 TANAP</div>
        <div class="app-subtitle">
            <strong>T</strong>ourisme <strong>A</strong>uthentique et <strong>N</strong>aturel en <strong>A</strong>frique - <strong>P</strong>ortail Cameroun
        </div>
        <hr style="border: 1px solid #e0e0e0; margin: 1.5rem 0;">
        <p style="text-align: center; color: #444; font-size: 1.2rem; margin-bottom: 2rem;">
            <strong>Qui êtes-vous ?</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 3, 1])
    with col2:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("""
            <div class="choice-card">
                <div class="choice-icon">🧳</div>
                <div class="choice-title">Touriste</div>
                <div class="choice-desc">Je cherche des sites à visiter au Cameroun</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Je suis touriste", key="btn_tourist", use_container_width=True):
                st.session_state.role = 'touriste'
                st.session_state.page = 'explorer'
                st.rerun()
        
        with c2:
            st.markdown("""
            <div class="choice-card">
                <div class="choice-icon">🏡</div>
                <div class="choice-title">Propriétaire</div>
                <div class="choice-desc">Je veux référencer mon site touristique</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Je suis propriétaire", key="btn_owner", use_container_width=True):
                st.session_state.role = 'proprietaire'
                st.session_state.page = 'enregistrer'
                st.rerun()
    
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <div class="footer-box">
            <p style="margin: 0;">📚 TP INF232 EC2 - Collecte et Analyse de Données</p>
            <p style="margin: 0.5rem 0;"><span class="gold-badge">24F2551 | NDOUMA NANG SOSTHENE ASTIN</span></p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============ PAGES APRÈS CHOIX ============
else:
    # Sidebar
    st.sidebar.markdown("### 🇨🇲 TANAP")
    st.sidebar.markdown(f"*Connecté en tant que: **{st.session_state.role.upper()}***")
    st.sidebar.markdown("---")
    
    if st.sidebar.button("🏠 Accueil", use_container_width=True):
        st.session_state.page = 'accueil'
    if st.sidebar.button("🔍 Explorer les sites", use_container_width=True):
        st.session_state.page = 'explorer'
    if st.sidebar.button("📝 Enregistrer un site", use_container_width=True):
        st.session_state.page = 'enregistrer'
    if st.sidebar.button("📊 Tableau de bord", use_container_width=True):
        st.session_state.page = 'dashboard'
    
    st.sidebar.markdown("---")
    if st.sidebar.button("🚪 Changer de profil", use_container_width=True):
        st.session_state.role = None
        st.rerun()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Matricule:** 24F2551")
    st.sidebar.markdown("**NDOUMA NANG**")
    st.sidebar.markdown("**SOSTHENE ASTIN**")
    
    df = get_df()
    
    # PAGE ACCUEIL
    if st.session_state.page == 'accueil':
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("## 🏠 Bienvenue sur TANAP")
        st.write(f"Vous êtes connecté en tant que **{st.session_state.role}**.")
        st.write("Utilisez le menu à gauche pour naviguer.")
        
        st.markdown("### 📈 Aperçu rapide")
        c1, c2, c3 = st.columns(3)
        c1.metric("Sites disponibles", len(df))
        c2.metric("Régions couvertes", df['region'].nunique())
        c3.metric("Note moyenne", f"{df['note'].mean():.1f}/5")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # PAGE EXPLORER
    elif st.session_state.page == 'explorer':
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("## 🔍 Explorer les Sites Touristiques")
        
        # Filtres
        col1, col2 = st.columns(2)
        with col1:
            region = st.selectbox("📍 Filtrer par région", ['Toutes'] + list(df['region'].unique()))
        with col2:
            categorie = st.selectbox("🏷️ Filtrer par catégorie", ['Toutes'] + list(df['categorie'].unique()))
        
        filtered = df.copy()
        if region != 'Toutes':
            filtered = filtered[filtered['region'] == region]
        if categorie != 'Toutes':
            filtered = filtered[filtered['categorie'] == categorie]
        
        st.markdown(f"**{len(filtered)} site(s) trouvé(s)**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        for _, site in filtered.iterrows():
            st.markdown(f"""
            <div class="site-card">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <h3 style="margin: 0;">{site['nom']}</h3>
                        <p style="color: #666; margin: 0.3rem 0;">{site['ville']}, {site['region']}</p>
                    </div>
                    <span class="green-badge">{site['categorie']}</span>
                </div>
                <p style="margin: 1rem 0;">{site['description']}</p>
                <div style="display: flex; gap: 2rem; flex-wrap: wrap; color: #555;">
                    <span>💰 <strong>{site['prix_entree']:,} FCFA</strong></span>
                    <span>⭐ <strong>{site['note']}/5</strong> ({site['avis']} avis)</span>
                    <span>🕐 {site['horaires']}</span>
                </div>
                <p style="margin-top: 0.5rem; color: #666; font-size: 0.9rem;">
                    📞 {site['contact']} | ✉️ {site['email']}
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    # PAGE ENREGISTRER
    elif st.session_state.page == 'enregistrer':
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("## 📝 Enregistrer votre Site")
        st.write("Remplissez ce formulaire pour ajouter votre site touristique.")
        
        with st.form("new_site"):
            nom = st.text_input("🏛️ Nom du site")
            col1, col2 = st.columns(2)
            with col1:
                region = st.selectbox("📍 Région", ["Centre", "Littoral", "Ouest", "Sud", "Sud-Ouest", "Nord-Ouest", "Est", "Adamaoua", "Nord", "Extrême-Nord"])
                ville = st.text_input("🏘️ Ville")
                categorie = st.selectbox("🏷️ Catégorie", ["Nature", "Monument", "Culture", "Safari", "Plage", "Musée", "Autre"])
            with col2:
                prix = st.number_input("💰 Prix d'entrée (FCFA)", min_value=0, step=100)
                horaires = st.text_input("🕐 Horaires (ex: 08h - 17h)")
                contact = st.text_input("📞 Téléphone")
            
            email = st.text_input("✉️ Email")
            description = st.text_area("📄 Description du site")
            proprietaire = st.text_input("👤 Votre nom complet")
            
            submitted = st.form_submit_button("✅ Enregistrer le site", use_container_width=True)
            
            if submitted:
                if nom and ville and description and proprietaire:
                    new_site = {
                        "id": len(st.session_state.sites) + 1,
                        "nom": nom, "region": region, "ville": ville,
                        "categorie": categorie, "description": description,
                        "prix_entree": prix, "horaires": horaires,
                        "contact": contact, "email": email,
                        "note": 0, "avis": 0,
                        "date": datetime.now().strftime("%Y-%m-%d")
                    }
                    st.session_state.sites.append(new_site)
                    st.success(f"✅ Le site '{nom}' a été enregistré avec succès!")
                    st.balloons()
                else:
                    st.error("⚠️ Veuillez remplir tous les champs obligatoires.")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # PAGE DASHBOARD
    elif st.session_state.page == 'dashboard':
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        st.markdown("## 📊 Tableau de Bord - Analyse des Données")
        
        pwd = st.text_input("🔐 Mot de passe administrateur", type="password")
        
        if pwd == "tanap2024":
            st.success("✅ Accès autorisé")
            
            # KPIs
            st.markdown("### 📈 Indicateurs Clés")
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Total Sites", len(df))
            c2.metric("Régions", df['region'].nunique())
            c3.metric("Note Moyenne", f"{df['note'].mean():.2f}")
            c4.metric("Total Avis", df['avis'].sum())
            
            # Graphiques
            st.markdown("### 📊 Visualisations")
            col1, col2 = st.columns(2)
            with col1:
                fig = px.pie(df, names='region', title="Répartition par Région")
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig, use_container_width=True)
            with col2:
                fig = px.bar(df, x='categorie', title="Sites par Catégorie", color='categorie')
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig, use_container_width=True)
            
            # Stats
            st.markdown("### 📋 Statistiques Descriptives")
            stats = df[['prix_entree', 'note', 'avis']].describe()
            stats.columns = ['Prix (FCFA)', 'Note', 'Avis']
            st.dataframe(stats, use_container_width=True)
            
            # Table
            st.markdown("### 📑 Données Complètes")
            st.dataframe(df[['nom', 'region', 'ville', 'categorie', 'prix_entree', 'note', 'avis']], use_container_width=True)
            
            # Export
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Télécharger les données (CSV)", csv, "tanap_donnees.csv")
        
        elif pwd:
            st.error("❌ Mot de passe incorrect")
        else:
            st.info("💡 Entrez le mot de passe: **tanap2024**")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer-box">
        <strong>🇨🇲 TANAP</strong> - Guide Touristique Camerounais<br>
        <small>TP INF232 EC2 | Application de Collecte et Analyse de Données</small><br>
        <span class="gold-badge" style="margin-top: 0.5rem;">Matricule: 24F2551 | NDOUMA NANG SOSTHENE ASTIN</span>
    </div>
    """, unsafe_allow_html=True)
