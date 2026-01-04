import streamlit as st
from random import randint

dico = {
    0: ["Radiographie",{"Définition": ["Technique basée sur l'absorption différentielle des rayons X, selon la densité des tissus"],
                        "Principes": ["- Les rayons X sont envoyés sur la zone à étudier où ils vont être plus ou moins absorbés selon les tissus. Ils vont ensuite impressionner un film photosensible, ou être analysés par un logiciel informatique.",
                            "- Les zones claires d'une radiographie sont appelées opacités et correspondent aux tissus denses qui ont fortement absorbé les rayons X, par exemple, les os.",
                            "- Les zones sombres d'une radiographie sont appelées clartés et correspondent aux tissus mous qui ont peu absorbé les rayons X.",
                            "- L'étude des organes absorbant peu les rayons X nécessite l'utilisation de produit de contraste absorbant les rayons X."],
                        "Intérêts médicaux": ["Pour diagnostiquer des atteintes : fractures, malformation, présence de tumeur..."], 
                        "Avantages": ["Examen rapide. Non invasif. Peu onéreux. Indolore"], 
                        "Inconvénients": ["Clichés imprécis. Technique irradiante pour le personnel médical et le patient. Eventuelle allergie à l'iode. Rayons X cancérigènes et tératogènes."]}],
    1: ["Scanographie",{"Définition": ["Technique basée sur l'absorption différentielle des rayons X, selon la densité des tissus."], 
                        "Principes": ["- Les rayons X sont envoyés sur la zone à étudier où ils vont être plus ou moins absorbés selon les tissus. Ils vont ensuite impressionner un film photosensible, ou être analysés par un logiciel informatique.",
                            "- Dans le cas de la tomodensitométrie, l'émetteur de rayons X tourne autour du patient, ce qui permet d'obtenir des images selon plusieurs plans de coupes. Un traitement informatique permet de reconstruire les organes en trois dimensions. Les images sont ainsi plus précises."], 
                        "Intérêts médicaux": ["Il permet de voir une anomalie peu ou pas visible sur une radiographie ou une échographie. Il est très utile pour visualiser les organes du système nerveux central mais pas seulement. Il permet aussi de localiser une tumeur, confirmer un accident vasculaire cérébral, diagnostiquer une maladie osseuse etc."], 
                        "Avantages": ["Images en coupes et en 3D. Image plus précises. Examen indolore et non invasif"], 
                        "Inconvénients": ["Technique irradiante donc contre indiquée pour femme enceinte. Allergie possible à l'iode. Appareillage plus coûteux que celui de la radiographie. Rayons X cancérigènes et tératogènes."]}],
    2: ["IRM",{"Définition": ["Technique basée sur l'utilisation d'un champ magnétique et des ondes radios."], 
               "Principes": ["- En fonction de la teneur en hydrogène des tissus, un système informatique donne des images en coupes, en trois dimensions.",
                   "- La qualité des images peut être améliorée en injectant un produit de contraste, le gadolinium"], 
               "Intérêts médicaux": ["- Analyse Morphologique : ",
                   "Images très précises et en coupes, particulièrement bien adaptée à l'étude du SNC. Diagnostic de tumeurs, kystes... Mise en évidence de malformations.",
                   "- Analyse Fonctionelle : ",
                   "Basée sur l'étude de la circulation sanguine. Mise en évidence de zones mal oxygénées. Diagnostic de maladies neuro-dégénératives."], 
               "Avantages": ["Sans Danger. Indolore. Rares allergies au produit de contraste"], 
               "Inconvénients": ["Technique interdite aux patients portant de pacemakers, prothèse, éléments métalliques. Examen long et bruyant pouvant provoquer l'anxiété des personnes claustrophobes."]}],
    3: ["Echographie",{"Définition": ["Technique d'imagerie médicale basée sur l'utilisation d'ultrasons."], 
                       "Principes": ["- Les ultrasons sont émis par une sonde à une certaine fréquence vers les régions à examiner. Ces ondes reviennent vers la sonde selon le principe de l'écho. Selon la densité des tissus traversés, leur éloignement par rapport à la sonde, la fréquence des ultrasons est plus ou moins modifiée. Un système informatique permet d'obtenir des images en direct."], 
                       "Intérêts médicaux": ["- Analyse morphologique : ",
                           "Mise en évidence de malformations. Recherche de tumeurs, kystes, nodules... Echographie obstétricale : Suivi de la grossesse et du développement du foetus",
                           "- Echographie Doppler : ",
                           "Les globules réfléchissent les ultrasons en modifiant leur fréquence. Plus les cellules vont vite, plus la fréquence est modifiée. Cette technique permet de mesurer la vitesse d'écoulement du sang, et de dépister des sténoses ou des thromboses."], 
                       "Avantages": ["Observation en temps réel et en mouvement."], 
                       "Inconvénients": ["Aucun danger ni contre-indication."]}],
    4: ["Scintigraphie",{"Définition": ["Technique d'imagerie médicale basée sur l'utilisation d'un isotope radioactif"], 
                         "Principes": ["- L'isotope est injecté par voie intraveineuse et se fixe sur les tissus ou organes à explorer. Il émet alors des rayonnements gamma détectés par une gammacaméra.",
                             "- Le niveau de fixation de l'isotope dans les cellules dépend de leur activité. Plus la cellule est active, plus la fixation est forte. A l'inverse, si les cellules sont nécrosées, la fixation est faible voire nulle.",
                             "- Un traitement informatique permet d'obtenir des images en couleur : rouge, si les cellules fixent fortement l'isotope, jaune/vert, quand la fixation est moyenne, bleu quand les cellules fixent peu ou pas l'isotope."], 
                         "Intérêts médicaux": ["Scintigraphie cardiaque : évaluer les conséquences d'un infarctus : mise en évidence de cellules nécrosées. Evaluer le volume d'éjection systolique cardiaque.",
                             "Cancérologie : Dépister tumeur ou métastases = zone de forte fixation isotope."], 
                         "Avantages": ["Examen peu invasif. Indolore. Examen Global."], 
                         "Inconvénients": ["Utilisation de la radioactivité = cancérigène. Réalisé dans des centres de médecine nucléaire. Protection du personnel. Traitement approprié des déchets. Nombre de scintigraphies à limiter."]}],
    5: ["Fibroscopie",{"Définition": ["Technique basée sur l'introduction d'un fibroscope dans une cavité ouverte ou fermée du corps, d'un tube muni de fibres optiques et d'une source de lumière froide pour observer la paroi de cette cavité."], 
                       "Principes": ["- Par voie haute : Introduction du fibroscope par voie buccale. Exploration de l'oesophage, estomac et duodénum.",
                                     "- Par voie basse : Introduction du fibroscope par voie anale. Exploration du rectum, colon et la fin de l'iléon."], 
                       "Intérêts médicaux": ["- Observation des cavités.",
                           "- Obtention d'images de qualité, en trois dimensions et en couleur.",
                           "- Vision directe.",
                           "- Mise en évidence de malformation, polype, tumeur...",
                           "- Prélèvement d'un fragment de tissu appelé biopsie pour une analyse anatomopathologique.",
                           "- Ablation d'une tumeur ou de l'appendice par exemple."], 
                       "Avantages": ["Vision directe. Examen rapide, facile à réaliser et pouvant être répéter. Possibilité de réaliser biopsie."], 
                       "Inconvénients": ["Préparation longue avant l'examen. Gestes très techniques. Gênant voire douloureux. Anesthésie locale ou générale. Risques de perforation. Risques d'infection nosocomiale."]}]
}

dico_indice2 = {0: "Définition",
                1: "Principes",
                2: "Intérêts médicaux",
                3: "Avantages",
                4: "Inconvénients"
}

if "score" not in st.session_state:
    st.session_state.score = 0
if "questions" not in st.session_state:
    st.session_state.questions = {}
if "dico_reponses" not in st.session_state:
    st.session_state.dico_reponses = {}
if "current" not in st.session_state:
    st.session_state.current = None
if "step" not in st.session_state:
    st.session_state.step = "debut"
if "end" not in st.session_state:
    st.session_state.end = {}
if "dico" not in st.session_state:
    st.session_state.dico = dico.copy()
if "indice" not in st.session_state:
    st.session_state.current = None
if "indice2" not in st.session_state:
    st.session_state.current = None

st.title("Quiz Imagerie Médicale")

if st.session_state.step == "debut":
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        if st.button("Radiographie"):
            st.session_state.indice = 0
            st.session_state.step = "question"
            st.rerun() 
    with col2:
        if st.button("Scanographie ou Tomodensitométrie"):
            st.session_state.indice = 1
            st.session_state.step = "question"
            st.rerun() 
    with col3:
        if st.button("IRM"):
            st.session_state.indice = 2
            st.session_state.step = "question"
            st.rerun() 
    with col4:
        if st.button("Echographie"):
            st.session_state.indice = 3
            st.session_state.step = "question"
            st.rerun() 
    with col5:
        if st.button("Scintigraphie"):
            st.session_state.indice = 4
            st.session_state.step = "question"
            st.rerun() 
    with col6:
        if st.button("Fibroscopie"):
            st.session_state.indice = 5 
            st.session_state.step = "question"
            st.rerun()  
    

if st.session_state.step == "question":
    st.session_state.reponse = ""
    if len(st.session_state.questions.keys()) >= len(st.session_state.dico.keys()):
        st.session_state.step = "fin"
        st.rerun()
    st.session_state.step = "reponse"
    st.rerun()

if st.session_state.step == "reponse":
    if "indice2" not in st.session_state or st.session_state.indice2 is None:
        st.session_state.indice2 = randint(0,4)
    imagerie = st.session_state.dico[st.session_state.indice][0]
    st.session_state.questions[st.session_state.indice] = imagerie
    st.write("Imagerie : "+imagerie)
    with st.form("form_reponse"):
        st.write(dico_indice2[st.session_state.indice2]+" : ")
        reponse = st.text_input("Écris ta réponse", key="reponse_input")
        validee = st.form_submit_button("Valider")

    if st.button("Stop"):
        st.session_state.step = "fin"

    elif validee:
        st.session_state.step = "feedback"
        st.session_state.reponse = reponse
        st.rerun()

if st.session_state.step == "feedback":
    st.write("La réponse était : ")
    for chaine in st.session_state.dico[st.session_state.indice][1][dico_indice2[st.session_state.indice2]]:
        st.write(chaine)
    st.write("Ta réponse était : "+st.session_state.reponse)
    vrai_faux = st.radio("Tu as eu :", ["Vrai", "Faux"], horizontal=True)

    if st.button("Continuer"):
        if vrai_faux == "Vrai":
            st.session_state.score += 1
        elif vrai_faux == "Faux":
            st.session_state.end[st.session_state.indice] = st.session_state.dico[st.session_state.indice][1][dico_indice2[st.session_state.indice2]]
        st.session_state.step = "question"
        st.session_state.indice2 = None
        st.rerun()

if st.session_state.step == "fin":
    st.write("C'est fini ! Ton score est de : "+str(st.session_state.score)+"/"+str(len(st.session_state.dico_reponses.keys()))+ " Bravo mon coeur t'es trop forte !")
    if len(st.session_state.end.keys())>1:
        st.write("Tes reponses fausses etaient : ")
    elif len(st.session_state.end.keys()) == 1:
        st.write("Ta reponse fausse etait : ")
    else:
        st.write("Tu n'as eu aucune reponse fausse bravo !")
    for tab in st.session_state.end.values():
        chaine = ""
        for item in tab:
            chaine = chaine + str(item) + " "
        st.write(chaine)
    if st.button("Refaire"):
        st.session_state.score = 0
        st.session_state.questions = {}
        st.session_state.end = {}
        st.session_state.current = None
        st.session_state.step = "debut"
        st.session_state.dico = dico.copy()
        st.session_state.indice = None
        st.session_state.indice2 = None
        st.session_state.reponse = ""
        st.rerun()