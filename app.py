import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Config
st.set_page_config(page_title="TANAP - Cameroun", page_icon="🇨🇲", layout="wide")

# REMPLACEZ PAR VOTRE LIEN IMAGE
BG_IMAGE = "https://raw.githubusercontent.com/astinndouma24-a11y/24F2551-NDOUMA-NANG-SOSTHENE-ASTIN/main/image%20de%20fond.jpg"

# PANTONE 116 C = #FFCC00 (Or)
GOLD = "#FFCC00"
GOLD_DARK = "#D4A900"
GOLD_LIGHT = "#FFE066"
DARK = "#1a1a1a"
DARK_SOFT = "#2d2d2d"

# CSS Thème Or Premium
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600&display=swap');
    
    * {{
        font-family: 'Montserrat', sans-serif;
    }}
    
    h1, h2, h3, .title {{
        font-family: 'Playfair Display', serif !important;
    }}
    
    .stApp {{
        background: linear-gradient(135deg, {DARK} 0%, {DARK_SOFT} 100%);
    }}
    
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {DARK} 0%, #0a0a0a 100%);
        border-right: 2px solid {GOLD};
    }}
    
    section[data-testid="stSidebar"] * {{
        color: white !important;
    }}
    
    section[data-testid="stSidebar"] .stButton > button {{
        background: transparent !important;
        border: 2px solid {GOLD} !important;
        color: {GOLD} !important;
        border-radius: 8px !important;
    }}
    
    section[data-testid="stSidebar"] .stButton > button:hover {{
        background: {GOLD} !important;
        color: {DARK} !important;
    }}
    
    .main-container {{
        background: white;
        border-radius: 20px;
        margin: 1rem auto;
        max-width: 1100px;
        box-shadow: 0 0 50px rgba(255, 204, 0, 0.2);
        overflow: hidden;
        border: 2px solid {GOLD};
    }}
    
    .hero-section {{
        display: flex;
        min-height: 480px;
    }}
    
    .hero-image {{
        flex: 1.2;
        background-image: url("{BG_IMAGE}");
        background-size: cover;
        background-position: center;
        position: relative;
    }}
    
    .hero-image::after {{
        content: '';
        position: absolute;
        top: 0;
        right: 0;
        width: 100px;
        height: 100%;
        background: linear-gradient(90deg, transparent, white);
    }}
    
    .hero-content {{
        flex: 1;
        padding: 3rem;
        display: flex;
        flex-direction: column;
        justify-content: center;
        background: white;
    }}
    
    .app-logo {{
        color: {DARK};
        font-size: 3.2rem;
        font-weight: 700;
        font-family: 'Playfair Display', serif;
        margin-bottom: 0.3rem;
    }}
    
    .app-logo span {{
        color: {GOLD_DARK};
    }}
    
    .app-slogan {{
        color: #666;
        font-size: 0.95rem;
        font-style: italic;
        margin-bottom: 1.5rem;
        letter-spacing: 1px;
    }}
    
    .gold-line {{
        height: 4px;
        width: 80px;
        background: linear-gradient(90deg, {GOLD}, {GOLD_DARK});
        margin: 1.5rem 0;
        border-radius: 2px;
    }}
    
    .question-text {{
        color: {DARK};
        font-size: 1.4rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
        font-family: 'Playfair Display', serif;
    }}
    
    .choice-card {{
        background: #fafafa;
        border: 2px solid #e5e5e5;
        border-radius: 15px;
        padding: 2rem 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        margin: 0.5rem;
    }}
    
    .choice-card:hover {{
        border-color: {GOLD};
        transform: translateY(-8px);
        box-shadow: 0 15px 40px rgba(255, 204, 0, 0.25);
    }}
    
    .choice-icon {{
        font-size: 3rem;
        margin-bottom: 0.8rem;
    }}
    
    .choice-title {{
        color: {DARK};
        font-size: 1.3rem;
        font-weight: 600;
        font-family: 'Playfair Display', serif;
    }}
    
    .choice-desc {{
        color: #888;
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }}
    
    .content-card {{
        background: white;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 5px 30px rgba(0,0,0,0.3);
        border-top: 4px solid {GOLD};
    }}
    
    .section-title {{
        color: {DARK};
        font-size: 1.6rem;
        font-weight: 600;
        font-family: 'Playfair Display', serif;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }}
    
    .section-title::before {{
        content: '';
        width: 5px;
        height: 30px;
        background: {GOLD};
        border-radius: 3px;
    }}
    
    .site-item {{
        background: #fafafa;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid {GOLD};
        transition: all 0.2s;
    }}
    
    .site-item:hover {{
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transform: translateX(5px);
    }}
    
    .site-name {{
        color: {DARK};
        font-size: 1.25rem;
        font-weight: 600;
        font-family: 'Playfair Display', serif;
        margin-bottom: 0.2rem;
    }}
    
    .site-location {{
        color: #777;
        font-size: 0.9rem;
    }}
    
    .tag {{
        display: inline-block;
        background: {GOLD};
        color: {DARK};
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    
    .tag-dark {{
        background: {DARK};
        color: {GOLD};
    }}
    
    .stat-box {{
        background: linear-gradient(135deg, {DARK}, {DARK_SOFT});
        border: 2px solid {GOLD};
        color: white;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }}
    
    .stat-number {{
        font-size: 2.5rem;
        font-weight: 700;
        color: {GOLD};
        font-family: 'Playfair Display', serif;
    }}
    
    .stat-label {{
        font-size: 0.8rem;
        color: #ccc;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.3rem;
    }}
    
    .footer-bar {{
        background: linear-gradient(90deg, {DARK}, {DARK_SOFT});
        border: 2px solid {GOLD};
        color: white;
        padding: 1.2rem 2rem;
        border-radius: 12px;
        text-align: center;
        margin-top: 2rem;
    }}
    
    .gold-badge {{
        background: {GOLD};
        color: {DARK};
        padding: 0.5rem 1.5rem;
        border-radius: 25px;
        font-weight: 700;
        font-size: 0.9rem;
        display: inline-block;
        margin-top: 0.5rem;
    }}
    
    .stButton > button {{
        background: {GOLD} !important;
        color: {DARK} !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 600 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        transition: all 0.3s !important;
    }}
    
    .stButton > button:hover {{
        background: {GOLD_DARK} !important;
        transform: scale(1.02);
        box-shadow: 0 5px 20px rgba(255, 204, 0, 0.4) !important;
    }}
    
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {{
        border-radius: 8px !important;
        border: 2px solid #ddd !important;
        background: white !important;
    }}
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {{
        border-color: {GOLD} !important;
        box-shadow: 0 0 10px rgba(255, 204, 0, 0.3) !important;
    }}
    
    .stSelectbox > div > div {{
        border-radius: 8px !important;
    }}
    
    .metric-container {{
        background: white;
        border-radius: 10px;
        padding: 1rem;
        border-left: 4px solid {GOLD};
    }}
    
    [data-testid="metric-container"] {{
        background: white;
        border-radius: 10px;
        padding: 1rem;
        border-left: 4px solid {GOLD};
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

# =============== PAGE ACCUEIL ===============
if st.session_state.role is None:
    st.markdown(f"""
    <div class="main-container">
        <div class="hero-section">
            <div class="hero-image"></div>
            <div class="hero-content">
                <div class="app-logo">🇨🇲 <span>TANAP</span></div>
                <div class="app-slogan">Tourisme Authentique et Naturel en Afrique - Portail Cameroun</div>
                <div class="gold-line"></div>
                <div class="question-text">Bienvenue ! Qui êtes-vous ?</div>
                <div style="display: flex; gap: 1rem;">
                    <div class="choice-card" style="flex: 1;">
                        <div class="choice-icon">🧳</div>
                        <div class="choice-title">Touriste</div>
                        <div class="choice-desc">Je recherche des sites à visiter</div>
                    </div>
                    <div class="choice-card" style="flex: 1;">
                        <div class="choice-icon">🏠</div>
                        <div class="choice-title">Propriétaire</div>
                        <div class="choice-desc">Je veux référencer mon site</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("ENTRER COMME TOURISTE", use_container_width=True):
                st.session_state.role = 'touriste'
                st.session_state.page = 'explorer'
                st.rerun()
        with c2:
            if st.button("ENTRER COMME PROPRIÉTAIRE", use_container_width=True):
                st.session_state.role = 'proprietaire'
                st.session_state.page = 'enregistrer'
                st.rerun()
    
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem;">
        <div class="footer-bar">
            📚 <strong>TP INF232 EC2</strong> - Application de Collecte et Analyse de Données<br>
            <span class="gold-badge">MATRICULE: 24F2551 | NDOUMA NANG SOSTHENE ASTIN</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =============== PAGES INTERNES ===============
else:
    with st.sidebar:
        st.markdown(f"### 🇨🇲 **TANAP**")
        st.markdown(f"*{st.session_state.role.upper()}*")
        st.markdown("---")
        
        if st.button("🏠 ACCUEIL", use_container_width=True):
            st.session_state.page = 'accueil'
        if st.button("🔍 EXPLORER", use_container_width=True):
            st.session_state.page = 'explorer'
        if st.button("📝 ENREGISTRER", use_container_width=True):
            st.session_state.page = 'enregistrer'
        if st.button("📊 DASHBOARD", use_container_width=True):
            st.session_state.page = 'dashboard'
        
        st.markdown("---")
        if st.button("🔄 CHANGER PROFIL", use_container_width=True):
            st.session_state.role = None
            st.rerun()
        
        st.markdown("---")
        st.markdown("**24F2551**")
        st.markdown("NDOUMA NANG")
        st.markdown("SOSTHENE ASTIN")
    
    df = get_df()
    
    if st.session_state.page == 'accueil':
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Tableau de Bord</div>', unsafe_allow_html=True)
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{len(df)}</div><div class="stat-label">Sites</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{df["region"].nunique()}</div><div class="stat-label">Régions</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{df["note"].mean():.1f}</div><div class="stat-label">Note Moy.</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="stat-box"><div class="stat-number">{df["avis"].sum()}</div><div class="stat-label">Avis</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif st.session_state.page == 'explorer':
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Explorer les Sites Touristiques</div>', unsafe_allow_html=True)
        
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
        
        st.markdown(f"**{len(filtered)} site(s)**")
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
                <p style="color: #555; margin: 1rem 0; line-height: 1.6;">{site['description']}</p>
                <div style="display: flex; gap: 1.5rem; flex-wrap: wrap; font-size: 0.9rem; color: #666;">
                    <span>💰 <strong>{site['prix']:,} FCFA</strong></span>
                    <span>⭐ <strong>{site['note']}/5</strong> ({site['avis']} avis)</span>
                    <span>🕐 {site['horaires']}</span>
                    <span>📞 {site['contact']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    elif st.session_state.page == 'enregistrer':
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Enregistrer Votre Site</div>', unsafe_allow_html=True)
        
        with st.form("form"):
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
            proprietaire = st.text_input("👤 Votre nom complet *")
            
            if st.form_submit_button("✅ ENREGISTRER LE SITE", use_container_width=True):
                if nom and ville and description and proprietaire:
                    new = {"id": len(st.session_state.sites)+1, "nom": nom, "region": region, "ville": ville,
                           "categorie": categorie, "description": description, "prix": prix, "horaires": horaires,
                           "contact": contact, "email": email, "note": 0, "avis": 0}
                    st.session_state.sites.append(new)
                    st.success(f"✅ '{nom}' enregistré avec succès !")
                    st.balloons()
                else:
                    st.error("⚠️ Remplissez les champs obligatoires")
        st.markdown('</div>', unsafe_allow_html=True)
    
    elif st.session_state.page == 'dashboard':
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Analyse des Données</div>', unsafe_allow_html=True)
        
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Sites", len(df))
        c2.metric("Régions", df['region'].nunique())
        c3.metric("Catégories", df['categorie'].nunique())
        c4.metric("Note Moy.", f"{df['note'].mean():.2f}")
        c5.metric("Avis Total", df['avis'].sum())
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            fig = px.pie(df, names='region', title="Répartition par Région", 
                        color_discrete_sequence=['#FFCC00', '#D4A900', '#FFE066', '#B8960A', '#FFDB4D'])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='#333')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            fig = px.bar(df, x='nom', y='note', title="Notes par Site", color_discrete_sequence=['#FFCC00'])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', font_color='#333')
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("**Statistiques Descriptives**")
        stats = df[['prix', 'note', 'avis']].describe()
        stats.columns = ['Prix (FCFA)', 'Note', 'Avis']
        st.dataframe(stats.round(2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="content-card">', unsafe_allow_html=True)
        st.markdown("**Données Complètes**")
        st.dataframe(df[['nom', 'region', 'ville', 'categorie', 'prix', 'note', 'avis']], use_container_width=True, hide_index=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 EXPORTER CSV", csv, "tanap_data.csv", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div class="footer-bar">
        🇨🇲 <strong>TANAP</strong> - Guide Touristique Camerounais<br>
        <span class="gold-badge">24F2551 | NDOUMA NANG SOSTHENE ASTIN</span>
    </div>
    """, unsafe_allow_html=True)
