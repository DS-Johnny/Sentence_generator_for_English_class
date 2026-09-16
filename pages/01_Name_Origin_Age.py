import streamlit as st
from gerador_de_frases import A1A_sentence_generator

generator = A1A_sentence_generator()

st.set_page_config(
    page_title="A1A Sentence Generator",
    page_icon="📚",
    layout="wide"
)

exercicio, conteudo = st.tabs(['Exercise', 'Content'])
with exercicio:

    # ================================ CSS
    with open('style.txt', 'r', encoding='utf-8') as f:
        estilo = f.read()

    st.markdown(estilo, unsafe_allow_html=True) # CARREGA CSS


    # ================================ SIDEBAR
    st.sidebar.title("SENTENCE GENERATOR")


    # ================================ FRASES

    tipo, frase_pt, frase_en = generator.gerar_frases()

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
    col1, col2= st.columns(2)
    with col1:
        st.image('./images/subject_pronouns_tobe.png')

    with col2:
        st.image('./images/possessive_adjectives.png')
    
    nome, origem, idade, wh_questions = st.tabs(['Name', 'Origin', 'Age', 'WH Questions'])
    with nome:
        st.image('./images/name.png',width=1000)

    with origem:
        st.image('./images/origin.png',width=1000)
    
    with idade:
        st.image('./images/age.png',width=1000)
    
    with wh_questions:
        st.image('./images/wh_questions.png',width=1000)

