import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

import time

if "last_request" not in st.session_state:
    st.session_state.last_request = 0
def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")

    #sample url for testing
    #url_input = st.text_input(
        #"Enter a URL:",
        #value="https://www.atlassian.com/company/careers/details/25318"
    #) 

    url_input = st.text_input(
    "Enter a Job URL:"
    )
    submit_button = st.button("Submit")

    if submit_button:

        current_time = time.time()

        if current_time - st.session_state.last_request < 10:
            st.warning("Please wait 10 seconds before generating another email.")
            return

        st.session_state.last_request = current_time

        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            portfolio.load_portfolio()

            jobs = llm.extract_jobs(data)

            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)

                email = llm.write_mail(job, links)

                st.code(email, language="markdown")

        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":

    st.set_page_config(
        layout="wide",
        page_title="Cold Email Generator",
        page_icon="📧"
    )

    if "chain" not in st.session_state:
        st.session_state.chain = Chain()

    if "portfolio" not in st.session_state:
        st.session_state.portfolio = Portfolio()

    create_streamlit_app(
        st.session_state.chain,
        st.session_state.portfolio,
        clean_text
    )
