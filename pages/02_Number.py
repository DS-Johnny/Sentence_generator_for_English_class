import streamlit as st
from random import randint

st.set_page_config(
    page_title="A1A Sentence Generator",
    page_icon="📚",
    layout="wide"
)

exercise, content = st.tabs(['Exercise', 'Content'])

with exercise:
    # ================================ CSS
    with open('style_place_value.txt', 'r', encoding='utf-8') as f:
        estilo = f.read()

    st.markdown(estilo, unsafe_allow_html=True)  # CARREGA CSS

    num_cat = randint(1,3)
    if num_cat == 1:
        num_raw = randint(1,999)
    
    elif num_cat == 2:
        num_raw = randint(1000,999999)
    
    else:
        num_raw = randint(1000,999999999)
    # ================================ NÚMERO
    # numero = "4728"  # vindo do seu gerador aleatório (3 a 9 dígitos)

    numero = str(num_raw)
    digitos = list(numero)
    digitos = [""] * (9 - len(digitos)) + digitos  # alinha à direita

    pos = {f"d{i+1}": digitos[i] for i in range(9)}

    # ================================ GRÁFICO
    st.html(f"""
    <div class="chart">

        <div class="connector connector-up" id="conn-m"></div>
        <div class="label label-top" id="lbl-m">Million</div>

        <div class="connector connector-up" id="conn-t"></div>
        <div class="label label-top" id="lbl-t">Thousand</div>

        <div class="slot" id="pos1">{pos['d1']}</div>
        <div class="slot" id="pos2">{pos['d2']}</div>
        <div class="slot" id="pos3">{pos['d3']}</div>
        <div class="slot" id="pos4">{pos['d4']}</div>
        <div class="slot" id="pos5">{pos['d5']}</div>
        <div class="slot" id="pos6">{pos['d6']}</div>
        <div class="slot" id="pos7">{pos['d7']}</div>
        <div class="slot" id="pos8">{pos['d8']}</div>
        <div class="slot" id="pos9">{pos['d9']}</div>

        <div class="connector connector-down" id="conn-h1"></div>
        <div class="label label-hundred" id="lbl-h1">Hundred</div>

        <div class="connector connector-down" id="conn-h2"></div>
        <div class="label label-hundred" id="lbl-h2">Hundred</div>

        <div class="connector connector-down" id="conn-h3"></div>
        <div class="label label-hundred" id="lbl-h3">Hundred</div>

    </div>
    """)

    col1, col2, col3, col4, col5 = st.columns(5)  # Gambiarra para centralizar o botão

    with col3:
        if st.button("Regenerate"):
            st.rerun()

with content:
    st.image('./images/numbers.png', width=1000)