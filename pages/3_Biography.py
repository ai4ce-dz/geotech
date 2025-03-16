import streamlit as st

col1, col2 = st.columns([1, 2])  # Adjust the ratio as needed
with col1:
    st.image("profile.png", width=200, caption="Dr. Abdelfattah Aouadj")  # Adjust width as needed

with col2:
    st.title("Biography")
    st.text("Dr. Abdelfattah Aouadj is a civil engineer specializing in geotechnical engineering, structural analysis, and artificial intelligence applications in construction. He has experience in foundation design, in-situ soil testing, and geotechnical modeling ")
    st.text("He is currently the Agency Director at CTC El Oued, where he oversees technical and administrative operations, ensuring compliance with industry standards. Previously, as a Senior Control Engineer at CTC, he was responsible for reviewing engineering designs and supervising site work for industrial and infrastructure projects, including power stations, university buildings, hospitals, and hydraulic structures.")
    st.text("Dr. Aouadj has also worked on developing geotechnical software, including NFS 2020, which predicts load-settlement behavior of shallow foundations, and NLPILE 2022, which analyzes lateral pile behavior. His research on artificial intelligence applications in geotechnical engineering has been published in scientific journals.")    
    st.text("He holds a PhD in Civil Engineering from the University of Blida 1, with research focused on AI-based methods for soil-structure interaction. He has also conducted research and training at the Technical University of Darmstadt in Germany.")
    st.text("Dr. Aouadj continues to work in geotechnical engineering, combining technical expertise with research and software development to support construction analysis and design.")           

    # Research & Publications
    st.subheader("📖 Research & Publications")
    st.write("Here are some of my research contributions:")
    st.write("📄 **Prediction of Foundation Bearing Capacity for Geosynthetic-Reinforced Soil Using Artificial Neural Networks** – SNGC 2024")
    st.write("[📄 **Artificial Neural Network for Predicting the Modulus of Subgrade Reaction on Sandy Soils** – ICCEE 2023](https://www.researchgate.net/publication/376550928_Artificial_Neural_Network_for_Predicting_the_Modulus_of_Subgrade_Reaction_on_Sandy_Soils)")
    st.write("[📄 **Méthode pratique de construction d'une courbe de chargement des fondations superficielles dans le sable** – SNGC 2024>](https://www.researchgate.net/publication/360901167_Methode_pratique_de_construction_d'une_courbe_de_chargement_des_fondations_superficielles_dans_le_sable)")
    st.write("[📄 **CPT-based method using hybrid artificial neural network and mathematical model to predict the load-settlement behaviour of shallow foundations.** – Geomechanics and Geoengineering, 2022>](https://doi.org/10.1080/17486025.2020.1755459)")
    st.write("[📄 **Load-Settlement behavior of shallow foundations - Numerical modelling by the Artificial Neural Network technique** – ASEC 2018>](https://www.researchgate.net/publication/341070890_LOAD-SETTLEMENT_BEHAVIOR_OF_SHALLOW_FOUNDATIONS_-NUMERICAL_MODELLING_BY_THE_ARTIFICIAL_NEURAL_NETWORK_TECHNIQUE)")
    st.write("[📄 **Book: Essai de Pénétration au Carottier SPT - Procédure d'essai et calcul des fondations** (2024) >](https://www.researchgate.net/publication/380466709_Essai_de_Penetration_au_Carottier_SPT_-_Procedure_d'essai_et_calcul_des_fondations)")

    publications = [
        "📄 **Prediction of Foundation Bearing Capacity for Geosynthetic-Reinforced Soil Using Artificial Neural Networks** – SNGC 2024",         
        "📄 **Artificial Neural Network for Predicting the Modulus of Subgrade Reaction on Sandy Soils** – ICCEE 2023",
        "📄 **Méthode pratique de construction d'une courbe de chargement des fondations superficielles dans le sable** – SNGCTP 2022",
        "📄 **CPT-based method using hybrid artificial neural network and mathematical model to predict the load-settlement behaviour of shallow foundations.** – Geomechanics and Geoengineering, 2022",
        "📄 **Load-Settlement behavior of shallow foundations - Numerical modelling by the Artificial Neural Network technique** – ASEC 2018",
        "📖 **Book:** *Essai de Pénétration au Carottier SPT - Procédure d’essai et calcul des fondations* (2024)"
        ]
   # for pub in publications:
   #         st.markdown(f"- {pub}")


    st.subheader("🖥 Engineering Software Development")
    st.write("I have developed several engineering tools leveraging AI.")


    software = {
        "🔍 MORAKEB DEB 2020": "Expert system for concrete conformity control based on Algerian and European standards.",
        "🏗 NFS 2020": "AI-based tool for predicting shallow foundation behavior using CPT data.",
        "📊 NLPILE 2022": "Neural network model for predicting lateral pile behavior using CPT results."
    }
    
    st.subheader("MORAKEB DEB 2020")
    st.image("DEB.png", width=600, caption=" MORAKEB DEB 2020.")  # Adjust width as needed
    st.write("MORAKEB DEB 2020 is an expert system-based software designed for Concrete Conformity Control. It enables users to verify the compliance of concrete constituents—sand, gravel, water, and cement—with Algerian and European standards. Additionally, the software assesses concrete formulation and characteristic strength, taking into account environmental factors. Finally, it provides the option to generate and print a detailed control report.")
   
    st.subheader("🏗 NFS 2020")
    st.image("NFS.jpg", width=600, caption=" NFS 2020.")  # Adjust width as needed
    st.write("NFS 2020 is a software based on artificial neural networks to predict the load-settlement behavior of shallow foundations. the software allows to analyze the profile of cone penetration test (CPT), then calculate the bearing capacity and settlement of foundation.  The used method in this software is published in the scientific journal Geomechanics an Geoengineering by AOUADJ and BOUAFIA.")
   
    st.subheader("🏗 NLPILE 2022")
    st.image("NLPILE.jpg", width=600, caption=" NLPILE 2022.")  # Adjust width as needed
    st.write("NLPILE 2022 is a software based on artificial neural networks to predict the lateral behavior of free pile. Using the results of cone penetration test (CPT), the software predicts the lateral displacement of pile at soil surface. It calculates also the bending moments, pressures of soil and displacement along the pile. This software was developed using the results of 45 laterally loaded pile tests.")
   
   # for name, desc in software.items():
  #      st.subheader(name)
   #     st.write(desc)

# Sidebar with Contact Info
st.sidebar.header("📬 Contact Me")
st.sidebar.write("📧 Email: [a.aouadj@gmail.com](mailto:a.aouadj@gmail.com)")
st.sidebar.write("🔗 LinkedIn: [linkedin.com/in/abdelfatah-aouadj-6665b4127](https://linkedin.com/in/abdelfatah-aouadj-6665b4127)")