import streamlit as st

st.set_page_config(
    page_title="Depo 78",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if "auth" not in st.session_state:
    st.session_state.auth = {"is_logged_in": False, "user": None}

st.title("🛒 Depo 78")

# Tombol navigasi (AMAN di Cloud)
if st.session_state.auth.get("is_logged_in"):
    st.success("Anda sudah login.")
    if st.button("Lanjut ke Order", use_container_width=True):
        st.switch_page("pages/3_User_Order.py")
else:
    st.info("Silakan login untuk melanjutkan.")
    if st.button("Ke Halaman Login", use_container_width=True):
        st.switch_page("pages/1_Login.py")
