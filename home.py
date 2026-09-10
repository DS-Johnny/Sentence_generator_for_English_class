import streamlit as st
from gerador_de_frases import A1A_sentence_generator

generator = A1A_sentence_generator()

st.set_page_config(
    page_title="A1A Sentence Generator",
    page_icon="📚",
    layout="centered"
)

# ================================
# CSS
# ================================
with open('style.txt', 'r', encoding='utf-8') as f:
    estilo = f.read()

st.markdown(estilo, unsafe_allow_html=True)


# ================================
# FRASES
# ================================

tipo, frase_pt, frase_en = generator.gerar_frases()


# ================================
# HEADER
# ================================

st.markdown("""
<div class="page-title">
    ENGLISH CLASS
</div>

<div class="page-subtitle">
    Passe o mouse sobre o cartão para revelar a tradução
</div>
""", unsafe_allow_html=True)


# ================================
# CARD
# ================================

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


# ================================
# BOTÃO
# ================================
col1, col2, col3, col4, col5 = st.columns(5)

with col3:
    if st.button("Regenerate"):
        st.rerun()
