import streamlit as st

st.markdown("## Repositorios de código")

c1, c2 = st.columns([5,7])

m="""
- Actualmente share.streamlit.io sólo puede conectar con github. 
- Algunas empresas usan otros proveedores: bitbucket, gitlab, etc.

El foco de streamlit no está en la industria. Eso hace que no se prioricen ciertas features que uno esperaría.
De todas maneras, el desarrollo de la librería va rápido!

"""

c1.markdown(m)

c2.image("images/repos.jpg", width=400)