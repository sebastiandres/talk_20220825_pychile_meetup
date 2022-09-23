import streamlit as st

st.markdown("# ¿Qué necesitamos en la industria?")

c1, c2 = st.columns([5,7])

m="""
## - Repositorios de código
## - Bases de datos
## - Deployment
## - Autenticación
"""

c1.markdown(m)

#c2.image("images/options.png", width=600)