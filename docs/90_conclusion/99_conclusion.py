import streamlit as st

st.markdown("# Conclusión")

c1, c2 = st.columns([3,4])
c1.image("images/preguntas.jpg", width=400)
m="""
### - Streamlit acelera creación de MVP y desarrollos internos.
### - Hacer deployment con streamlit.share.io es fácil pero con poco control.
### - Encargarse de todo el deployment requiere considerar todas las aristas.
"""
c2.markdown(m)
