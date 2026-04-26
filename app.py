import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, timedelta
import json
import os

STUDENT_INFO = {
    "matricule": "24F2551",
    "nom": "NDOUMA NANG SOSTHENE ASTIN"
}

DATA_FILE = "planning_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return get_default_data()

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)

def get_default_data():
    today = date.today()
    lundi = today - timedelta(days=today.weekday())

    taches = [
        {"id": 1, "titre": "Réunion de direction mensuelle", "responsable": "Dr. MBARGA Paul", "date_debut": str(lundi), "date_fin": str(lundi + timedelta(days=0)), "heure_debut": "09:00", "heure_fin": "11:00", "statut": "Terminé", "priorite": "Haute", "categorie": "Réunion", "salle": "Salle A", "description": "Bilan mensuel et objectifs"},
        {"id": 2, "titre": "Formation Excel avancé", "responsable": "NKOMO Sylvie", "date_debut": str(lundi + timedelta(days=1)), "date_fin": str(lundi + timedelta(days=1)), "heure_debut": "14:00", "heure_fin": "17:00", "statut": "En cours", "priorite": "Moyenne", "categorie": "Formation", "salle": "Salle Informatique", "description": "Formation du personnel administratif"},
        {"id": 3, "titre": "Audit des dossiers RH", "responsable": "ATEBA Christine", "date_debut": str(lundi + timedelta(days=2)), "date_fin": str(lundi + timedelta(days=4)), "heure_debut": "08:00", "heure_fin": "12:00", "statut": "En cours", "priorite": "Haute", "categorie": "Audit", "salle": "Bureau RH", "description": "Contrôle annuel des dossiers"},
        {"id": 4, "titre": "Accueil délégation ministérielle", "responsable": "FOUDA Jean-Baptiste", "date_debut": str(lundi + timedelta(days=3)), "date_fin": str(lundi + timedelta(days=3)), "heure_debut": "10:00", "heure_fin": "13:00", "statut": "Planifié", "priorite": "Très haute", "categorie": "Événement", "salle": "Salle de conférence", "description": "Visite officielle"},
        {"id": 5, "titre": "Rédaction rapport semestriel", "responsable": "BIYA Martine", "date_debut": str(lundi + timedelta(days=1)), "date_fin": str(lundi + timedelta(days=5)), "heure_debut": "08:00", "heure_fin": "12:00", "statut": "En cours", "priorite": "Haute", "categorie": "Rédaction", "salle": "Bureaux", "description": "Rapport d'activités semestriel"},
        {"id": 6, "titre": "Maintenance système informatique", "responsable": "TCHUENTE Boris", "date_debut": str(lundi + timedelta(days=5)), "date_fin": str(lundi + timedelta(days=5)), "heure_debut": "07:00", "heure_fin": "09:00", "statut": "Planifié", "priorite": "Moyenne", "categorie": "Maintenance", "salle": "Salle serveurs", "description": "Mise à jour et maintenance préventive"},
        {"id": 7, "titre": "Séance de concertation budgétaire", "responsable": "ESSAMA Roger", "date_debut": str(lundi + timedelta(days=4)), "date_fin": str(lundi + timedelta(days=4)), "heure_debut": "15:00", "heure_fin": "17:30", "statut": "Planifié", "priorite": "Très haute", "categorie": "Réunion", "salle": "Salle B", "description": "Préparation budget N+1"},
        {"id": 8, "titre": "Archivage documents administratifs", "responsable": "NGONO Elise", "date_debut": str(lundi - timedelta(days=7)), "date_fin": str(lundi - timedelta(days=5)), "heure_debut": "13:00", "heure_fin": "17:00", "statut": "Terminé", "priorite": "Basse", "categorie": "Administration", "salle": "Archives", "description": "Classement trimestriel"},
        {"id": 9, "titre": "Webinaire sur la e-gouvernance", "responsable": "NKOA Daniel", "date_debut": str(lundi + timedelta(days=2)), "date_fin": str(lundi + timedelta(days=2)), "heure_debut": "09:00", "heure_fin": "12:00", "statut": "Planifié", "priorite": "Moyenne", "categorie": "Formation", "salle": "En ligne", "description": "Formation numérique"},
        {"id": 10, "titre": "Évaluation annuelle du personnel", "responsable": "Dr. MBARGA Paul", "date_debut": str(lundi + timedelta(days=7)), "date_fin": str(lundi + timedelta(days=11)), "heure_debut": "08:30", "heure_fin": "11:30", "statut": "Planifié", "priorite": "Haute", "categorie": "RH", "salle": "Bureau direction", "description": "Entretiens annuels"},
    ]

    absences = [
        {"id": 1, "agent": "NKOMO Sylvie", "type": "Congé annuel", "date_debut": str(lundi - timedelta(days=14)), "date_fin": str(lundi - timedelta(days=8)), "statut": "Approuvé", "motif": "Vacances familiales"},
        {"id": 2, "agent": "FOUDA Jean-Baptiste", "type": "Maladie", "date_debut": str(lundi - timedelta(days=3)), "date_fin": str(lundi - timedelta(days=1)), "statut": "Approuvé", "motif": "Certificat médical"},
        {"id": 3, "agent": "BIYA Martine", "type": "Formation externe", "date_debut": str(lundi + timedelta(days=14)), "date_fin": str(lundi + timedelta(days=18)), "statut": "En attente", "motif": "Séminaire national"},
        {"id": 4, "agent": "NGONO Elise", "type": "Congé maternité", "date_debut": str(lundi + timedelta(days=21)), "date_fin": str(lundi + timedelta(days=105)), "statut": "Approuvé", "motif": "Naissance"},
        {"id": 5, "agent": "TCHUENTE Boris", "type": "Récupération", "date_debut": str(lundi + timedelta(days=6)), "date_fin": str(lundi + timedelta(days=7)), "statut": "Approuvé", "motif": "Heures supplémentaires"},
    ]

    ressources = [
        {"id": 1, "nom": "Salle de conférence", "type": "Salle", "capacite": 50, "equipements": "Vidéoprojecteur, Climatisation, Micro"},
        {"id": 2, "nom": "Salle A", "type": "Salle", "capacite": 20, "equipements": "Tableau blanc, TV 65 pouces"},
        {"id": 3, "nom": "Salle B", "type": "Salle", "capacite": 15, "equipements": "Tableau blanc, Projecteur"},
        {"id": 4, "nom": "Salle Informatique", "type": "Salle", "capacite": 25, "equipements": "Ordinateurs x25, Projecteur"},
        {"id": 5, "nom": "Véhicule de service 1", "type": "Véhicule", "capacite": 5, "equipements": "Toyota Hilux - BL 123 CM"},
        {"id": 6, "nom": "Véhicule de service 2", "type": "Véhicule", "capacite": 8, "equipements": "Minibus Toyota - BL 456 CM"},
    ]

    return {"taches": taches, "absences": absences, "ressources": ressources}

def df_taches(data):
    df = pd.DataFrame(data["taches"])
    df["date_debut"] = pd.to_datetime(df["date_debut"])
    df["date_fin"] = pd.to_datetime(df["date_fin"])
    return df

def df_absences(data):
    df = pd.DataFrame(data["absences"])
    df["date_debut"] = pd.to_datetime(df["date_debut"])
    df["date_fin"] = pd.to_datetime(df["date_fin"])
    return df

def page_accueil(data):
    st.markdown("""
    <div style='background: linear-gradient(135deg, #1E3A5F 0%, #2980B9 100%);
                padding: 2rem; border-radius: 12px; margin-bottom: 2rem;'>
        <h1 style='color: white; margin: 0; font-size: 2.2rem; font-weight: 800;'>
            🏛️ PlanAdmin Pro
        </h1>
        <p style='color: #BDE3FF; margin: 0.5rem 0 0 0; font-size: 1.1rem;'>
            Système de Gestion de Planning Bureau Administratif
        </p>
    </div>
    """, unsafe_allow_html=True)

    df = df_taches(data)
    df_abs = df_absences(data)
    today = pd.Timestamp(date.today())

    total = len(df)
    termines = len(df[df["statut"] == "Terminé"])
    en_cours = len(df[df["statut"] == "En cours"])
    planifies = len(df[df["statut"] == "Planifié"])
    absences_actives = len(df_abs[(df_abs["date_debut"] <= today) & (df_abs["date_fin"] >= today)])

    col1, col2, col3, col4, col5 = st.columns(5)
    metrics = [
        (col1, "📋 Total Activités", total, "planifiées"),
        (col2, "✅ Terminées", termines, f"{round(termines/total*100 if total else 0)}%"),
        (col3, "⚡ En cours", en_cours, "actives"),
        (col4, "📅 Planifiées", planifies, "à venir"),
        (col5, "🏖️ Absences", absences_actives, "aujourd'hui"),
    ]
    for col, label, val, delta in metrics:
        col.metric(label, val, delta)

    st.markdown("---")
    col_g, col_d = st.columns(2)

    with col_g:
        st.subheader("📊 Répartition par Statut")
        statut_counts = df["statut"].value_counts().reset_index()
        statut_counts.columns = ["Statut", "Nombre"]
        couleurs = {"Terminé": "#27AE60", "En cours": "#F39C12", "Planifié": "#2980B9", "Annulé": "#E74C3C"}
        fig = px.pie(statut_counts, values="Nombre", names="Statut",
                     color="Statut", color_discrete_map=couleurs, hole=0.4)
        fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=300)
        st.plotly_chart(fig, use_container_width=True)

    with col_d:
        st.subheader("🗂️ Activités par Catégorie")
        cat_counts = df["categorie"].value_counts().reset_index()
        cat_counts.columns = ["Catégorie", "Nombre"]
        fig2 = px.bar(cat_counts, x="Catégorie", y="Nombre",
                      color="Catégorie", color_discrete_sequence=px.colors.qualitative.Set2)
        fig2.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=300,
                           showlegend=False, xaxis_title="", yaxis_title="Nb")
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📅 Activités de la Semaine")
    lundi = today - timedelta(days=today.weekday())
    dimanche = lundi + timedelta(days=6)
    semaine = df[(df["date_debut"] >= lundi) & (df["date_debut"] <= dimanche)]

    if semaine.empty:
        st.info("Aucune activité planifiée cette semaine.")
    else:
        for _, row in semaine.iterrows():
            couleur_priorite = {"Très haute": "🔴", "Haute": "🟠", "Moyenne": "🟡", "Basse": "🟢"}.get(row["priorite"], "⚪")
            with st.container():
                st.markdown(f"""
                <div style='border-left: 4px solid #2980B9; padding: 0.5rem 1rem;
                            background: white; border-radius: 0 8px 8px 0; margin-bottom: 0.5rem;
                            box-shadow: 0 1px 3px rgba(0,0,0,0.1);'>
                    <strong>{couleur_priorite} {row["titre"]}</strong><br>
                    <small>👤 {row["responsable"]} | 🕐 {row["heure_debut"]}-{row["heure_fin"]} | 📍 {row["salle"]} | 📌 {row["statut"]}</small>
                </div>
                """, unsafe_allow_html=True)

def page_planning(data):
    st.title("📅 Gestion du Planning")

    tab1, tab2, tab3 = st.tabs(["📋 Liste des Activités", "➕ Ajouter une Activité", "🗓️ Vue Calendrier"])

    with tab1:
        df = df_taches(data)
        col1, col2, col3 = st.columns(3)
        with col1:
            filtre_statut = st.multiselect("Statut", df["statut"].unique(), default=list(df["statut"].unique()))
        with col2:
            filtre_cat = st.multiselect("Catégorie", df["categorie"].unique(), default=list(df["categorie"].unique()))
        with col3:
            filtre_priorite = st.multiselect("Priorité", df["priorite"].unique(), default=list(df["priorite"].unique()))

        df_filtered = df[df["statut"].isin(filtre_statut) & df["categorie"].isin(filtre_cat) & df["priorite"].isin(filtre_priorite)]
        df_filtered = df_filtered.sort_values("date_debut")

        st.markdown(f"**{len(df_filtered)} activité(s) affichée(s)**")
        for _, row in df_filtered.iterrows():
            badge_statut = {"Terminé": "🟢", "En cours": "🟡", "Planifié": "🔵", "Annulé": "🔴"}.get(row["statut"], "⚪")
            with st.expander(f"{badge_statut} {row['titre']} — {row['date_debut'].strftime('%d/%m/%Y')}"):
                col_a, col_b = st.columns(2)
                with col_a:
                    st.write(f"**Responsable :** {row['responsable']}")
                    st.write(f"**Date :** {row['date_debut'].strftime('%d/%m/%Y')} → {row['date_fin'].strftime('%d/%m/%Y')}")
                    st.write(f"**Horaire :** {row['heure_debut']} - {row['heure_fin']}")
                with col_b:
                    st.write(f"**Salle :** {row['salle']}")
                    st.write(f"**Catégorie :** {row['categorie']}")
                    st.write(f"**Priorité :** {row['priorite']}")
                st.write(f"**Description :** {row['description']}")
                col_edit, col_del = st.columns([1, 5])
                with col_edit:
                    if st.button("🗑️ Supprimer", key=f"del_{row['id']}"):
                        data["taches"] = [t for t in data["taches"] if t["id"] != row["id"]]
                        save_data(data)
                        st.success("Activité supprimée.")
                        st.rerun()

    with tab2:
        st.subheader("➕ Nouvelle Activité")
        with st.form("form_activite"):
            col1, col2 = st.columns(2)
            with col1:
                titre = st.text_input("Titre de l'activité *", placeholder="Ex: Réunion mensuelle")
                responsable = st.text_input("Responsable *", placeholder="Nom et prénom")
                date_debut = st.date_input("Date de début *", value=date.today())
                heure_debut = st.time_input("Heure de début *", value=datetime.strptime("08:00", "%H:%M").time())
            with col2:
                categorie = st.selectbox("Catégorie *", ["Réunion", "Formation", "Audit", "Événement", "Rédaction", "Maintenance", "Administration", "RH", "Autre"])
                priorite = st.selectbox("Priorité *", ["Très haute", "Haute", "Moyenne", "Basse"])
                date_fin = st.date_input("Date de fin *", value=date.today())
                heure_fin = st.time_input("Heure de fin *", value=datetime.strptime("17:00", "%H:%M").time())
            salle = st.text_input("Lieu / Salle", placeholder="Ex: Salle de conférence")
            statut = st.selectbox("Statut", ["Planifié", "En cours", "Terminé", "Annulé"])
            description = st.text_area("Description", placeholder="Description de l'activité...")
            submitted = st.form_submit_button("✅ Enregistrer l'activité", use_container_width=True)

            if submitted:
                if titre and responsable:
                    new_id = max([t["id"] for t in data["taches"]], default=0) + 1
                    new_item = {
                        "id": new_id, "titre": titre, "responsable": responsable,
                        "date_debut": str(date_debut), "date_fin": str(date_fin),
                        "heure_debut": str(heure_debut)[:5], "heure_fin": str(heure_fin)[:5],
                        "statut": statut, "priorite": priorite, "categorie": categorie,
                        "salle": salle, "description": description
                    }
                    data["taches"].append(new_item)
                    save_data(data)
                    st.success(f"✅ Activité '{titre}' ajoutée avec succès!")
                    st.rerun()
                else:
                    st.error("Veuillez remplir les champs obligatoires (*)")

    with tab3:
        st.subheader("🗓️ Diagramme de Gantt")
        df = df_taches(data)
        couleurs_statut = {"Terminé": "#27AE60", "En cours": "#F39C12", "Planifié": "#2980B9", "Annulé": "#E74C3C"}
        fig = px.timeline(
            df, x_start="date_debut", x_end="date_fin", y="titre",
            color="statut", color_discrete_map=couleurs_statut,
            hover_data=["responsable", "salle", "priorite"],
            labels={"titre": "Activité", "statut": "Statut"}
        )
        fig.update_yaxes(autorange="reversed")
        fig.update_layout(height=500, margin=dict(l=10, r=10, t=30, b=10))
        st.plotly_chart(fig, use_container_width=True)

def page_absences(data):
    st.title("🏖️ Gestion des Absences")
    tab1, tab2 = st.tabs(["📋 Liste des Absences", "➕ Déclarer une Absence"])

    with tab1:
        df = df_absences(data)
        today = pd.Timestamp(date.today())

        col1, col2, col3 = st.columns(3)
        absences_actuelles = df[(df["date_debut"] <= today) & (df["date_fin"] >= today)]
        absences_futures = df[df["date_debut"] > today]
        absences_passees = df[df["date_fin"] < today]
        col1.metric("🟡 En cours", len(absences_actuelles))
        col2.metric("🔵 À venir", len(absences_futures))
        col3.metric("🟢 Passées", len(absences_passees))

        st.markdown("---")
        for _, row in df.sort_values("date_debut", ascending=False).iterrows():
            delta = (row["date_fin"] - row["date_debut"]).days + 1
            statut_emoji = {"Approuvé": "✅", "En attente": "⏳", "Refusé": "❌"}.get(row["statut"], "❓")
            with st.expander(f"{statut_emoji} {row['agent']} — {row['type']} ({delta} jour(s))"):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Agent :** {row['agent']}")
                    st.write(f"**Type :** {row['type']}")
                    st.write(f"**Durée :** {delta} jour(s)")
                with col2:
                    st.write(f"**Début :** {row['date_debut'].strftime('%d/%m/%Y')}")
                    st.write(f"**Fin :** {row['date_fin'].strftime('%d/%m/%Y')}")
                    st.write(f"**Statut :** {row['statut']}")
                st.write(f"**Motif :** {row['motif']}")
                if st.button("🗑️ Supprimer", key=f"del_abs_{row['id']}"):
                    data["absences"] = [a for a in data["absences"] if a["id"] != row["id"]]
                    save_data(data)
                    st.success("Absence supprimée.")
                    st.rerun()

    with tab2:
        st.subheader("➕ Déclarer une Absence")
        with st.form("form_absence"):
            col1, col2 = st.columns(2)
            with col1:
                agent = st.text_input("Nom de l'agent *")
                type_absence = st.selectbox("Type d'absence *", ["Congé annuel", "Maladie", "Formation externe", "Congé maternité", "Récupération", "Congé sans solde", "Autre"])
                date_debut_abs = st.date_input("Date de début *", value=date.today(), key="abs_debut")
            with col2:
                statut_abs = st.selectbox("Statut", ["En attente", "Approuvé", "Refusé"])
                date_fin_abs = st.date_input("Date de fin *", value=date.today() + timedelta(days=1), key="abs_fin")
            motif = st.text_area("Motif *")
            submitted = st.form_submit_button("✅ Enregistrer", use_container_width=True)
            if submitted:
                if agent and motif:
                    new_id = max([a["id"] for a in data["absences"]], default=0) + 1
                    data["absences"].append({
                        "id": new_id, "agent": agent, "type": type_absence,
                        "date_debut": str(date_debut_abs), "date_fin": str(date_fin_abs),
                        "statut": statut_abs, "motif": motif
                    })
                    save_data(data)
                    st.success("✅ Absence enregistrée!")
                    st.rerun()
                else:
                    st.error("Veuillez remplir tous les champs obligatoires.")

def page_ressources(data):
    st.title("🏢 Gestion des Ressources")
    tab1, tab2 = st.tabs(["📋 Ressources disponibles", "➕ Ajouter une ressource"])

    with tab1:
        df = pd.DataFrame(data["ressources"])
        col1, col2 = st.columns(2)
        with col1:
            types = df["type"].unique()
            filtre_type = st.multiselect("Filtrer par type", types, default=list(types))
        df_filtered = df[df["type"].isin(filtre_type)]

        st.markdown(f"**{len(df_filtered)} ressource(s)**")
        for _, row in df_filtered.iterrows():
            icon = "🏛️" if row["type"] == "Salle" else "🚗" if row["type"] == "Véhicule" else "💻"
            with st.expander(f"{icon} {row['nom']} — Capacité: {row['capacite']}"):
                col_a, col_b = st.columns(2)
                with col_a:
                    st.write(f"**Type :** {row['type']}")
                    st.write(f"**Capacité :** {row['capacite']} personne(s)")
                with col_b:
                    st.write(f"**Équipements :** {row['equipements']}")
                if st.button("🗑️ Supprimer", key=f"del_res_{row['id']}"):
                    data["ressources"] = [r for r in data["ressources"] if r["id"] != row["id"]]
                    save_data(data)
                    st.success("Ressource supprimée.")
                    st.rerun()

    with tab2:
        st.subheader("➕ Nouvelle Ressource")
        with st.form("form_ressource"):
            col1, col2 = st.columns(2)
            with col1:
                nom_res = st.text_input("Nom de la ressource *")
                type_res = st.selectbox("Type *", ["Salle", "Véhicule", "Équipement", "Autre"])
            with col2:
                capacite = st.number_input("Capacité", min_value=1, value=10)
            equipements = st.text_area("Équipements / Description")
            submitted = st.form_submit_button("✅ Enregistrer", use_container_width=True)
            if submitted:
                if nom_res:
                    new_id = max([r["id"] for r in data["ressources"]], default=0) + 1
                    data["ressources"].append({
                        "id": new_id, "nom": nom_res, "type": type_res,
                        "capacite": capacite, "equipements": equipements
                    })
                    save_data(data)
                    st.success("✅ Ressource ajoutée!")
                    st.rerun()
                else:
                    st.error("Veuillez saisir un nom.")

def page_analyses(data):
    st.title("📊 Analyses Descriptives")

    df = df_taches(data)
    df_abs = df_absences(data)

    st.subheader("📈 Statistiques Générales")
    col1, col2, col3, col4 = st.columns(4)
    durees = (df["date_fin"] - df["date_debut"]).dt.days + 1
    col1.metric("Durée moyenne (jours)", f"{durees.mean():.1f}")
    col2.metric("Durée max (jours)", f"{durees.max()}")
    col3.metric("Activités haute priorité", len(df[df["priorite"].isin(["Haute", "Très haute"])]))
    durees_abs = (df_abs["date_fin"] - df_abs["date_debut"]).dt.days + 1
    col4.metric("Jours d'absences totaux", int(durees_abs.sum()))

    st.markdown("---")
    col_g, col_d = st.columns(2)

    with col_g:
        st.subheader("📊 Activités par Responsable")
        resp_counts = df["responsable"].value_counts().head(8).reset_index()
        resp_counts.columns = ["Responsable", "Nombre"]
        fig = px.bar(resp_counts, x="Nombre", y="Responsable", orientation="h",
                     color="Nombre", color_continuous_scale="Blues")
        fig.update_layout(height=350, margin=dict(l=10, r=10, t=10, b=10), yaxis_title="")
        st.plotly_chart(fig, use_container_width=True)

    with col_d:
        st.subheader("🎯 Répartition par Priorité")
        prio_counts = df["priorite"].value_counts().reset_index()
        prio_counts.columns = ["Priorité", "Nombre"]
        couleurs_prio = {"Très haute": "#E74C3C", "Haute": "#F39C12", "Moyenne": "#3498DB", "Basse": "#27AE60"}
        fig2 = px.pie(prio_counts, values="Nombre", names="Priorité",
                      color="Priorité", color_discrete_map=couleurs_prio)
        fig2.update_layout(height=350, margin=dict(l=10, r=10, t=10, b=10))
        st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📅 Volume d'Activités dans le Temps")
    df["mois"] = df["date_debut"].dt.to_period("W").astype(str)
    mois_counts = df.groupby(["mois", "statut"]).size().reset_index(name="count")
    fig3 = px.bar(mois_counts, x="mois", y="count", color="statut",
                  color_discrete_map={"Terminé": "#27AE60", "En cours": "#F39C12", "Planifié": "#2980B9"},
                  labels={"mois": "Semaine", "count": "Nombre d'activités", "statut": "Statut"})
    fig3.update_layout(height=350, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("📋 Tableau de Bord Complet")
    col_export1, col_export2 = st.columns([3, 1])
    with col_export2:
        csv = df.to_csv(index=False, encoding="utf-8-sig")
        st.download_button("⬇️ Exporter CSV", csv, "planning_export.csv", "text/csv", use_container_width=True)
    st.dataframe(
        df[["titre", "responsable", "date_debut", "date_fin", "statut", "priorite", "categorie", "salle"]].rename(columns={
            "titre": "Titre", "responsable": "Responsable", "date_debut": "Début",
            "date_fin": "Fin", "statut": "Statut", "priorite": "Priorité",
            "categorie": "Catégorie", "salle": "Salle"
        }),
        use_container_width=True, hide_index=True
    )

def main():
    st.set_page_config(
        page_title="PlanAdmin Pro | Bureau Administratif",
        page_icon="🏛️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown("""
    <style>
    .stMetric { background: white; border-radius: 10px; padding: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    .block-container { padding-top: 1rem; }
    [data-testid="stSidebar"] { background: #1E3A5F; }
    [data-testid="stSidebar"] * { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

    data = load_data()

    with st.sidebar:
        st.markdown(f"""
        <div style='text-align:center; padding: 1rem 0; border-bottom: 1px solid rgba(255,255,255,0.2); margin-bottom: 1rem;'>
            <div style='font-size: 2.5rem;'>🏛️</div>
            <div style='font-weight: 800; font-size: 1.2rem;'>PlanAdmin Pro</div>
            <div style='font-size: 0.75rem; opacity: 0.8;'>Gestion de Planning</div>
        </div>
        """, unsafe_allow_html=True)

        page = st.radio("Navigation", [
            "🏠 Tableau de bord",
            "📅 Planning",
            "🏖️ Absences",
            "🏢 Ressources",
            "📊 Analyses"
        ], label_visibility="collapsed")

        st.markdown("---")
        st.markdown(f"""
        <div style='font-size: 0.7rem; opacity: 0.7; padding: 0.5rem 0;'>
            <div>📌 INF232 — EC2</div>
            <div>🎓 <strong>{STUDENT_INFO['matricule']}</strong></div>
            <div style='word-break: break-word;'>{STUDENT_INFO['nom']}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style='font-size: 0.7rem; opacity: 0.6;'>
            Mis à jour le {datetime.now().strftime("%d/%m/%Y %H:%M")}
        </div>
        """, unsafe_allow_html=True)

    if page == "🏠 Tableau de bord":
        page_accueil(data)
    elif page == "📅 Planning":
        page_planning(data)
    elif page == "🏖️ Absences":
        page_absences(data)
    elif page == "🏢 Ressources":
        page_ressources(data)
    elif page == "📊 Analyses":
        page_analyses(data)

if __name__ == "__main__":
    main()
