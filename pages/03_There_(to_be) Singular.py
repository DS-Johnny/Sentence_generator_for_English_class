import streamlit as st
from gerador_de_frases import There_to_be_city_generator
import pandas as pd
import json

generator = There_to_be_city_generator()

st.set_page_config(
    page_title="There to be Simple Sentence Generator",
    page_icon="📚",
    layout="wide"
)

exercicio, conteudo = st.tabs(['Exercise', 'Content'])
with exercicio:

    # ================================ CSS
    with open('./styles/style.txt', 'r', encoding='utf-8') as f:
        estilo = f.read()

    st.markdown(estilo, unsafe_allow_html=True) # CARREGA CSS


    # ================================ SIDEBAR
    st.sidebar.title("SENTENCE GENERATOR")


    # ================================ FRASES

    frase_pt, frase_en = generator.gerar_there_tobe_singular()

    # ================================ HEADER

    st.markdown("""
    <div class="page-title">
        ENGLISH CLASS
    </div>

    <div class="page-subtitle">
        Hover over(or tap) the card to reveal the translation
    </div>
    """, unsafe_allow_html=True)

    # ================================ CARD

    st.html(f"""
    <div class="card">

        <div class="card-inner">

            <div class="card-front">
                <span>{frase_pt}</span>
            </div>

            <div class="card-back">
                <span>{frase_en}</span>
            </div>

        </div>

    </div>
    """)

    # ================================ BOTÃO
    col1, col2, col3, col4, col5 = st.columns(5) # Gambiarra para centralizar o botão

    with col3:
        if st.button("Regenerate"):
            st.rerun()

with conteudo:
    with open('data/areas.json', 'r', encoding='utf-8') as f:
        areas = json.load(f)
        
    with open('data/places.json', 'r', encoding='utf-8') as f:
        places = json.load(f)

    dados_areas = {
        "Portuguese" : [],
        "English" : []
    }

    for k,v in areas.items():
        dados_areas['Portuguese'].append(k)
        dados_areas['English'].append(v['en']['translation'])

    dados_places = {
        "Portuguese" : [],
        "English" : [],
        "Article" : []
    }

    for k,v in places.items():
        dados_places['Portuguese'].append(k)
        dados_places['English'].append(v['en']['translation'])
        dados_places['Article'].append(v['en']['article'])
        
    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(pd.DataFrame(dados_areas))
    with col2:
        st.dataframe(pd.DataFrame(dados_places))
        
