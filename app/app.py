# app.py

import streamlit as st
from generation import generate_answer
from gemini_client import generate_text

st.title("Chat with David's model")

with st.sidebar:
    with st.expander("Project Description"):
        st.write(
                """
                This chatbot is powered by a Retrieval-Augmented Generation (RAG) pipeline
                connected to Google's Gemini API. It is designed to answer questions about
                my (David Arzumanyan's) background, education, projects, technical skills, and
                professional experience by retrieving information from a curated knowledge base.

                Rather than relying solely on a language model's memory, the chatbot searches
                relevant documents and provides responses grounded in real information about
                David's academic and industry experience.
                """)

    st.header("Example Questions")

    st.write("* Tell me about your Data Science experience.")
    st.write("* What machine learning projects have you worked on?")
    st.write("* What technologies did you use to build this chatbot?")
    st.write("* What can you bring to our team?")
    st.write("* How does the RAG pipeline behind this project work?")

    st.header("Note")

    st.write(
        """
        This chatbot is intended to simulate a conversation with David and therefore
        responds in the first person. All answers are generated from information
        contained within the project's knowledge base.
        """
    )


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# Walrus operator := asks the prompt and stores the variable prompt at the same time
if prompt := st.chat_input("Ask a question"):

    # User's message in the chat
    with st.chat_message("user"):
        st.write(prompt)
    
    # Saving user's message in the session state
    st.session_state.messages.append(
    {"role": "user", "content": prompt}
    )

    # Model's message (response) in the chat
    with st.chat_message("assistant"):
        response = st.write_stream(generate_answer(prompt, st.session_state.messages)) # write_stream accepts generators only

    # Saving model's message (response) in the session state
    st.session_state.messages.append(
    {"role": "assistant", "content": response}
    )
