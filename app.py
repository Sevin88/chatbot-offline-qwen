import streamlit as st
import utils

st.title(":llama: qwen2.5 AI")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role":"assistant",
                                     "content": "How can i help you"}]

# st.chat_message("assistant").write("How can i help you?")
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])
model = "qwen2.5-coder:7b"
prompt = st.chat_input("Enter your question! ")
if prompt:

    st.chat_message("user").write(prompt)
    st.session_state["messages"].append({"role":"user", "content":prompt})

    if "password" in prompt:
        st.chat_message("ai").write("I can not asnwer to these topics")
    else:
        with st.spinner("Wait for generate response..."):
            result = utils.call_ollama_model(model, prompt)

        st.chat_message("assistant").write(result)
        st.session_state["messages"].append({"role":"ai", "content":result})