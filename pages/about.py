"""About page shown when the user enters the application"""
import streamlit as st

def write():
    """Used to write the about page in the app.py file"""
    st.title("About Rohan Malhotra")
    st.markdown(
            """## Why Hire Me?
I am an aspiring Data Scientist and I am confident I would be a great fit for a Data Analytics/Scientist position. To 
know why, it is important to know more about me. Ever since I learned about Data Science I knew it would be the position
for me because I have always enjoyed solving issues using an analytical approach and am passionate about incorporating 
technology into my work. Data Science allows me to apply my analytical skills to solve real-world issues using many 
different tools to deal with data. Next, My experience in my previous positions has prepared me for this position 
by giving me the skills I need to work in a group setting, manage projects and quickly adapt to different situations.
Being in this field I know technology changes often and there will be new tools out which I will need to adapt to. 
From the technical standpoint, I believe I possess the technical skills needed for this position. I have learned and 
have had experience with many different tools which are used in the position. To learn more about what technical skills 
I have and how I have used them please refer to the skills and experience sections. In conclusion, I would be a great 
candidate due to my leadership qualities, technical skills, and most importantly my drive to finding a solution with 
any problem I am faced. To learn more about me please vist my website. 
""",
            unsafe_allow_html=True,
        )
if __name__ == "__main__":
    main()
