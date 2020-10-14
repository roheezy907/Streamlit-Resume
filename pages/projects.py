"""Projects page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the page in the app.py file"""
    st.title("Experiences - :male-construction-worker: ")
    st.markdown(
            """### **Student Assistant - Data Quality and Engineering Control** | California Energy Commission | 10/2019 - present

- Assisted with many data-related tasks associated with the Commercial End Use Survey (CEUS) project which aimed to increase the accuracy of the department’s ability to forecast energy consumption and demand in California
- Performed statistical and energy related analyses on CEUS survey data in Python to find patterns and trends within the data which could be used by the engineering team when constructing the forecast model
- Automated quality checks for incoming energy data in R to remove inaccurate observations which enhanced the quality control process as it significantly decreased the time it takes to clean the data by 50%
- Collaborated with two other interns to generate reports/dashboards in Tableau to present ideas and suggestions to help refine CEUS data collection and analytical techniques
- **Tools**: Python, R, Excel, VBA, Tableau, SQL

            
### **Research Data Analyst** | Center for Water-Energy Efficiency | 04/2020 - 09/2020
- Managed data pre-processing projects in Python that seek to model energy demand flexibility in the water sector and improve measurements of carbon emission from the electricity sector
- Created original datasets in Python using Pandas (Numpy, Pandas) to scrape, clean, reformat, and merge data from multiple sources • 
- Applied regex and fuzzy matching techniques in Python to correctly identify 80% of the duplicates
- **Tools**: Python, Excel

### **Data Science/Machine Learning Intern** | Hindsight Technology Solutions | 09/2019 - 01/2020

- Analyzed multiple articles in Python to improve the company’s predictive model to tag entities present within an article 
- Scraped content of 100+ online website articles using Python (BeautifulSoup) to use as a sample to discover patterns which could be used to identify an entity 
- Led a team of 2 interns and performed word tokenization using Python (NLTK) to identify words and phrases which suggested the presence of an entity to be used in the model to identify an entity; repeated for multiple publishing partners
- **Tools**: Python, Excel

### **Campus Climate Analyst** | UC Davis | 04/2019 - 03/2020

- Assessed the needs of the UC Davis community in regard to issues surrounding racism, sexism, sexual assault, and other forms of discrimination and violence
- Conducted surveys and analyzed data in R to help create policies that address the needs of the UC Davis community around the aforementioned topics
- Met regularly with UC Davis Administration, California State Legislature members, and members of the community to advocate for marginalized communities on campus
- **Tools**: R, Excel

### **Data Analyst Intern** | Giving Garden | 06/2019 - 10/2019
- Web-scraped locations of the different parts of rice production in California using Python
- Analyzed datasets on rice in California acquired from USDA and summarized results through visualizations
- Created a R shiny web application which displays locations of the different parts of rice production in CA
- **Tools**: Python, Excel, R 

            

""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
