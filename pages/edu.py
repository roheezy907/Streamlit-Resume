"""Edu page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Education :books:")
    st.markdown(
            """### University of California, Davis
**Bachelor of Science in Statistics (emphasis on Data Science)** | June 2020 |GPA 3.34/4.0
** Activities/Societies **: Board Member of UC Davis' Sports Analytics Club


**Davis Courses** \n
- Probability Theory\n
- Statistical Data Science \n
- Data and Web Technologies for Data Science \n
- Introduction to Mathematical Statistics  \n
- Big Data and High Performance Statistical Computing \n
- Applied Linear Algebra \n
- Multivariate Data Analysis \n
- Analysis of Categorical Data \n
- Data Sense and Exploration \n
- Regression Analysis \n
- Analysis of Variance \n
- Statistical Learning \n


### Distance Learning

**Intermediate Python** | Data Camp | [Credential](https://www.datacamp.com/statement-of-accomplishment/course/feda44c27a6676e1852a141ba3e07513984b7410) \n


**Introduction to Tableau** | Data Camp | [Credential](https://www.datacamp.com/statement-of-accomplishment/course/47fa8f41c6f8443e7ded) \n


**The Ultimate Hands-On Hadoop** | Udemy | [Credential](https://www.udemy.com/certificate/UC-82ee628f-fc36-4402-b7ca-5a5d85e0a602/)\n

**The Complete SQL Bootcamp** | Udemy | [Credential](https://www.udemy.com/certificate/UC-82353f60-a8ed-4477-9640-1d8f4d671c0c/) \n


""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
