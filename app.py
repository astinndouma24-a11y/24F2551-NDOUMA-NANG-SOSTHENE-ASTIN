import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Configuration
st.set_page_config(
    page_title="TANAP - Guide Touristique Camerounais",
    page_icon="🌍",
    layout="wide"
)

# CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1a5f2a 0%, #2d8f4e 50%, #f4a020 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .stat-card {
        background: linear-gradient(135deg, #2d8f4e, #1a5f2a);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
    }
    .footer {
        background: #1a1a1a;
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 3rem;
    }
    .matricule {
        background: #f4a020;
        color: #1a1a1a;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Données initiales
INITIAL_SITES = [
    {"id": 1, "nom": "Monument de la Réunification", "region": "Centre", "ville": "Yaoundé", 
     "categorie": "Monument Historique", "description": "Symbole de l'unité nationale camerounaise.", 
     "prix_entree": 1000, "horaires": "08h00 - 18h00", "contact": "+237 222 23 45 67",
     "email": "monument@tourisme.cm", "note_moyenne": 4.7, "nombre_avis": 1250, "date_ajout": "2024-01-15"},
    {"id": 2, "nom": "Chutes de la Lobé", "region": "Sud", "ville": "Kribi",
     "categorie": "Site Naturel", "description": "Chutes spectaculaires se jetant dans l'océan.",
     "prix_entree": 2000, "horaires": "07h00 - 18h00", "contact": "+237 699 88 77 66",
     "email": "lobe@tourisme.cm", "note_moyenne": 4.9, "nombre_avis": 2340, "date_ajout": "2024-01-20"},
    {"id": 3, "nom": "Palais des Sultans Bamoun", "region": "Ouest", "ville": "Foumban",
     "categorie": "Patrimoine Culturel", "description": "Résidence royale du Sultan des Bamoun.",
     "prix_entree": 3000, "horaires": "09h00 - 17h00", "contact": "+237 677 55 44 33",
     "email": "bamoun@tourisme.cm", "note_moyenne": 4.8, "nombre_avis": 890, "date_ajout": "2024-02-01"},
    {"id": 4, "nom": "Mont Cameroun", "region": "Sud-Ouest", "ville": "Buéa",
     "categorie": "Site Naturel", "description": "Plus haut sommet d'Afrique de l'Ouest (4095m).",
     "prix_entree": 15000, "horaires": "06h00 - 18h00", "contact": "+237 654 32 10 98",
     "email": "mont@tourisme.cm", "note_moyenne": 4.6, "nombre_avis": 567, "date_ajout": "2024-02-10"},
    {"id": 5, "nom": "Parc National de Waza", "region": "Extrême-Nord", "ville": "Waza",
     "categorie": "Parc National", "description": "Safari authentique avec éléphants et lions.",
     "prix_entree": 10000, "horaires": "06h00 - 18h00", "contact": "+237 622 11 00 99",
     "email": "waza@tourisme.cm", "note_moyenne": 4.5, "nombre_avis": 432, "date_ajout": "2024-02-15"},
    {"id": 6, "nom": "Plages de Limbé", "region": "Sud-Ouest", "ville": "Limbé",
     "categorie": "Plage", "description": "Plages de sable volcanique noir unique.",
     "prix_entree": 500, "horaires": "Accès libre", "contact": "+237 677 44 33 22",
     "email": "limbe@tourisme.cm", "note_moyenne": 4.4, "nombre_avis": 1876, "date_ajout": "2024-03-01"},
]

# Session state
if 'sites' not in st.session_state:
    st.session_state.sites = INITIAL_SITES.copy()
if 'page' not in st.session_state:
    st.session_state.page = 'accueil'

def get_df():
    return pd.DataFrame(st.session_state.sites)

# Sidebar
st.sidebar.markdown("## 🌍 TANAP")
st.sidebar.markdown("Navigation")

if st.sidebar.button("🏠 Accueil", use_container_width=True):
    st.session_state.page = 'accueil'
if st.sidebar.button("🔍 Explorer", use_container_width=True):
    st.session_state.page = 'explorer'
if st.sidebar.button("📝 Enregistrer", use_container_width=True):
    st.session_state.page = 'enregistrer'
if st.sidebar.button("📊 Dashboard", use_container_width=True):
    st.session_state.page = 'admin'

st.sidebar.markdown("---")
st.sidebar.markdown("**Matricule:** 24F2551")
st.sidebar.markdown("**NDOUMA NANG SOSTHENE ASTIN**")

# Pages
if st.session_state.page == 'accueil':
    st.markdown('<div class="main-header"><h1>🌍 TANAP</h1><p>Tourisme Authentique et Naturel en Afrique - Cameroun</p></div>', unsafe_allow_html=True)
    
    st.markdown("## Bienvenue ! 👋")
    st.write("Que vous soyez voyageur ou propriétaire de site, TANAP est votre guide touristique camerounais.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🔍 Je cherche un site")
        if st.button("Explorer les sites", use_container_width=True):
            st.session_state.page = 'explorer'
            st.rerun()
    with col2:
        st.markdown("### 📝 J'enregistre un site")
        if st.button("Enregistrer mon site", use_container_width=True):
            st.session_state.page = 'enregistrer'
            st.rerun()
    
    df = get_df()
    st.markdown("### 📊 Statistiques")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Sites", len(df))
    c2.metric("Régions", df['region'].nunique())
    c3.metric("Catégories", df['categorie'].nunique())
    c4.metric("Avis", df['nombre_avis'].sum())

elif st.session_state.page == 'explorer':
    st.markdown('<div class="main-header"><h1>🗺️ Explorer les Sites</h1></div>', unsafe_allow_html=True)
    
    df = get_df()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        region = st.selectbox("Région", ['Toutes'] + list(df['region'].unique()))
    with col2:
        categorie = st.selectbox("Catégorie", ['Toutes'] + list(df['categorie'].unique()))
    with col3:
        prix_max = st.slider("Prix max (FCFA)", 0, 20000, 20000)
    
    filtered = df.copy()
    if region != 'Toutes':
        filtered = filtered[filtered['region'] == region]
    if categorie != 'Toutes':
        filtered = filtered[filtered['categorie'] == categorie]
    filtered = filtered[filtered['prix_entree'] <= prix_max]
    
    st.markdown(f"### 📍 {len(filtered)} site(s)")
    
    for _, site in filtered.iterrows():
        with st.expander(f"🏛️ {site['nom']} - {site['ville']}"):
            st.write(f"**Région:** {site['region']} | **Catégorie:** {site['categorie']}")
            st.write(site['description'])
            st.write(f"💰 **Prix:** {site['prix_entree']:,} FCFA | ⭐ **Note:** {site['note_moyenne']}/5 ({site['nombre_avis']} avis)")
            st.write(f"🕐 {site['horaires']} | 📞 {site['contact']}")

elif st.session_state.page == 'enregistrer':
    st.markdown('<div class="main-header"><h1>📝 Enregistrer un Site</h1></div>', unsafe_allow_html=True)
    
    with st.form("site_form"):
        col1, col2 = st.columns(2)
        with col1:
            nom = st.text_input("Nom du site *")
            region = st.selectbox("Région *", ["Centre", "Littoral", "Ouest", "Nord-Ouest", "Sud-Ouest", "Sud", "Est", "Adamaoua", "Nord", "Extrême-Nord"])
            ville = st.text_input("Ville *")
            categorie = st.selectbox("Catégorie *", ["Site Naturel", "Monument Historique", "Patrimoine Culturel", "Parc National", "Plage", "Musée"])
        with col2:
            prix = st.number_input("Prix (FCFA)", min_value=0, step=500)
            horaires = st.text_input("Horaires *")
            contact = st.text_input("Téléphone *")
            email = st.text_input("Email *")
        
        description = st.text_area("Description *")
        proprietaire = st.text_input("Votre nom *")
        
        if st.form_submit_button("✅ Enregistrer", use_container_width=True):
            if all([nom, ville, horaires, contact, email, description, proprietaire]):
                new_site = {
                    "id": len(st.session_state.sites) + 1,
                    "nom": nom, "region": region, "ville": ville, "categorie": categorie,
                    "description": description, "prix_entree": prix, "horaires": horaires,
                    "contact": contact, "email": email, "note_moyenne": 0, "nombre_avis": 0,
                    "date_ajout": datetime.now().strftime("%Y-%m-%d")
                }
                st.session_state.sites.append(new_site)
                st.success("✅ Site enregistré avec succès!")
                st.balloons()
            else:
                st.error("Remplissez tous les champs obligatoires")

elif st.session_state.page == 'admin':
    st.markdown('<div class="main-header"><h1>📊 Dashboard Admin</h1></div>', unsafe_allow_html=True)
    
    password = st.text_input("Mot de passe", type="password")
    
    if password == "tanap2024":
        df = get_df()
        
        # KPIs
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("Sites", len(df))
        c2.metric("Régions", df['region'].nunique())
        c3.metric("Note moy.", f"{df['note_moyenne'].mean():.2f}")
        c4.metric("Total avis", df['nombre_avis'].sum())
        c5.metric("Prix moy.", f"{df['prix_entree'].mean():,.0f}")
        
        # Graphiques
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Distribution par Région")
            fig = px.pie(df, names='region', title="")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.markdown("### Distribution par Catégorie")
            fig = px.bar(df['categorie'].value_counts(), title="")
            st.plotly_chart(fig, use_container_width=True)
        
        # Stats descriptives
        st.markdown("### Statistiques Descriptives")
        st.dataframe(df[['prix_entree', 'note_moyenne', 'nombre_avis']].describe())
        
        # Tableau
        st.markdown("### Données Complètes")
        st.dataframe(df[['nom', 'region', 'ville', 'categorie', 'prix_entree', 'note_moyenne', 'nombre_avis']])
        
        # Export
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Télécharger CSV", csv, "tanap_data.csv", "text/csv")
    
    elif password:
        st.error("Mot de passe incorrect")
    else:
        st.info("💡 Mot de passe: tanap2024")

# Footer
st.markdown("""
<div class="footer">
    <h3>🌍 TANAP</h3>
    <p>TP INF232 EC2 - Application de Collecte et Analyse de Données</p>
    <span class="matricule">Matricule: 24F2551 | NDOUMA NANG SOSTHENE ASTIN</span>
</div>
""", unsafe_allow_html=True)
