import streamlit as st
import streamlit_book as stb

st.set_page_config(layout="wide")

# Set multipage
stb.set_book_config(menu_title="Charla",
                    menu_icon="file-richtext",
                    options=[
                            "Introducción",
                            "Problema Ilustrador",
                            "Webapps", 
                            "Streamlit", 
                            "Desafíos en la industria", 
                            "Conclusión", 
                            ],
                    paths=[
                            "docs/00_intro/", 
                            "docs/10_problema/", 
                            "docs/20_webapps/", 
                            "docs/50_streamlit/", 
                            "docs/80_desafios/", 
                            "docs/90_conclusion/", 
                            ],
                    save_answers=False,
                    )