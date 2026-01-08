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

# Landing minimal (biar Streamlit selesai init dulu)
st.markdown("### Memuat aplikasi...")

# Auto redirect via query param kecil (hindari switch di frame pertama)
if st.session_state.auth.get("is_logged_in"):
    if st.button("Masuk ke Order", use_container_width=True):
        st.switch_page("pages/3_User_Order.py")
else:
    if st.button("Ke Halaman Login", use_container_width=True):
        st.switch_page("pages/1_Login.py")
