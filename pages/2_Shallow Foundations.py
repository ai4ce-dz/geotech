import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt 

st.set_page_config(page_title="AI4CE", page_icon=":toda:",layout="wide",initial_sidebar_state="auto")
st.title("NFS 2025")
st.subheader("Load-Settlement Behavior of Shallow Foundations on Sandy Soils Using Artificial Neural Networks")
#st.subheader("Load-settlement of shallow foundations in sandy soils")

st.write("Introducing an innovative approach, our AI application unveils a Hybrid Artificial Neural Networks and Mathematical model designed to predict the load-settlement behavior of shallow foundations in sandy soils. This method, meticulously crafted and rigorously validated, harnesses the power of 110 comprehensive full-scale loading tests on shallow foundations conducted in sand, coupled with cone penetration test (CPT) results. Published by Taylor & Francis in the Geomechanics and Geoengineering: An International Journal on April 29, 2020. Explore the details of our research, methodologies, and findings online at: ")
st.write("[Learn more>](https://doi.org/10.1080/17486025.2020.1755459)")

col1, col2 = st.columns([1, 1])  # Adjust the ratio as needed

with col1:
    geom=st.radio('Foundation Geometry',['Rectangular','Cercular'],horizontal = True) 
    mat=st.radio('Foundation Material',['Concrete','Steel'],horizontal = True) 
    B=st.number_input(label='foundation width')
    L = st.number_input('foundation length')
    D = st.number_input('foundation depth')
    qc = st.number_input('soil tip resistance qc')
    sbmax = 0.01*st.number_input('max value of settelement s/B')

    if geom=='rectangular':
        sh=0
    else :
        sh=1
    if mat=='Concrete':
        m=0
    else :
        m=1

    #st.button("calculate", type="primary")
    #st.button("Reset", type="primary")
    if st.button("calculate", type="primary"):

        x1=-0.51*m-0.35*sh+1.04*B/36+1.03*L/B+0.56*D/5-1.18
        x2=-0.79*m+0.94*sh+2.86*B/36+0.46*L/B+7.62*D/5-0.37
        n1=1/(1+np.exp(-x1))
        n2=1/(1+np.exp(-x2))
        qu=qc*(0.48*n1+0.12*n2+0.01)
        st.write("qu=",qu)
        st.write("sbmax=",sbmax)

        sb=np.arange(0,sbmax,sbmax/100)
        q=1000*qu*(1-np.exp(-3.393*(sb)**(2/3)))
        #st.table(sb)
        #st.write("q=",q)

        with col2:
            fig = plt.figure()
            pl=plt.plot(1000*sb,q)
            plt.title("Load-Settelement Curve")
            plt.ylabel("Load (kPa)")
            plt.xlabel("Settelement (mm)")
            plt.grid()
            qmax=max(q)*1.1
            sbmax=max(sb)*1.1*1000
            plt.axis((0, sbmax, 0, qmax))
            st.pyplot(fig)

# Sidebar with Contact Info
st.sidebar.header("📬 Contact Me")
st.sidebar.write("📧 Email: [a.aouadj@gmail.com](mailto:a.aouadj@gmail.com)")
st.sidebar.write("🔗 LinkedIn: [linkedin.com/in/abdelfatah-aouadj-6665b4127](https://linkedin.com/in/abdelfatah-aouadj-6665b4127)")