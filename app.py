import streamlit as st
from chatbot import *
st.title(":mechanical_arm: Asistente Virtual")

if "messages" not in st.session_state:
    st.session_state.messages = []
if "first_message" not in st.session_state:
    st.session_state.first_message = True

for messages in st.session_state.messages:
    with st.chat_message(messages["role"]):
        st.markdown(messages["content"])

if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("Hola, ¿Como puedo ayudar?")

    st.session_state.messages.append({"role":"assistant", "content":"Hola, ¿Como puedo ayudar?"})
    st.session_state.first_message = False

if prompt := st.chat_input("¿Como puedo ayudar?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role":"user", "content":prompt})

    #se usa la IA
    res, ints = respuesta(prompt)

    with st.chat_message("assistant"):
        st.markdown(res)
    st.session_state.messages.append({"role":"assistant", "content":res})