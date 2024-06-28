import os

import streamlit as st


def display_defensive_warning() -> None:
    """
    Let the user know that the LLM can output incorrect answers.
    """
    st.warning("""As an LLM, I cannot guarantee that the SQL code I generated will provide you with the answer you 
               need for your question. Try to be as precise as possible. Moreover, it would help if you can specify 
               the schema of your database.
               """, icon="⚠️")


def get_openai_api_key() -> None:
    """
    Get the OpenAI API key from the user.
    """
    openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
    os.environ["OPENAI_API_KEY"] = openai_api_key
    if not openai_api_key.startswith("sk-"):
        st.error("Please enter your OpenAI API key!", icon="⚠️")
