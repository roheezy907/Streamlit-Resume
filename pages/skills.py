"""Skills page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Skills :hammer_and_wrench:")
    st.markdown(
            """## Languages
- R
- Python
- SQL 
- VBA

## Platforms and Libraries
- **MS Office** - Excel, Powerpoint, Project, Word
- **Python** - Pandas, Numpy, Skicit Learn,Scipy, NLTK, Streamlit, Plotly, Matplotlib, Seaborn, etc.
- **R** - Shiny, Dplyr, GGplot2
- **SQL** - PostgreSQL
- Tableau
- PowerBI
- Qlik View
- JIRA, Confluence

## Analytical Skills
- Statistical Data Analysis
- Data Wrangling
- Hypothesis Testing
- Machine Learning
- Natural Language Processing
- Web Scraping

## AWS Stack
- EC2

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
