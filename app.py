### Main page for streamlit resume
import streamlit as st
import pages.about
import pages.skills
import pages.projects
import pages.edu
import pages.recommendations

import resources.ast as ast

PAGES = {
    "About": pages.about,
    "Education" : pages.edu,
    "Skills": pages.skills,
    "Experiences": pages.projects,
}

def main():
    """Main function of App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    
    with st.spinner(f"Loading {selection} ..."):
        ast.write_page(page)

    st.sidebar.title("Hire Me")
    st.sidebar.info(
        """
        If you are looking to hire a Data Scientist/Data Analyst, 
        [email me](mailto:rohanmalhotra010798@gmail.com) or reach out 
        to me on [LinkedIn](https://www.linkedin.com/in/rohan-malhotra-270a86172/)
""")
    st.sidebar.title("Additional Info")
    st.sidebar.info(
        "This an interactive streamlit app completely created with Python's latest library **streamlit**. "
        "The template of this Streamlit app was made by Abhishek Gupta and feel free to check out his  "
        "[source code](https://github.com/alphadatagamma/Streamlit-Resume-App) here."

)

if __name__ == "__main__":
    main()
