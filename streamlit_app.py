import streamlit as st

st.set_page_config(
    page_title="Depo 78",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# INIT AUTH
if "auth" not in st.session_state:
    st.session_state.auth = {"is_logged_in": False, "user": None}

st.title("🛒 Depo 78")

st.info("Klik tombol untuk masuk ke halaman Login (aman untuk Streamlit Cloud).")

# ✅ switch_page hanya dipanggil saat ada interaksi tombol
if st.button("➡️ Ke Halaman Login", use_container_width=True):
    st.switch_page("pages/1_Login.py")
