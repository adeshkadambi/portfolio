from pathlib import PurePath

import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def markdown(filename: str):
    with open(PurePath(__file__).parent / "markdown" / f"{filename}.md", "r") as f:
        st.markdown(f.read())


def header():
    st.image("files/logo.png", width=100)
    st.title("Hi, I'm Adesh Kadambi!")


def socials():
    github, linkedin, scholar, email = st.columns(4)

    with github:
        st.link_button(
            "GitHub",
            "https://github.com/adeshkadambi/",
            use_container_width=True,
        )

    with linkedin:
        st.link_button(
            "LinkedIn",
            "https://www.linkedin.com/in/akadambi/",
            use_container_width=True,
        )

    with scholar:
        st.link_button(
            "Google Scholar",
            "https://scholar.google.com/citations?hl=en&user=y6O3yK0AAAAJ",
            use_container_width=True,
        )

    with email:
        st.link_button(
            "Email", "mailto:adeshkadambi@gmail.com", use_container_width=True
        )


def about():
    markdown("about-me")
    st.image("files/interests.png")
    markdown("research-interests")
    markdown("bio")
    st.link_button(
        "Download CV",
        "https://docs.google.com/document/d/1VgZDnTwb6rSEfRq_3QUtteR8fhvRNxnaCvdt85iupIQ/edit?usp=sharing",
        type="primary",
    )


def publications():
    markdown("publications")


def main():
    local_css("styles.css")
    header()
    socials()
    about()
    # publications()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Adesh Kadambi",
        page_icon="files/logo.png",
    )
    main()
