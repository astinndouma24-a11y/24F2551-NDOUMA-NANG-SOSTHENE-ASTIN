import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.set_page_config(page_title="TANAP - Cameroun", page_icon="🇨🇲", layout="wide")

# REMPLACEZ PAR VOTRE LIEN IMAGE
BG_IMAGE = "https://raw.githubusercontent.com/astinndouma24-a11y/24F2551-NDOUMA-NANG-SOSTHENE-ASTIN/main/image%20de%20fond.jpg"

# CSS - Or transparent + Texte lisible
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&display=swap');
    
    * {{
        font-family: Calibri, 'Segoe UI', Arial, sans-serif;
    }}
    
    h1, h2, h3, .titre {{
        font-family: 'Times New Roman', 'Libre Baskerville', Georgia, serif !important;
    }}
    
    .stApp {{
        background-color: #f5f5f0;
    }}
    
    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #2c2c2c 0%, #1a1a1a 100%);
        border-right: 3px solid #FFCC00;
    }}
    
    section[data-testid="stSidebar"] * {{
        color: #ffffff !important;
        font-family: Calibri, Arial, sans-serif !important;
    }}
    
    section[data-testid="stSidebar"] .stButton > button {{
        background: transparent !important;
        border: 2px solid #FFCC00 !important;
        color: #FFCC00 !important;
        border-radius: 5px !important;
        font-weight: bold !important;
    }}
    
    section[data-testid="stSidebar"] .stButton > button:hover {{
        background: #FFCC00 !important;
        color: #1a1a1a !important;
    }}
    
    /* Container principal */
    .main-box {{
        background: rgba(255, 255, 255, 0.95);
        border: 3px solid #FFCC00;
        border-radius: 15px;
        padding: 0;
        margin: 1rem auto;
        max-width: 1100px;
        box-shadow: 0 5px 30px rgba(0, 0, 0, 0.15);
        overflow: hidden;
    }}
    
    /* Hero section */
    .hero-wrapper {{
        display: flex;
        min-height: 450px;
    }}
    
    .hero-img {{
        flex: 1;
        background-image: url("{BG_IMAGE}");
        background-size: cover;
        background-position: center;
    }}
    
    .hero-text {{
        flex: 1;
        padding: 2.5rem;
        background: #ffffff;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }}
    
    .logo-titre {{
        font-family: 'Times New Roman', Georgia, serif;
        font-size: 2.8rem;
        font-weight: bold;
        color: #1a1a1a;
        margin-bottom: 0.5rem;
    }}
    
    .logo-titre span {{
        color: #D4A900;
    }}
    
    .slogan {{
        font-family: Calibri, Arial, sans-serif;
        font-size: 1rem;
        color: #555555;
        font-style: italic;
        margin-bottom: 1.5rem;
    }}
    
    .ligne-or {{
        width: 60px;
        height: 4px;
        background: #FFCC00;
        margin: 1rem 0;
    }}
    
    .question {{
        font-family: 'Times New Roman', Georgia, serif;
        font-size: 1.5rem;
        color: #1a1a1a;
        margin-bottom: 1.5rem;
    }}
    
    /* Cartes de choix */
    .choix-box {{
        display: flex;
        gap: 1rem;
    }}
    
    .choix-carte {{
        flex: 1;
        background: #fffef5;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s;
    }}
    
    .choix-carte:hover {{
        border-color: #FFCC00;
        box-shadow: 0 8px 25px rgba(255, 204, 0, 0.2);
        transform: translateY(-5px);
    }}
    
    .choix-icone {{
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }}
    
    .choix-titre {{
        font-family: 'Times New Roman', Georgia, serif;
        font-size: 1.3rem;
        font-weight: bold;
        color: #1a1a1a;
    }}
    
    .choix-desc {{
        font-family: Calibri, Arial, sans-serif;
        font-size: 0.9rem;
        color: #666666;
        margin-top: 0.3rem;
    }}
    
    /* Contenu pages */
    .page-carte {{
        background: #ffffff;
        border: 2px solid #FFCC00;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 3px 15px rgba(0, 0, 0, 0.08);
    }}
    
    .page-titre {{
        font-family: 'Times New Roman', Georgia, serif;
        font-size: 1.6rem;
        font-weight: bold;
        color: #1a1a1a;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #FFCC00;
    }}
    
    /* Liste des sites */
    .site-carte {{
        background: #fffef8;
        border-left: 4px solid #FFCC00;
        border-radius: 8px;
        padding: 1.2rem;
        margin: 0.8rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
    }}
    
    .site-nom {{
        font-family: 'Times New Roman', Georgia, serif;
        font-size: 1.2rem;
        font-weight: bold;
        color: #1a1a1a;
        margin-bottom: 0.2rem;
    }}
    
    .site-lieu {{
        font-family: Calibri, Arial, sans-serif;
        font-size: 0.9rem;
        color: #666666;
    }}
    
    .site-desc {{
        font-family: Calibri, Arial, sans-serif;
        font-size: 0.95rem;
        color: #444444;
        margin: 0.8rem 0;
        line-height: 1.5;
    }}
    
    .site-infos {{
        font-family: Calibri, Arial, sans-serif;
        font-size: 0.9rem;
        color: #555555;
    }}
    
    .etiquette {{
        display: inline-block;
        background: #FFCC00;
        color: #1a1a1a;
        padding: 0.2rem 0.7rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: bold;
        font-family: Calibri, Arial, sans-serif;
    }}
    
    /* Stats */
    .stat-boite {{
        background: linear-gradient(135deg, #2c2c2c, #1a1a1a);
        border: 2px solid #FFCC00;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
    }}
    
    .stat-chiffre {{
        font-family: 'Times New Roman', Georgia, serif;
        font-size: 2rem;
        font-weight: bold;
        color: #FFCC00;
    }}
    
    .stat-texte {{
        font-family: Calibri, Arial, sans-serif;
        font-size: 0.8rem;
        color: #cccccc;
        text-transform: uppercase;
    }}
    
    /* Footer */
    .pied-page {{
        background: #2c2c2c;
        border: 2px solid #FFCC00;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin-top: 2rem;
    }}
    
    .pied-page p {{
        font-family: Calibri, Arial, sans-serif;
        color: #ffffff;
        margin: 0.3rem 0;
    }}
    
    .badge-or {{
        display: inline-block;
        background: #FFCC00;
        color: #1a1a1a;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-family: Calibri, Arial, sans-serif;
        font-weight: bold;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }}
    
    /* Boutons */
    .stButton > button {{
        background: #FFCC00 !important;
        color: #1a1a1a !important;
        border: none !important;
        border-radius: 5px !important;
        font-family: Calibri, Arial, sans-serif !important;
        font-weight: bold !important;
        padding: 0.6rem 1.5rem !important;
    }}
    
    .stButton > button:hover {{
        background: #D4A900 !important;
    }}
    
    /* Inputs */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {{
        font-family: Calibri, Arial, sans-serif !important;
        border: 2px solid #dddddd !important;
        border-radius: 5px !important;
    }}
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {{
        border-color: #FFCC00 !important;
    }}
    
    /* Labels */
    .stTextInput > label, .stTextArea > label, .stSelectbox > label {{
        font-family: Calibri, Arial, sans-serif !important;
        color: #1a1a1a !important;
    }}
</style>
""", unsafe_allow_html=True)

# Données
SITES = [
    {"id": 1, "nom": "Monument de la Réunification", "region": "Centre", "ville": "Yaoundé", 
     "categorie": "Monument", "description": "Symbole de l'unité nationale camerounaise, érigé en 1972.", 
     "prix": 500, "horaires": "08h - 17h", "contact": "+237 677 12 34 56", "email": "info@monument.cm", "note": 4.5, "avis": 38},
    {"id": 2, "nom": "Chutes de la Lobé", "region": "Sud", "ville": "Kribi",
     "categorie": "Nature", "description": "Chutes uniques se jetant directement dans l'océan Atlantique.",
     "prix": 1000, "horaires": "07h - 18h", "contact": "+237 699 45 67 89", "email": "lobe@tourisme.cm", "note": 4.8, "avis": 27},
    {"id": 3, "nom": "Palais Royal Bamoun", "region": "Ouest", "ville": "Foumban",
     "categorie": "Culture", "description": "Résidence du Sultan, musée d'art et d'histoire Bamoun.",
     "prix": 2000, "horaires": "09h - 16h", "contact": "+237 655 78 90 12", "email": "palais@foumban.cm", "note": 4.6, "avis": 22},
    {"id": 4, "nom": "Mont Cameroun", "region": "Sud-Ouest", "ville": "Buéa",
     "categorie": "Nature", "description": "Plus haut sommet d'Afrique de l'Ouest, randonnées guidées.",
     "prix": 5000, "horaires": "06h - 15h", "contact": "+237 670 23 45 67", "email": "mont@guide.cm", "note": 4.7, "avis": 15},
    {"id": 5, "nom": "Parc National de Waza", "region": "Extrême-Nord", "ville": "Waza",
     "categorie": "Safari", "description": "Safari authentique avec éléphants, lions et girafes.",
     "prix": 3000, "horaires": "06h - 18h", "contact": "+237 622 56 78 90", "email": "waza@parcs.cm", "note": 4.4, "avis": 12},
]

if 'sites' not in st.session_state:
    st.session_state.sites = SITES.copy()
if 'role' not in st.session_state:
    st.session_state.role = None
if 'page' not in st.session_state:
    st.session_state.page = 'accueil'

def get_df():
    return pd.DataFrame(st.session_state.sites)

# ============ ACCUEIL - CHOIX ============
if st.session_state.role is None:
    st.markdown(f"""
    <div class="main-box">
        <div class="hero-wrapper">
            <div class="hero-img"></div>
            <div class="hero-text">
                <div class="logo-titre">🇨🇲 <span>TANAP</span></div>
                <div class="slogan">Tourisme Authentique et Naturel en Afrique - Portail Cameroun</div>
                <div class="ligne-or"></div>
                <div class="question">Bienvenue ! Qui êtes-vous ?</div>
                <div class="choix-box">
                    <div class="choix-carte">
                        <div class="choix-icone"></div>
                        <div class="choix-titre">Touriste</div>
                        <div class="choix-desc">Je recherche des sites à visiter</div>
                    </div>
                    <div class="choix-carte">
                        <div class="choix-icone"></div>
                        <div class="choix-titre">Propriétaire</div>
                        <div class="choix-desc">Je référence mon site touristique</div>
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
            if st.button("Entrer comme Touriste", use_container_width=True):
                st.session_state.role = 'touriste'
                st.session_state.page = 'explorer'
                st.rerun()
        with c2:
            if st.button("Entrer comme Propriétaire", use_container_width=True):
                st.session_state.role = 'proprietaire'
                st.session_state.page = 'enregistrer'
                st.rerun()
    
    st.markdown("""
    <div class="pied-page">
        <p><strong>TP INF232 EC2</strong> - Application de Collecte et Analyse de Données</p>
        <span class="badge-or">Matricule: 24F2551 | NDOUMA NANG SOSTHENE ASTIN</span>
    </div>
    """, unsafe_allow_html=True)

# ============ PAGES INTERNES ============
else:
    with st.sidebar:
        st.markdown("### 🇨🇲 TANAP")
        st.markdown(f"**Profil:** {st.session_state.role.capitalize()}")
        st.markdown("---")
        
        if st.button(" Accueil", use_container_width=True):
            st.session_state.page = 'accueil'
        if st.button(" Explorer", use_container_width=True):
            st.session_state.page = 'explorer'
        if st.button(" Enregistrer", use_container_width=True):
            st.session_state.page = 'enregistrer'
        if st.button(" Dashboard", use_container_width=True):
            st.session_state.page = 'dashboard'
        
        st.markdown("---")
        if st.button(" Changer profil", use_container_width=True):
            st.session_state.role = None
            st.rerun()
        
        st.markdown("---")
        st.markdown("**Matricule:** 24F2551")
        st.markdown("NDOUMA NANG")
        st.markdown("SOSTHENE ASTIN")
    
    df = get_df()
    
    # ACCUEIL
    if st.session_state.page == 'accueil':
        st.markdown('<div class="page-carte">', unsafe_allow_html=True)
        st.markdown('<div class="page-titre">Bienvenue sur TANAP</div>', unsafe_allow_html=True)
        st.write(f"Vous êtes connecté en tant que **{st.session_state.role}**.")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="stat-boite"><div class="stat-chiffre">{len(df)}</div><div class="stat-texte">Sites</div></div>', unsafe_allow_html=True)
        with c2:
            st.markdown(f'<div class="stat-boite"><div class="stat-chiffre">{df["region"].nunique()}</div><div class="stat-texte">Régions</div></div>', unsafe_allow_html=True)
        with c3:
            st.markdown(f'<div class="stat-boite"><div class="stat-chiffre">{df["note"].mean():.1f}</div><div class="stat-texte">Note Moy.</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="stat-boite"><div class="stat-chiffre">{df["avis"].sum()}</div><div class="stat-texte">Avis</div></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # EXPLORER
    elif st.session_state.page == 'explorer':
        st.markdown('<div class="page-carte">', unsafe_allow_html=True)
        st.markdown('<div class="page-titre">Explorer les Sites Touristiques</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            region = st.selectbox("Région", ['Toutes'] + list(df['region'].unique()))
        with col2:
            cat = st.selectbox("Catégorie", ['Toutes'] + list(df['categorie'].unique()))
        with col3:
            tri = st.selectbox("Trier par", ['Note', 'Prix', 'Avis'])
        
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
        
        st.write(f"**{len(filtered)} site(s) trouvé(s)**")
        st.markdown('</div>', unsafe_allow_html=True)
        
        for _, site in filtered.iterrows():
            st.markdown(f"""
            <div class="site-carte">
                <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                    <div>
                        <div class="site-nom">{site['nom']}</div>
                        <div class="site-lieu"> {site['ville']}, {site['region']}</div>
                    </div>
                    <span class="etiquette">{site['categorie']}</span>
                </div>
                <div class="site-desc">{site['description']}</div>
                <div class="site-infos">
                     <strong>{site['prix']:,} FCFA</strong> &nbsp;|&nbsp;
                     <strong>{site['note']}/5</strong> ({site['avis']} avis) &nbsp;|&nbsp;
                     {site['horaires']} &nbsp;|&nbsp;
                     {site['contact']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # ENREGISTRER
    elif st.session_state.page == 'enregistrer':
        st.markdown('<div class="page-carte">', unsafe_allow_html=True)
        st.markdown('<div class="page-titre">Enregistrer Votre Site Touristique</div>', unsafe_allow_html=True)
        
        with st.form("formulaire"):
            nom = st.text_input("Nom du site *")
            col1, col2 = st.columns(2)
            with col1:
                region = st.selectbox("Région *", ["Centre", "Littoral", "Ouest", "Sud", "Sud-Ouest", "Nord-Ouest", "Est", "Adamaoua", "Nord", "Extrême-Nord"])
                ville = st.text_input("Ville *")
                categorie = st.selectbox("Catégorie *", ["Nature", "Monument", "Culture", "Safari", "Plage", "Musée"])
            with col2:
                prix = st.number_input("Prix d'entrée (FCFA)", min_value=0, step=100)
                horaires = st.text_input("Horaires (ex: 08h - 17h)")
                contact = st.text_input("Téléphone")
            
            email = st.text_input("Email")
            description = st.text_area("Description du site *")
            proprietaire = st.text_input("Votre nom complet *")
            
            if st.form_submit_button("Enregistrer le site", use_container_width=True):
                if nom and ville and description and proprietaire:
                    new = {"id": len(st.session_state.sites)+1, "nom": nom, "region": region, "ville": ville,
                           "categorie": categorie, "description": description, "prix": prix, "horaires": horaires,
                           "contact": contact, "email": email, "note": 0, "avis": 0}
                    st.session_state.sites.append(new)
                    st.success(f"Le site '{nom}' a été enregistré avec succès !")
                    st.balloons()
                else:
                    st.error("Veuillez remplir tous les champs obligatoires (*)")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # DASHBOARD
    elif st.session_state.page == 'dashboard':
        st.markdown('<div class="page-carte">', unsafe_allow_html=True)
        st.markdown('<div class="page-titre">Tableau de Bord - Analyse des Données</div>', unsafe_allow_html=True)
        
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Sites", len(df))
        c2.metric("Régions", df['region'].nunique())
        c3.metric("Catégories", df['categorie'].nunique())
        c4.metric("Note Moyenne", f"{df['note'].mean():.2f}")
        c5.metric("Total Avis", df['avis'].sum())
        st.markdown('</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="page-carte">', unsafe_allow_html=True)
            fig = px.pie(df, names='region', title="Répartition par Région",
                        color_discrete_sequence=['#FFCC00', '#FFE066', '#D4A900', '#B8960A', '#FFF2CC'])
            fig.update_layout(paper_bgcolor='white', font=dict(family="Calibri", color="#1a1a1a"))
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        with col2:
            st.markdown('<div class="page-carte">', unsafe_allow_html=True)
            cat_counts = df['categorie'].value_counts().reset_index()
            cat_counts.columns = ['Catégorie', 'Nombre']
            fig = px.bar(cat_counts, x='Catégorie', y='Nombre', title="Sites par Catégorie",
                        color_discrete_sequence=['#FFCC00'])
            fig.update_layout(paper_bgcolor='white', font=dict(family="Calibri", color="#1a1a1a"))
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="page-carte">', unsafe_allow_html=True)
        st.markdown("**Statistiques Descriptives**")
        stats = df[['prix', 'note', 'avis']].describe()
        stats.columns = ['Prix (FCFA)', 'Note', 'Nombre Avis']
        st.dataframe(stats.round(2), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="page-carte">', unsafe_allow_html=True)
        st.markdown("**Base de Données Complète**")
        st.dataframe(df[['nom', 'region', 'ville', 'categorie', 'prix', 'note', 'avis']], 
                    use_container_width=True, hide_index=True)
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Télécharger les données (CSV)", csv, "tanap_donnees.csv", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div class="pied-page">
        <p>🇨🇲 <strong>TANAP</strong> - Guide Touristique Camerounais</p>
        <p>TP INF232 EC2 - Application de Collecte et Analyse de Données</p>
        <span class="badge-or">Matricule: 24F2551 | NDOUMA NANG SOSTHENE ASTIN</span>
    </div>
    """, unsafe_allow_html=True)
