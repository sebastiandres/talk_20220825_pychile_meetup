import streamlit as st

st.markdown("# Bases de datos")

c1, c2 = st.columns([5,7])

m="""
- Conviene usar st.secrets para no dejar contraseñas dando vueltas
- Conviene usar st.cache para almacenar la conexión o los datos extraídos, y no rejecutar las operaciones.
"""

c1.markdown(m)

c2.image("images/bbdd.jpg", width=400)