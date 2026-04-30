import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import json
import os

# Configuration de la page
st.set_page_config(
    page_title="TANAP - Guide Touristique Camerounais",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personnalisé pour un look professionnel
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1a5f2a 0%, #2d8f4e 50%, #f4a020 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .main-header h1 {
        font-size: 3rem;
        font-weight: 700;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .main-header p {
        font-size: 1.2rem;
        margin-top: 0.5rem;
        opacity: 0.95;
    }
    
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        border-left: 5px solid #2d8f4e;
        transition: transform 0.3s ease;
    }
    
    .card:hover {
        transform: translateY(-5px);
    }
    
    .stat-card {
        background: linear-gradient(135deg, #2d8f4e, #1a5f2a);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .welcome-btn {
        background: linear-gradient(135deg, #2d8f4e, #1a5f2a);
        color: white;
        padding: 1.5rem 3rem;
        border-radius: 50px;
        font-size: 1.2rem;
        font-weight: 600;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        display: inline-block;
        text-decoration: none;
        margin: 0.5rem;
    }
    
    .welcome-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(45,143,78,0.4);
    }
    
    .site-card {
        background: white;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
        margin-bottom: 1rem;
    }
    
    .site-card:hover {
        transform: translateY(-10px);
    }
    
    .region-tag {
        background: #f4a020;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .category-tag {
        background: #2d8f4e;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    .footer {
        background: #1a1a1a;
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-top: 3rem;
    }
    
    .footer p {
        margin: 0.3rem 0;
    }
    
    .matricule {
        background: #f4a020;
        color: #1a1a1a;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        font-weight: 600;
        display: inline-block;
        margin-top: 1rem;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #2d8f4e, #1a5f2a);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 20px rgba(45,143,78,0.4);
    }
    
    .success-message {
        background: linear-gradient(135deg, #2d8f4e, #1a5f2a);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# Données initiales des sites touristiques camerounais
INITIAL_SITES = [
    {
        "id": 1,
        "nom": "Monument de la Réunification",
        "region": "Centre",
        "ville": "Yaoundé",
        "categorie": "Monument Historique",
        "description": "Symbole de l'unité nationale camerounaise, ce monument emblématique commémore la réunification du Cameroun français et britannique en 1961. Sa structure en spirale s'élève majestueusement vers le ciel.",
        "prix_entree": 1000,
        "horaires": "08h00 - 18h00",
        "contact": "+237 222 23 45 67",
        "email": "monument.reunification@tourisme.cm",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Reunification_Monument_Yaounde.jpg/800px-Reunification_Monument_Yaounde.jpg",
        "note_moyenne": 4.7,
        "nombre_avis": 1250,
        "date_ajout": "2024-01-15",
        "coordonnees": {"lat": 3.8667, "lon": 11.5167}
    },
    {
        "id": 2,
        "nom": "Chutes de la Lobé",
        "region": "Sud",
        "ville": "Kribi",
        "categorie": "Site Naturel",
        "description": "Unique en Afrique, ces chutes spectaculaires se jettent directement dans l'océan Atlantique. Un spectacle naturel époustouflant où eau douce et eau salée se rencontrent.",
        "prix_entree": 2000,
        "horaires": "07h00 - 18h00",
        "contact": "+237 699 88 77 66",
        "email": "chutes.lobe@tourisme.cm",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Lobe_Falls.jpg/800px-Lobe_Falls.jpg",
        "note_moyenne": 4.9,
        "nombre_avis": 2340,
        "date_ajout": "2024-01-20",
        "coordonnees": {"lat": 2.8833, "lon": 9.9000}
    },
    {
        "id": 3,
        "nom": "Palais des Sultans Bamoun",
        "region": "Ouest",
        "ville": "Foumban",
        "categorie": "Patrimoine Culturel",
        "description": "Résidence royale du Sultan des Bamoun, ce palais abrite un musée exceptionnel présentant l'art et l'histoire du peuple Bamoun, connu pour son écriture unique inventée par le Sultan Njoya.",
        "prix_entree": 3000,
        "horaires": "09h00 - 17h00",
        "contact": "+237 677 55 44 33",
        "email": "palais.bamoun@tourisme.cm",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Foumban_Royal_Palace.jpg/800px-Foumban_Royal_Palace.jpg",
        "note_moyenne": 4.8,
        "nombre_avis": 890,
        "date_ajout": "2024-02-01",
        "coordonnees": {"lat": 5.7272, "lon": 10.8981}
    },
    {
        "id": 4,
        "nom": "Mont Cameroun",
        "region": "Sud-Ouest",
        "ville": "Buéa",
        "categorie": "Site Naturel",
        "description": "Plus haut sommet d'Afrique de l'Ouest (4095m), ce volcan actif offre des randonnées inoubliables à travers différents écosystèmes, de la forêt tropicale aux prairies d'altitude.",
        "prix_entree": 15000,
        "horaires": "06h00 - 18h00",
        "contact": "+237 654 32 10 98",
        "email": "montcameroun@tourisme.cm",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Mount_Cameroon_crbread.jpg/800px-Mount_Cameroon_crhead.jpg",
        "note_moyenne": 4.6,
        "nombre_avis": 567,
        "date_ajout": "2024-02-10",
        "coordonnees": {"lat": 4.2033, "lon": 9.1706}
    },
    {
        "id": 5,
        "nom": "Parc National de Waza",
        "region": "Extrême-Nord",
        "ville": "Waza",
        "categorie": "Parc National",
        "description": "Le plus célèbre parc national du Cameroun, habitat naturel d'éléphants, lions, girafes et de nombreuses espèces d'oiseaux. Une expérience safari authentique en Afrique centrale.",
        "prix_entree": 10000,
        "horaires": "06h00 - 18h00",
        "contact": "+237 622 11 00 99",
        "email": "parcwaza@tourisme.cm",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Waza_elephant.jpg/800px-Waza_elephant.jpg",
        "note_moyenne": 4.5,
        "nombre_avis": 432,
        "date_ajout": "2024-02-15",
        "coordonnees": {"lat": 11.3167, "lon": 14.6667}
    },
    {
        "id": 6,
        "nom": "Lac Nyos",
        "region": "Nord-Ouest",
        "ville": "Nyos",
        "categorie": "Site Naturel",
        "description": "Lac de cratère aux eaux d'un bleu profond, ce site mémoriel rappelle la catastrophe de 1986. Aujourd'hui sécurisé, il offre un paysage volcanique unique et une leçon d'histoire naturelle.",
        "prix_entree": 5000,
        "horaires": "08h00 - 16h00",
        "contact": "+237 670 88 77 66",
        "email": "lacnyos@tourisme.cm",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/54/Lake_Nyos.jpg/800px-Lake_Nyos.jpg",
        "note_moyenne": 4.3,
        "nombre_avis": 234,
        "date_ajout": "2024-02-20",
        "coordonnees": {"lat": 6.4381, "lon": 10.2981}
    },
    {
        "id": 7,
        "nom": "Plages de Limbé",
        "region": "Sud-Ouest",
        "ville": "Limbé",
        "categorie": "Plage",
        "description": "Plages de sable volcanique noir unique, bordées de cocotiers et surplombées par le Mont Cameroun. Un cadre paradisiaque pour la détente et les sports nautiques.",
        "prix_entree": 500,
        "horaires": "Accès libre",
        "contact": "+237 677 44 33 22",
        "email": "plages.limbe@tourisme.cm",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Limbe_beach.jpg/800px-Limbe_beach.jpg",
        "note_moyenne": 4.4,
        "nombre_avis": 1876,
        "date_ajout": "2024-03-01",
        "coordonnees": {"lat": 4.0167, "lon": 9.2167}
    },
    {
        "id": 8,
        "nom": "Chefferie de Bafut",
        "region": "Nord-Ouest",
        "ville": "Bafut",
        "categorie": "Patrimoine Culturel",
        "description": "Siège du royaume Bafut, cette chefferie traditionnelle présente une architecture grassfield unique. Le musée expose des objets royaux et des masques traditionnels.",
        "prix_entree": 2500,
        "horaires": "09h00 - 17h00",
        "contact": "+237 655 66 77 88",
        "email": "chefferie.bafut@tourisme.cm",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/Bafut_Palace.jpg/800px-Bafut_Palace.jpg",
        "note_moyenne": 4.6,
        "nombre_avis": 345,
        "date_ajout": "2024-03-10",
        "coordonnees": {"lat": 6.0833, "lon": 10.1000}
    }
]

# Initialisation des données en session
def init_session_state():
    if 'sites' not in st.session_state:
        st.session_state.sites = INITIAL_SITES.copy()
    if 'page' not in st.session_state:
        st.session_state.page = 'accueil'
    if 'admin_logged' not in st.session_state:
        st.session_state.admin_logged = False

init_session_state()

# Fonctions utilitaires
def get_sites_df():
    return pd.DataFrame(st.session_state.sites)

def add_site(site_data):
    new_id = max([s['id'] for s in st.session_state.sites]) + 1 if st.session_state.sites else 1
    site_data['id'] = new_id
    site_data['date_ajout'] = datetime.now().strftime("%Y-%m-%d")
    site_data['note_moyenne'] = 0
    site_data['nombre_avis'] = 0
    st.session_state.sites.append(site_data)
    return True

# Navigation
def navigate_to(page):
    st.session_state.page = page

# ==================== PAGES ====================

def page_accueil():
    # En-tête principal
    st.markdown("""
    <div class="main-header">
        <h1>🌍 TANAP</h1>
        <p>Tourisme Authentique et Naturel en Afrique - Portail Cameroun</p>
        <p style="font-size: 0.9rem; opacity: 0.8;">Découvrez les merveilles du Cameroun, l'Afrique en miniature</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Message de bienvenue
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 15px; margin-bottom: 2rem;">
        <h2 style="color: #1a5f2a; margin-bottom: 1rem;">Bienvenue sur TANAP ! 👋</h2>
        <p style="font-size: 1.1rem; color: #555; max-width: 800px; margin: 0 auto;">
            Que vous soyez un voyageur en quête d'aventures ou un propriétaire de site touristique 
            souhaitant promouvoir votre établissement, TANAP est votre passerelle vers le tourisme camerounais.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Options de choix
    st.markdown("<h3 style='text-align: center; color: #1a5f2a; margin: 2rem 0;'>Que souhaitez-vous faire ?</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        col_a, col_b = st.columns(2)
        
        with col_a:
            st.markdown("""
            <div class="card" style="text-align: center; padding: 2rem;">
                <div style="font-size: 4rem;">🔍</div>
                <h3 style="color: #1a5f2a;">Je cherche un site</h3>
                <p style="color: #666;">Explorez les merveilles touristiques du Cameroun</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Explorer les sites 🗺️", key="btn_explorer", use_container_width=True):
                navigate_to('explorer')
                st.rerun()
        
        with col_b:
            st.markdown("""
            <div class="card" style="text-align: center; padding: 2rem;">
                <div style="font-size: 4rem;">📝</div>
                <h3 style="color: #1a5f2a;">J'enregistre un site</h3>
                <p style="color: #666;">Référencez votre site touristique sur notre plateforme</p>
            </div>
            """, unsafe_allow_html=True)
            if st.button("Enregistrer mon site ➕", key="btn_enregistrer", use_container_width=True):
                navigate_to('enregistrer')
                st.rerun()
    
    # Statistiques rapides
    st.markdown("<br>", unsafe_allow_html=True)
    df = get_sites_df()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{len(df)}</div>
            <div>Sites référencés</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{df['region'].nunique()}</div>
            <div>Régions couvertes</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{df['categorie'].nunique()}</div>
            <div>Catégories</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        total_avis = df['nombre_avis'].sum()
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{total_avis:,}</div>
            <div>Avis collectés</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Aperçu des sites populaires
    st.markdown("<h3 style='color: #1a5f2a; margin: 2rem 0;'>🌟 Sites les plus populaires</h3>", unsafe_allow_html=True)
    
    top_sites = df.nlargest(4, 'nombre_avis')
    
    cols = st.columns(4)
    for idx, (_, site) in enumerate(top_sites.iterrows()):
        with cols[idx]:
            st.markdown(f"""
            <div class="site-card">
                <div style="height: 150px; background: linear-gradient(135deg, #2d8f4e, #1a5f2a); display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 3rem;">🏛️</span>
                </div>
                <div style="padding: 1rem;">
                    <h4 style="margin: 0; color: #1a5f2a;">{site['nom'][:20]}...</h4>
                    <p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0;">{site['ville']}</p>
                    <span class="region-tag">{site['region']}</span>
                    <div style="margin-top: 0.5rem;">
                        <span style="color: #f4a020;">★</span> {site['note_moyenne']} ({site['nombre_avis']} avis)
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

def page_explorer():
    st.markdown("""
    <div class="main-header">
        <h1>🗺️ Explorer les Sites</h1>
        <p>Découvrez les trésors touristiques du Cameroun</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bouton retour
    if st.button("← Retour à l'accueil"):
        navigate_to('accueil')
        st.rerun()
    
    df = get_sites_df()
    
    # Filtres
    st.markdown("### 🔍 Filtrer les sites")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        regions = ['Toutes'] + list(df['region'].unique())
        region_filter = st.selectbox("Région", regions)
    
    with col2:
        categories = ['Toutes'] + list(df['categorie'].unique())
        categorie_filter = st.selectbox("Catégorie", categories)
    
    with col3:
        prix_max = st.slider("Prix d'entrée max (FCFA)", 0, 20000, 20000, step=500)
    
    # Appliquer les filtres
    filtered_df = df.copy()
    
    if region_filter != 'Toutes':
        filtered_df = filtered_df[filtered_df['region'] == region_filter]
    
    if categorie_filter != 'Toutes':
        filtered_df = filtered_df[filtered_df['categorie'] == categorie_filter]
    
    filtered_df = filtered_df[filtered_df['prix_entree'] <= prix_max]
    
    # Tri
    sort_option = st.selectbox("Trier par", ["Note (décroissant)", "Nombre d'avis", "Prix (croissant)", "Prix (décroissant)"])
    
    if sort_option == "Note (décroissant)":
        filtered_df = filtered_df.sort_values('note_moyenne', ascending=False)
    elif sort_option == "Nombre d'avis":
        filtered_df = filtered_df.sort_values('nombre_avis', ascending=False)
    elif sort_option == "Prix (croissant)":
        filtered_df = filtered_df.sort_values('prix_entree', ascending=True)
    else:
        filtered_df = filtered_df.sort_values('prix_entree', ascending=False)
    
    st.markdown(f"### 📍 {len(filtered_df)} site(s) trouvé(s)")
    
    # Affichage des sites
    for _, site in filtered_df.iterrows():
        with st.expander(f"🏛️ {site['nom']} - {site['ville']} ({site['region']})"):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, #2d8f4e, #1a5f2a); height: 200px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                    <span style="font-size: 5rem;">🏛️</span>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div>
                    <span class="category-tag">{site['categorie']}</span>
                    <span class="region-tag" style="margin-left: 0.5rem;">{site['region']}</span>
                    <h3 style="color: #1a5f2a; margin: 1rem 0 0.5rem 0;">{site['nom']}</h3>
                    <p style="color: #666;">{site['description']}</p>
                    <div style="display: flex; gap: 2rem; margin-top: 1rem;">
                        <div>
                            <strong>💰 Prix:</strong> {site['prix_entree']:,} FCFA
                        </div>
                        <div>
                            <strong>🕐 Horaires:</strong> {site['horaires']}
                        </div>
                    </div>
                    <div style="margin-top: 0.5rem;">
                        <strong>📞 Contact:</strong> {site['contact']}
                    </div>
                    <div style="margin-top: 0.5rem;">
                        <strong>📧 Email:</strong> {site['email']}
                    </div>
                    <div style="margin-top: 1rem; padding: 0.5rem; background: #fff3cd; border-radius: 5px;">
                        <span style="color: #f4a020; font-size: 1.5rem;">★</span>
                        <strong>{site['note_moyenne']}/5</strong> 
                        <span style="color: #666;">({site['nombre_avis']} avis)</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)

def page_enregistrer():
    st.markdown("""
    <div class="main-header">
        <h1>📝 Enregistrer un Site</h1>
        <p>Référencez votre site touristique sur TANAP</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Bouton retour
    if st.button("← Retour à l'accueil"):
        navigate_to('accueil')
        st.rerun()
    
    st.markdown("""
    <div class="card">
        <h3 style="color: #1a5f2a;">📋 Formulaire d'enregistrement</h3>
        <p style="color: #666;">Remplissez ce formulaire pour ajouter votre site touristique à notre plateforme.</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("form_site"):
        col1, col2 = st.columns(2)
        
        with col1:
            nom = st.text_input("Nom du site *", placeholder="Ex: Chutes de la Mefou")
            region = st.selectbox("Région *", [
                "Centre", "Littoral", "Ouest", "Nord-Ouest", "Sud-Ouest",
                "Sud", "Est", "Adamaoua", "Nord", "Extrême-Nord"
            ])
            ville = st.text_input("Ville *", placeholder="Ex: Yaoundé")
            categorie = st.selectbox("Catégorie *", [
                "Site Naturel", "Monument Historique", "Patrimoine Culturel",
                "Parc National", "Plage", "Musée", "Réserve Naturelle", "Autre"
            ])
        
        with col2:
            prix_entree = st.number_input("Prix d'entrée (FCFA) *", min_value=0, step=500)
            horaires = st.text_input("Horaires d'ouverture *", placeholder="Ex: 08h00 - 18h00")
            contact = st.text_input("Numéro de téléphone *", placeholder="Ex: +237 6XX XX XX XX")
            email = st.text_input("Email *", placeholder="Ex: contact@monsite.cm")
        
        description = st.text_area(
            "Description du site *", 
            placeholder="Décrivez votre site touristique en détail (attractions, activités, histoire...)",
            height=150
        )
        
        image_url = st.text_input(
            "URL de l'image (optionnel)", 
            placeholder="https://exemple.com/image.jpg"
        )
        
        # Coordonnées GPS (optionnel)
        st.markdown("#### 📍 Localisation GPS (optionnel)")
        col1, col2 = st.columns(2)
        with col1:
            latitude = st.number_input("Latitude", value=0.0, format="%.4f")
        with col2:
            longitude = st.number_input("Longitude", value=0.0, format="%.4f")
        
        st.markdown("---")
        
        # Informations du propriétaire
        st.markdown("#### 👤 Informations du propriétaire")
        col1, col2 = st.columns(2)
        with col1:
            nom_proprietaire = st.text_input("Nom complet *")
        with col2:
            telephone_proprietaire = st.text_input("Téléphone personnel")
        
        submitted = st.form_submit_button("✅ Enregistrer le site", use_container_width=True)
        
        if submitted:
            if all([nom, region, ville, categorie, prix_entree >= 0, horaires, contact, email, description, nom_proprietaire]):
                site_data = {
                    "nom": nom,
                    "region": region,
                    "ville": ville,
                    "categorie": categorie,
                    "prix_entree": prix_entree,
                    "horaires": horaires,
                    "contact": contact,
                    "email": email,
                    "description": description,
                    "image_url": image_url if image_url else "",
                    "coordonnees": {"lat": latitude, "lon": longitude},
                    "proprietaire": nom_proprietaire,
                    "tel_proprietaire": telephone_proprietaire
                }
                
                if add_site(site_data):
                    st.markdown("""
                    <div class="success-message">
                        ✅ Félicitations ! Votre site a été enregistré avec succès !<br>
                        Il est maintenant visible par tous les visiteurs de TANAP.
                    </div>
                    """, unsafe_allow_html=True)
                    st.balloons()
            else:
                st.error("⚠️ Veuillez remplir tous les champs obligatoires (*)")

def page_admin():
    st.markdown("""
    <div class="main-header">
        <h1>📊 Dashboard Administrateur</h1>
        <p>Analyse descriptive des données touristiques</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Authentification simple
    if not st.session_state.admin_logged:
        st.markdown("""
        <div class="card" style="max-width: 400px; margin: 2rem auto;">
            <h3 style="color: #1a5f2a; text-align: center;">🔐 Connexion Admin</h3>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            password = st.text_input("Mot de passe", type="password")
            if st.button("Se connecter", use_container_width=True):
                if password == "tanap2024":
                    st.session_state.admin_logged = True
                    st.rerun()
                else:
                    st.error("Mot de passe incorrect")
            st.info("💡 Mot de passe: tanap2024")
        return
    
    # Bouton déconnexion
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("🚪 Déconnexion"):
            st.session_state.admin_logged = False
            st.rerun()
    
    with col1:
        if st.button("← Retour à l'accueil"):
            navigate_to('accueil')
            st.rerun()
    
    df = get_sites_df()
    
    # KPIs principaux
    st.markdown("### 📈 Indicateurs Clés de Performance")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total Sites", len(df))
    
    with col2:
        st.metric("Régions Couvertes", df['region'].nunique())
    
    with col3:
        st.metric("Note Moyenne", f"{df['note_moyenne'].mean():.2f}/5")
    
    with col4:
        st.metric("Total Avis", f"{df['nombre_avis'].sum():,}")
    
    with col5:
        st.metric("Prix Moyen", f"{df['prix_entree'].mean():,.0f} FCFA")
    
    st.markdown("---")
    
    # Graphiques d'analyse
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🗺️ Distribution par Région")
        region_counts = df['region'].value_counts()
        fig = px.pie(
            values=region_counts.values, 
            names=region_counts.index,
            color_discrete_sequence=px.colors.sequential.Greens_r
        )
        fig.update_layout(height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 📂 Distribution par Catégorie")
        cat_counts = df['categorie'].value_counts()
        fig = px.bar(
            x=cat_counts.index, 
            y=cat_counts.values,
            color=cat_counts.values,
            color_continuous_scale='Greens'
        )
        fig.update_layout(height=350, showlegend=False, xaxis_title="", yaxis_title="Nombre de sites")
        st.plotly_chart(fig, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### ⭐ Top 10 Sites par Note")
        top_notes = df.nlargest(10, 'note_moyenne')[['nom', 'note_moyenne', 'region']]
        fig = px.bar(
            top_notes, 
            x='note_moyenne', 
            y='nom',
            orientation='h',
            color='note_moyenne',
            color_continuous_scale='YlGn'
        )
        fig.update_layout(height=400, yaxis={'categoryorder':'total ascending'}, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### 💬 Top 10 Sites par Nombre d'Avis")
        top_avis = df.nlargest(10, 'nombre_avis')[['nom', 'nombre_avis', 'region']]
        fig = px.bar(
            top_avis, 
            x='nombre_avis', 
            y='nom',
            orientation='h',
            color='nombre_avis',
            color_continuous_scale='Oranges'
        )
        fig.update_layout(height=400, yaxis={'categoryorder':'total ascending'}, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Analyse des prix
    st.markdown("### 💰 Analyse des Prix d'Entrée")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Distribution des Prix")
        fig = px.histogram(
            df, 
            x='prix_entree', 
            nbins=20,
            color_discrete_sequence=['#2d8f4e']
        )
        fig.update_layout(xaxis_title="Prix (FCFA)", yaxis_title="Nombre de sites")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("#### Prix Moyen par Catégorie")
        prix_cat = df.groupby('categorie')['prix_entree'].mean().sort_values(ascending=True)
        fig = px.bar(
            x=prix_cat.values, 
            y=prix_cat.index,
            orientation='h',
            color=prix_cat.values,
            color_continuous_scale='Greens'
        )
        fig.update_layout(showlegend=False, xaxis_title="Prix moyen (FCFA)", yaxis_title="")
        st.plotly_chart(fig, use_container_width=True)
    
    # Statistiques descriptives détaillées
    st.markdown("### 📊 Statistiques Descriptives Complètes")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Variables Numériques")
        stats = df[['prix_entree', 'note_moyenne', 'nombre_avis']].describe()
        stats.index = ['Nombre', 'Moyenne', 'Écart-type', 'Minimum', '25%', '50% (Médiane)', '75%', 'Maximum']
        stats.columns = ['Prix (FCFA)', 'Note', 'Nombre Avis']
        st.dataframe(stats.round(2), use_container_width=True)
    
    with col2:
        st.markdown("#### Variables Catégorielles")
        cat_stats = pd.DataFrame({
            'Variable': ['Régions', 'Catégories', 'Villes'],
            'Nombre Unique': [df['region'].nunique(), df['categorie'].nunique(), df['ville'].nunique()],
            'Mode (Plus Fréquent)': [df['region'].mode()[0], df['categorie'].mode()[0], df['ville'].mode()[0]],
            'Fréquence Mode': [
                df['region'].value_counts().iloc[0],
                df['categorie'].value_counts().iloc[0],
                df['ville'].value_counts().iloc[0]
            ]
        })
        st.dataframe(cat_stats, use_container_width=True, hide_index=True)
    
    # Corrélations
    st.markdown("#### 🔗 Matrice de Corrélation")
    corr_data = df[['prix_entree', 'note_moyenne', 'nombre_avis']].corr()
    fig = px.imshow(
        corr_data,
        text_auto=True,
        color_continuous_scale='Greens',
        labels=dict(x="Variable", y="Variable", color="Corrélation")
    )
    fig.update_layout(height=350)
    st.plotly_chart(fig, use_container_width=True)
    
    # Tableau complet des données
    st.markdown("### 📋 Base de Données Complète")
    st.dataframe(
        df[['nom', 'region', 'ville', 'categorie', 'prix_entree', 'note_moyenne', 'nombre_avis', 'date_ajout']],
        use_container_width=True,
        hide_index=True
    )
    
    # Export des données
    st.markdown("### 📥 Exporter les Données")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Télécharger CSV",
            data=csv,
            file_name="tanap_sites_touristiques.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col2:
        json_data = df.to_json(orient='records', force_ascii=False)
        st.download_button(
            label="📥 Télécharger JSON",
            data=json_data,
            file_name="tanap_sites_touristiques.json",
            mime="application/json",
            use_container_width=True
        )

def footer():
    st.markdown("""
    <div class="footer">
        <h3>🌍 TANAP - Tourisme Authentique et Naturel en Afrique</h3>
        <p>Guide Touristique Camerounais Interactif</p>
        <p>Application de Collecte et Analyse Descriptive des Données</p>
        <hr style="border-color: #333; margin: 1rem 0;">
        <p><strong>TP INF232 EC2</strong></p>
        <div class="matricule">
            Matricule: 24F2551 | NDOUMA NANG SOSTHENE ASTIN
        </div>
        <p style="margin-top: 1rem; font-size: 0.8rem; opacity: 0.7;">
            © 2024 TANAP - Tous droits réservés
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==================== MAIN ====================

def main():
    # Sidebar navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 1rem;">
            <h2 style="color: #2d8f4e;">🌍 TANAP</h2>
            <p style="font-size: 0.9rem; color: #666;">Navigation</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🏠 Accueil", use_container_width=True):
            navigate_to('accueil')
            st.rerun()
        
        if st.button("🔍 Explorer les Sites", use_container_width=True):
            navigate_to('explorer')
            st.rerun()
        
        if st.button("📝 Enregistrer un Site", use_container_width=True):
            navigate_to('enregistrer')
            st.rerun()
        
        if st.button("📊 Dashboard Admin", use_container_width=True):
            navigate_to('admin')
            st.rerun()
        
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: #f0f0f0; border-radius: 10px;">
            <p style="font-size: 0.8rem; color: #666; margin: 0;">
                <strong>Matricule:</strong> 24F2551<br>
                <strong>NDOUMA NANG<br>SOSTHENE ASTIN</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    # Router
    if st.session_state.page == 'accueil':
        page_accueil()
    elif st.session_state.page == 'explorer':
        page_explorer()
    elif st.session_state.page == 'enregistrer':
        page_enregistrer()
    elif st.session_state.page == 'admin':
        page_admin()
    
    # Footer
    footer()

if __name__ == "__main__":
    main()
