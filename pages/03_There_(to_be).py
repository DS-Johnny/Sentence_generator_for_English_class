import streamlit as st
from gerador_de_frases import There_to_be_city_generator

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
    pass

