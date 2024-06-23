import streamlit as st
from langchain.chains.conversation.base import ConversationChain

from langchain.prompts import PromptTemplate
from langchain_community.llms.ctransformers import CTransformers


# Function to get response from Llama 2 model

def getllamaresponse(input_text, no_words, blog_style):
    # Llama 2 model
    llm = CTransformers(model="/Users/yash/Workspaces/nlp-model/llama-2-7b-chat.Q3_K_L.gguf", model_type="llama",
                        config={"max_new_tokens": 256, "temperature": 0.01})

    # Prompt Template
    template = """
    Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."""

    prompt = PromptTemplate.from_template(template)
    chain = prompt | llm
    response = chain.invoke({"blog_style":blog_style, "input_text": input_text, "no_words": no_words})

    print(response)
    return response


st.set_page_config(page_title="Generate Blogs", page_icon='', layout="centered", initial_sidebar_state="collapsed")

st.header("Generate Blogs")
input_text = st.text_input("Enter the Blog Topic")

# create two more columns for additonal 2 fields

col1, col2 = st.columns([5, 5])
with col1:
    no_words = st.text_input("No of Words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Scientist", "Common People"), index=0)

submit = st.button("Generate")

if submit:
    st.write(getllamaresponse(input_text, no_words, blog_style))
