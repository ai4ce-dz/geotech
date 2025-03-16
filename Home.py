import streamlit as st

# Website Title

st.set_page_config(page_title="Dr. Abdelfattah Aouadj - Civil Engineering", layout="wide")

col1, col2 = st.columns([2, 1])  # Adjust the ratio as needed
with col2:
    st.image("profile.png", width=400, caption="Dr. Abdelfattah Aouadj")  # Adjust width as needed

with col1:
# Header
    #st.title("Dr. Abdelfattah Aouadj – Geotechnical Engineering & AI in Civil Engineering")
    st.title("Welcome to My Official Website")

    st.text("I'm Abdelfattah Aouadj – PhD Civil Engineering. Here, you’ll find my research, software developments, and insights on geotechnical engineering and artificial intelligence applications in civil engineering.")



    # About Me
    # st.subheader("About Me")
    # st.write("""
    # - **Name:** Dr. Abdelfattah Aouadj  
    # - **Expertise:** Geotechnical Engineering, AI in Civil Engineering, Structural Analysis  
    # - **Education:**
    # - 🏛 **PhD in Civil Engineering** – University of Blida 1, Algeria (2022)  
    # - 📚 **Magister in Civil Engineering** – National Polytechnic School of Algiers (2012)  
    # - 🎓 **Civil Engineering Degree** – National Polytechnic School of Algiers (2008)  
    # - **Professional Experience:**  
    # - 🏗 **Agency Director at Technical Control of Construction CTC El Oued, Algeria** (2023 - Present)              
    # - 🏗 **Senior Control Engineer at CTC EL Oued** (2013 - 2023)  
    # - 🏗 **Control Engineer at Technical Control of Hydraulic Construction CTH** (2010 - 2013)  
    # - Expertise in geotechnical testing, foundation design, and construction control.  
    # - **Technical Skills:**  
    # - 🖥 Structural Analysis Software : SAP2000, Robot Structural Analysis  
    # - 🖥 Geotechnical Software: Plaxis, Geo5  
    # - 🤖 AI & Programming: MATLAB, VB.NET, Python  
    # """)

    
    # Contact Section
    st.subheader("📩 Contact Me")
    st.write("Feel free to reach out for collaborations or inquiries.")

    st.markdown(
        """
        - 📧 **Email:** [a.aouadj@gmail.com](mailto:a.aouadj@gmail.com)  
        - 🔗 **LinkedIn:** [linkedin.com/in/abdelfatah-aouadj-6665b4127](https://linkedin.com/in/abdelfatah-aouadj-6665b4127)  
        """
    )

# Footer
st.write("---")
st.write("© 2024 Dr. Abdelfattah Aouadj | Geotechnical Engineering & AI Applications")

