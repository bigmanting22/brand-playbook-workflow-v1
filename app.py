import streamlit as st
from langfloww import rag_chain

st.title("LangGraph RAG App")

query = st.text_input("what do you want to know about the brands we work with?")

if query:
    answer, context = rag_chain(query)
    st.write("### Answer")
    st.write(answer)
    st.write("### Retrieved Context")
    for chunk in context:
        st.write(f"- {chunk}")