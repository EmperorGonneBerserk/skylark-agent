import streamlit as st
from agent import handle_query

st.set_page_config(page_title="Skylark Drone Coordinator", page_icon="🚁")

st.title("🚁 Skylark Drone Operations Coordinator AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.write(message)

user_input = st.chat_input("Enter command (example: assign PRJ001)")

if user_input:

    st.session_state.messages.append(("user", user_input))

    response = handle_query(user_input)

    st.session_state.messages.append(("assistant", response))

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        st.write(response)
