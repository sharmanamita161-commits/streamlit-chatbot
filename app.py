import streamlit as st

st.title("💬 Simple Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append(("You", user_input))
        response = "You said: " + user_input
        st.session_state.messages.append(("Bot", response))

for sender, message in st.session_state.messages:
    st.write(f"**{sender}:** {message}")
