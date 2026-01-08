import streamlit as st

st.set_page_config(
    page_title="Depo 78",
    page_icon="🛒",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if "auth" not in st.session_state:
    st.session_state.auth = {"is_logged_in": False, "user": None}

# flag 1x agar tidak loop
if "boot_redirected" not in st.session_state:
    st.session_state.boot_redirected = True
    st.rerun()

# setelah rerun kedua, baru switch
if st.session_state.auth.get("is_logged_in"):
    st.switch_page("pages/3_User_Order.py")
else:
    st.switch_page("pages/1_Login.py")
