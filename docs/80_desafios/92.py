import streamlit as st

st.markdown("# Datos")

c1, c2 = st.columns([5,7])

m="""
- La conexión a Bases de Datos se hace de la misma manera que se hacen normalmente en python. 
- Por seguridad las Bases de Datos suelen estar protegidas y aceptar conexiones de IP específicas. 
- Desde streamlit.share.io:
    - Agregar las 6 IPs estables a whitelist: 34.127.33.101, 35.230.127.150, 34.127.0.121, 35.230.58.211, 34.127.88.74, y 35.230.56.30
- Desde provisión propia:
    - Configuraciones según la modalidad.
"""

c1.markdown(m)

c2.image("images/bbdd.jpg", width=400)