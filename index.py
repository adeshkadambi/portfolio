import streamlit as st
from pathlib import PurePath


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def markdown(filename: str):
    with open(PurePath(__file__).parent / "markdown" / f"{filename}.md", "r") as f:
        st.markdown(f.read())


def about():
    st.image("logo.png", width=100)
    markdown("about-me")

def education():
    st.

def main():
    local_css("styles.css")
    about()
    education()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Adesh Kadambi",
        page_icon="logo.png",
    )
    main()
