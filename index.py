from pathlib import PurePath

import streamlit as st


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def markdown(filename: str):
    with open(PurePath(__file__).parent / "markdown" / f"{filename}.md", "r") as f:
        st.markdown(f.read())


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
    st.image("files/logo.png", width=100)
    st.title("Hi, I'm Adesh Kadambi!")
    socials()
    markdown("about-me")
    st.image("files/interests.png")
    markdown("research-interests")
    markdown("bio")
    st.download_button(
        label="Download CV",
        data="files/kadambi_cv.pdf",
        file_name="kadambi_cv.pdf",
        type="primary",
    )


def main():
    local_css("styles.css")
    about()


if __name__ == "__main__":
    st.set_page_config(
        page_title="Adesh Kadambi",
        page_icon="files/logo.png",
    )
    main()
