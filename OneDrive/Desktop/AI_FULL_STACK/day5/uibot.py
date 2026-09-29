import ollama
import streamlit as st
st.title(":red[**Hello Uibot 🤖**!!]")
with st.sidebar:
    personalites={
        "kid👶":"give the answer like are explaining to a 5 year old kid.give the answer in 2 lines only.",
        "professor 👨‍🏫":"you are IIT professor.explain the topics using correct terminology.give the answer in 2 lines only",
        "student 👨🏻‍🎓":"i am college student.exlaining to a 15 year old student the answer in 2-3 lines only"
    }
    personality=st.selectbox("select a personlity",personalites.keys())
    if st.button("clear chat🚮"):
        st.session_state.messages=[]
        st.success("chat cleared successfully")
    uploaded_file=st.file_uploader("upload a file...")
    if uploaded_file:
        st.write("File uploaded successfully...")
        with st.expander("preview"):
            context=uploaded_file.read().decode("utf-8")
            st.text(context)
if "messages" not in st.session_state:
    st.session_state.messages = []
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("You : ")
if question:
    with st.chat_message("User 👤 "):
        st.write("User: ",question)
    st.session_state.messages.append(
        {
            "role" : "user",
            "content" : question
        }
    )
    with st.spinner("Thinking......🤔"):
        response = ollama.chat(
            model="llama3.2:3b",
            messages = [{
                "role":"system","content":"personalities[personality]"
            }] + st.session_state.messages
            )
    st.session_state.messages.append(
            {
                "role" : "assistant",
                "content":response["message"]["content"]
            }
        )
    with st.chat_message("Assistant"):
        st.write("AI:",response["message"]["content"])
        st.balloons()
        


