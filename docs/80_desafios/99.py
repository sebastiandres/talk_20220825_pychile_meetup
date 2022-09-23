import streamlit as st

st.markdown("# Autenticación")

c1, c2 = st.columns([3,4])
c1.image("images/pass.png", width=400)
m="""
- En streamlit.share.io:
    - Apps públicas: disponible para cualquiera con la url
    - Apps privadas: requiere que los usuarios creen una cuenta streamlit.share.io, y estén en la lista de correos o @dominios permitidos.
    - Apps públicas con autenticación: es posible separar la app en una página de login y otra de contenido. 
        - httpx-oauth Google 
        - streamlit-azure-ad-login 
"""
c2.markdown(m)
