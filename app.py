import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container              



with stylable_container(
    key="header_classic",
    css_styles="""{
    background-color: #112639;
    color: white;
    font-family:roboto;
    padding: 10px;
    border-bottom: 2px solid #007bff;
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    z-index: 1000;
    }""",):      
        col1,col2=st.columns([2,2.5])
        with col1:
            
            st.write("""<b style="color: white; font-size: 42px">PredSAL</b>""",unsafe_allow_html=True)
            
        with col2:
            
            #############################################################################
            # menu options
            #############################################################################
            


            selected = option_menu(None, ["Home", "Predictor","Data Visuals", "Explored Results","Login/Signup"],  
                icons=['house', 'speedometer','table' ,'chat-left','person-circle'], 
                menu_icon="cast", default_index=0, orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#112639","border-radius": "0px","box-shadow": "none" ,"margin": "0px","border": "none","overflow": "hidden","padding-top":"50px"},
                    "icon": {"color": "white", "display": "block", "text-align": "center","border": "none","padding": "0px","font-size":"30px"},
                    "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "color": "white", "--hover-color": "rgba(255, 87, 51,0.5)","padding": "0px","border": "none"},
                    "nav-link-selected": {"background-color": "#ff6804", "color": "white", "display": "block"},
                    "nav-link-icon": {"display": "block", "text-align": "center"}
                }
            )