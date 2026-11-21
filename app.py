import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mostafa Mahmoud | Data & AI Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide default Streamlit top padding/menu for a cleaner full-screen portfolio view
st.markdown(
    """
    <style>
        .block-container { padding-top: 1rem; padding-bottom: 0rem; }
        header { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([4, 1])
with col1:
    st.markdown("### Mostafa Mahmoud — Data Engineering & Analytics Portfolio")
with col2:
    st.link_button("Open Full Screen ↗", "https://mostafamahmoud-25.github.io/portfolio/", use_container_width=True)

# Embed your live GitHub Pages portfolio
components.iframe("https://mostafamahmoud-25.github.io/portfolio/", height=950, scrolling=True)
