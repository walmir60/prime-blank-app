import streamlit as st

st.title("Echo Bot")

prompt = st.chat_input("Diga algo...")
if prompt:
    st.write(f"Usuário disse: {prompt}")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])