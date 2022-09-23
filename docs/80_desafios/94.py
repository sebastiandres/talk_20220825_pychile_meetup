import streamlit as st

st.markdown("# Opciones de Deployment")

c1, c2 = st.columns([5,7])

m="""
- streamlit.share.io
- HuggingFace
- Heroku: casi tan simple como streamlit.share.io
- Digital Ocean
- Azure Microsoft
- Amazon Web Services AWS
- GCP Google Cloud Platform
"""

c1.markdown(m)

c2.image("images/options.png", width=600)