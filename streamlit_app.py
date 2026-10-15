import streamlit as st
import streamlit.components.v1 as components
import os

# Configure Streamlit Page
st.set_page_config(
    page_title="AccessOSM — Inclusive Urban Mobility & Amenity Navigator",
    page_icon="♿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Inject CSS to make the app full-bleed and hide Streamlit chrome
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {
        padding: 0rem !important;
        margin: 0rem !important;
        max-width: 100vw !important;
        height: 100vh !important;
        overflow: hidden !important;
    }
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        border: none !important;
        display: block !important;
    }
</style>
""", unsafe_allow_html=True)

# Path to local files
current_dir = os.path.dirname(os.path.abspath(__file__))

index_path = os.path.join(current_dir, "index.html")
styles_path = os.path.join(current_dir, "styles.css")
app_path = os.path.join(current_dir, "app.js")

# Read components
with open(index_path, "r", encoding="utf-8") as f:
    html_content = f.read()

with open(styles_path, "r", encoding="utf-8") as f:
    css_content = f.read()

with open(app_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# Inline CSS & JavaScript so it runs seamlessly inside Streamlit's iframe sandbox
bundled_html = html_content.replace(
    '<link rel="stylesheet" href="styles.css">',
    f"<style>\n{css_content}\n</style>"
)

bundled_html = bundled_html.replace(
    '<script src="app.js"></script>',
    f"<script>\n{js_content}\n</script>"
)

# Render interactive component
components.html(bundled_html, height=920, scrolling=False)
