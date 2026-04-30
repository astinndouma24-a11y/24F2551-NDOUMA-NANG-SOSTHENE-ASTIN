import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Config
st.set_page_config(page_title="TANAP - Cameroun", page_icon="🇨🇲", layout="wide")

# REMPLACEZ PAR VOTRE LIEN IMAGE (GitHub ou Imgur)
BG_IMAGE = "https://raw.githubusercontent.com/VOTRE_USERNAME/24F2551-NDOUMA-NANG-SOSTHENE-ASTIN/main/image%20de%20fond.jpg"

# CSS Style GlowSpot adapté - Tons bleu-vert doux
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {{
        font-family: 'Poppins', sans-serif;
    }}
    
    .stApp {{
        background: linear-gradient(135deg, #e8f4f3 0%, #d4e8e6 50%, #c5dbd9 100%);
    }}
    
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #1a5c4c 0%, #0d3d31 100%);
    }}
    
    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}
    
    section[data-testid="stSidebar"] .stButton > button {{
        background: rgba(255,255,255,0.15) !important;
        border: 1px solid rgba(255,255,255,0.3) !important;
        color: white !important;
    }}
    
    section[data-testid="stSidebar"] .stButton > button:hover {{
        background: rgba(255,255,255,0.25) !important;
    }}
    
    .main-container {{
        background: white;
        border-radius: 25px;
        padding: 0;
        margin: 1rem auto;
        max-width: 1100px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        overflow: hidden;
    }}
    
    .hero-section {{
        display: flex;
        min-height: 450px;
    }}
    
    .hero-image {{
        flex: 1;
        background-image: url("{BG_IMAGE}");
        background-size: cover;
        background-position: center;
        border-radius: 25px;
        margin: 20px;
    }}
    
    .hero-content {{
        flex: 1;
        padding: 3rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    
    .app-logo {{
        color: #1a5c4c;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }}
    
    .app-slogan {{
        color: #666;
        font-size: 1rem;
        font-style: italic;
        margin-bottom: 2rem;
    }}
    
    .divider {{
        height: 3px;
        background: linear-gradient(90deg, #c9a227 0%, #c9a227 30%, #e0e0e0 30%);
        margin: 1.5rem 0;
        border: none;
    }}
    
    .question-text {{
        color: #333;
        font-size: 1.3rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
    }}
    
    .choice-container {{
        display: flex;
        gap: 1.5rem;
        margin-top: 1rem;
    }}
    
    .choice-card {{
        flex: 1;
        background: #f8fafa;
        border: 2px solid #e8f0ef;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
    }}
    
    .choice-card:hover {{
        border-color: #1a5c4c;
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(26,92,76,0.15);
    }}
    
    .choice-icon {{
        font-size: 3.5rem;
        margin-bottom: 1rem;
    }}
    
    .choice-title {{
        color: #1a5c4c;
        font-size: 1.2rem;
        font-weight: 600;
    }}
    
    .choice-desc {{
        color: #888;
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }}
    
    .content-card {{
        background: white;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.08);
    }}
    
    .section-title {{
        color: #1a5c4c;
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #c9a227;
        display: inline-block;
    }}
    
    .site-item {{
        background: #f8fafa;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #1a5c4c;
        transition: all 0.2s;
    }}
    
    .site-item:hover {{
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }}
    
    .site-name {{
        color: #1a5c4c;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }}
    
    .site-location {{
        color: #888;
        font-size: 0.9rem;
    }}
    
    .tag {{
        display: inline-block;
        background: #1a5c4c;
        color: white;
        padding: 0.2rem 0.8rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: 500;
    }}
    
    .tag-gold {{
        background: #c9a227;
    }}
    
    .stat-box {{
        background: linear-gradient(135deg, #1a5c4c, #0d3d31);
        color: white;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
    }}
    
    .stat-number {{
        font-size: 2.5rem;
        font-weight: 700;
    }}
    
    .stat-label {{
        font-size: 0.85rem;
        opacity: 0.9;
    }}
    
    .footer-bar {{
        background: #1a5c4c;
        color: white;
        padding: 1rem 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 2rem;
    }}
    
    .gold-badge {{
        background: #c9a227;
        color: white;
        padding: 0.4rem 1.2rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }}
    
    .stButton > button {{
        background: #1a5c4c !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 500 !important;
        transition: all 0.3s !important;
    }}
    
    .stButton > button:hover {{
        background: #c9a227 !important;
        transform: scale(1.02);
    }}
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea,
    .stSelectbox > div > div {{
        border-radius: 12px !important;
        border: 2px solid #e0e0e0 !important;
    }}
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {{
        border-color: #1a5c4c !important;
    }}
</style>
""", unsafe_allow_html=True)

# Données
SITES = [
    {"id": 1, "nom": "Monument de la Réunification", "region": "Centre", "ville": "Yaoundé", 
     "categorie": "Monument", "description": "Symbole de l'unité nationale camerounaise, érigé en 1972 pour commémorer la réunification.", 
     "prix": 500, "horaires": "08h - 17h", "contact": "+237 677 12 34 56", "email": "info@monument.cm", "note": 4.5, "avis": 38},
    {"id": 2, "nom": "Chutes de la Lobé", "region": "Sud", "ville": "Kribi",
     "categorie": "Nature", "description": "Chutes uniques se jetant directement dans l'océan Atlantique.",
     "prix": 1000, "horaires": "07h - 18h", "contact": "+237 699 45 67 89", "email": "lobe@tourisme.cm", "note": 4.8, "avis": 27},
    {"id": 3, "nom": "Palais Royal Bamoun", "region": "Ouest", "ville": "Foumban",
     "categorie": "Culture", "description": "Résidence du Sultan, musée d'art et d'histoire Bamoun.",
     "prix": 2000, "horaires": "09h - 16h", "contact": "+237 655 78 90 12", "email": "palais@foumban.cm", "note": 4.6, "avis": 22},
    {"id": 4, "nom": "Mont Cameroun", "region": "Sud-Ouest", "ville": "Buéa",
     "categorie": "Nature", "description": "Plus haut sommet d'Afrique de l'Ouest, randonnées guidées disponibles.",
     "prix": 5000, "horaires": "06h - 15h", "contact": "+237 670 23 45 67", "email": "montcam@guide.cm", "note": 4.7, "avis": 15},
    {"id": 5, "nom": "Parc National de Waza", "region": "Extrême-Nord", "ville": "Waza",
     "categorie": "Safari", "description": "Safari authentique : éléphants, lions, girafes.",
     "prix": 3000, "horaires": "06h - 18h", "contact": "+237 622 56 78 90", "email": "waza@parcs.cm", "note": 4.4, "avis": 12},
]

# Session
if 'sites' not in st.session_state:
    st.session_state.sites = SITES.copy()
if 'role' not in st.session_state:
    st.session_state.role = None
if 'page' not in st.session_state:
    st.session_state.page = 'accueil'

def get_df():
    return pd.DataFrame(st.session_state.sites)

# =============== PAGE ACCUEIL - CHOIX RÔLE ===============
if st.session_state.role is None:
    st.markdown(f"""
    <div class="main-container">
        <div class="hero-section">
            <div class="hero-image"></div>
            <div class="hero-content">
                <div class="app-logo">🇨🇲 TANAP</div>
                <div class="app-slogan">Découvrez les merveilles du Cameroun, l'Afrique en miniature</div>
                <div class="divider"></div>
                <div class="question-text">Qui êtes-vous ?</div>
                <div class="choice-container">
                    <div class="choice-card" id="tourist-card">
                        <div class="choice-icon">🧳</div>
                        <div class="choice-title">Touriste</div>
                        <div class="choice-desc">Je recherche des sites à visiter</div>
                    </div>
                    <div class="choice-card" id="owner-card">
                        <div class="choice-icon">🏠</div>
                        <div class="choice-title">Propriétaire</div>
                        <div class="choice-desc">Je veux référencer mon site</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Boutons (cachés visuellement mais fonctionnels)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Je suis Touriste", use_container_width=True):
                st.session_state.role = 'touriste'
                st.session_state.page = 'explorer'
                st.rerun()
        with c2:
            if st.button("Je suis Propriétaire", use_container_width=True):
                st.session_state.role = 'proprietaire'
                st.session_state.page = 'enregistrer'
                st.rerun()
    
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <div class="footer-bar">
            📚 TP INF232 EC2 - Collecte et Analyse de Données<br>
            <span class="gold-badge" style="margin-top: 0.5rem; display: inline-block;">24F2551 | NDOUMA NANG SOSTHENE ASTIN</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =============== PAGES APRÈS CONNEXION ===============
else:
    # Sidebar
    with st.sidebar:
        st.markdown("### 🇨🇲 TANAP")
        st.markdown(f"**Profil:** {st.session_state.role.capitalize()}")
        st.markdown("---")
        
        if st.button("🏠 Accueil", use_container_width=True):
            st.session_state.page = 'accueil'
        if st.button("🔍 Explorer", use_container_width=True):
            st.session_state.page = 'explorer'
        if st.button("📝 Enregistrer", use_container_width=True):
            st.session_state.page = 'enregistrer'
        if st.button("📊 Dashboard", use_container_width=True):
            st.session_state.page = 'dashboard'
        
        st.markdown("---")
        if st.button("🔄 Changer profil", use_container_width=True):
            st.session_state.role = None
            st.rerun()
        
        st.markdown("---")
        st.markdown("**Matricule:** 24F2551")
        st.markdown("**NDOUMA NANG**")
        st.markdown("**SOSTHENE ASTIN**")
    
    df = get_df()
    
    # PAGE ACCUEIL
    if st.session_state.page == 'accueil':
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Bienvenue sur TANAP</div>', unsafe_allow_html=True)
        st.write(f"Vous êtes connecté en tant que **{st.session_state.role}**. Explorez le Cameroun !")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{len(df)}</div><div class="stat-label">Sites</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{df["region"].nunique()}</div><div class="stat-label">Régions</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{df["note"].mean():.1f}</div><div class="stat-label">Note moy.</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{df["avis"].sum()}</div><div class="stat-label">Avis</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # PAGE EXPLORER
    elif st.session_state.page == 'explorer':
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Explorer les Sites</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            region = st.selectbox("📍 Région", ['Toutes'] + list(df['region'].unique()))
        with col2:
            cat = st.selectbox("🏷️ Catégorie", ['Toutes'] + list(df['categorie'].unique()))
        with col3:
            tri = st.selectbox("📊 Trier par", ['Note', 'Prix', 'Avis'])
        
        filtered = df.copy()
        if region != 'Toutes':
            filtered = filtered[filtered['region'] == region]
        if cat != 'Toutes':
            filtered = filtered[filtered['categorie'] == cat]
        
        if tri == 'Note':
            filtered = filtered.sort_values('note', ascending=False)
        elif tri == 'Prix':
            filtered = filtered.sort_values('prix')
        else:
            filtered = filtered.sort_values('avis', ascending=False)
        
        st.markdown(f"**{len(filtered)} site(s) trouvé(s)**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        for _, site in filtered.iterrows():
            st.markdown(f"""
            <div class="site-item">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <div class="site-name">{site['nom']}</div>
                        <div class="site-location">📍 {site['ville']}, {site['region']}</div>
                    </div>
                    <span class="tag">{site['categorie']}</span>
                </div>
                <p style="color: #555; margin: 1rem 0;">{site['description']}</p>
                <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; font-size: 0.9rem; color: #666;">
                    <span>💰 <strong>{site['prix']:,} FCFA</strong></span>
                    <span>⭐ <strong>{site['note']}/5</strong> ({site['avis']} avis)</span>
                    <span>🕐 {site['horaires']}</span>
                    <span>📞 {site['contact']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # PAGE ENREGISTRER
    elif st.session_state.page == 'enregistrer':
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Enregistrer un Site</div>', unsafe_allow_html=True)
        
        with st.form("site_form"):
            nom = st.text_input("🏛️ Nom du site *")
            
            col1, col2 = st.columns(2)
            with col1:
                region = st.selectbox("📍 Région *", ["Centre", "Littoral", "Ouest", "Sud", "Sud-Ouest", "Nord-Ouest", "Est", "Adamaoua", "Nord", "Extrême-Nord"])
                ville = st.text_input("🏘️ Ville *")
                categorie = st.selectbox("🏷️ Catégorie *", ["Nature", "Monument", "Culture", "Safari", "Plage", "Musée"])
            with col2:
                prix = st.number_input("💰 Prix (FCFA)", min_value=0, step=100)
                horaires = st.text_input("🕐 Horaires")
                contact = st.text_input("📞 Téléphone")
            
            email = st.text_input("✉️ Email")
            description = st.text_area("📝 Description *")
            proprietaire = st.text_input("👤 Votre nom *")
            
            if st.form_submit_button("✅ Enregistrer", use_container_width=True):
                if nom and ville and description and proprietaire:
                    new = {"id": len(st.session_state.sites)+1, "nom": nom, "region": region, "ville": ville,
                           "categorie": categorie, "description": description, "prix": prix, "horaires": horaires,
                           "contact": contact, "email": email, "note": 0, "avis": 0}
                    st.session_state.sites.append(new)
                    st.success(f"✅ '{nom}' enregistré avec succès !")
                    st.balloons()
                else:
                    st.error("⚠️ Remplissez les champs obligatoires (*)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # PAGE DASHBOARD (SANS MOT DE PASSE)
    elif st.session_state.page == 'dashboard':
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📊 Tableau de Bord Analytique</div>', unsafe_allow_html=True)
        
        # KPIs
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Sites", len(df))
        c2.metric("Régions", df['region'].nunique())
        c3.metric("Catégories", df['categorie'].nunique())
        c4.metric("Note Moy.", f"{df['note'].mean():.2f}")
        c5.metric("Total Avis", df['avis'].sum())
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Graphiques
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.markdown("**Répartition par Région**")
            fig = px.pie(df, names='region', hole=0.4, color_discrete_sequence=px.colors.sequential.Teal)
            fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), paper_bgcolor='rgba(0,0,0,0)')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.markdown("**Sites par Catégorie**")
            fig = px.bar(df['categorie'].value_counts(), color_discrete_sequence=['#1a5c4c'])
            fig.update_layout(margin=dict(t=20, b=20, l=20, r=20), paper_bgcolor='rgba(0,0,0,0)', showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        # Stats descriptives
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("**Statistiques Descriptives**")
        stats = df[['prix', 'note', 'avis']].describe()
        stats.columns = ['Prix (FCFA)', 'Note', 'Avis']
        st.dataframe(stats.round(2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Données
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("**Base de Données**")
        st.dataframe(df[['nom', 'region', 'ville', 'categorie', 'prix', 'note', 'avis']], use_container_width=True, hide_index=True)
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Exporter CSV", csv, "tanap_data.csv", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="footer-bar">
        🇨🇲 <strong>TANAP</strong> - Guide Touristique Camerounais | TP INF232 EC2<br>
        <span class="gold-badge">24F2551 | NDOUMA NANG SOSTHENE ASTIN</span>
    </div>
    """, unsafe_allow_html=True)
