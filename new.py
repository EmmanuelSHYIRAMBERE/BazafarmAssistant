import streamlit as st
from streamlit import session_state
import time
import base64
import os
from vectors import EmbeddingsManager  
from chatbot import ChatbotManager     
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Function to display the PDF of a given file
def displayPDF(file):
    """Display a PDF file in the Streamlit app."""
    base64_pdf = base64.b64encode(file.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Data Analysis Functions
def generate_mock_data():
    """Generate mock data for farm analytics."""
    dates = [(datetime.now() - timedelta(days=x)).strftime('%Y-%m-%d') for x in range(30)]
    dates.reverse()
    
    data = {
        'Date': dates,
        'Water_Level': np.random.uniform(60, 90, 30),  # Water level in percentage
        'Soil_Temperature': np.random.uniform(20, 30, 30),  # Temperature in Celsius
        'Soil_Moisture': np.random.uniform(30, 70, 30),  # Moisture in percentage
        'Soil_pH': np.random.uniform(6.0, 7.5, 30),  # pH levels
        'Nitrogen': np.random.uniform(150, 250, 30),  # NPK values in ppm
        'Phosphorus': np.random.uniform(100, 200, 30),
        'Potassium': np.random.uniform(180, 280, 30)
    }
    return pd.DataFrame(data)

def render_data_analysis():
    """Render the data analysis dashboard."""
    st.title("📊 Farm Data Analysis")
    
    df = generate_mock_data()
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Real-time Metrics",
        "🌡️ Temperature Analysis", 
        "💧 Water Metrics",
        "🧪 Soil Analysis"
    ])
    
    with tab1:
        st.header("Real-time Farm Metrics")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            current_temp = df['Soil_Temperature'].iloc[-1]
            st.metric(
                label="Soil Temperature", 
                value=f"{current_temp:.1f}°C",
                delta=f"{current_temp - df['Soil_Temperature'].iloc[-2]:.1f}°C"
            )
        
        with col2:
            current_moisture = df['Soil_Moisture'].iloc[-1]
            st.metric(
                label="Soil Moisture", 
                value=f"{current_moisture:.1f}%",
                delta=f"{current_moisture - df['Soil_Moisture'].iloc[-2]:.1f}%"
            )
        
        with col3:
            current_ph = df['Soil_pH'].iloc[-1]
            st.metric(
                label="Soil pH", 
                value=f"{current_ph:.1f}",
                delta=f"{current_ph - df['Soil_pH'].iloc[-2]:.1f}"
            )
    
    with tab2:
        st.header("Temperature Analysis")
        fig_temp = px.line(
            df, 
            x='Date', 
            y='Soil_Temperature',
            title='Soil Temperature Trend'
        )
        fig_temp.update_layout(yaxis_title="Temperature (°C)")
        st.plotly_chart(fig_temp, use_container_width=True)
        
        fig_temp_dist = px.histogram(
            df, 
            x='Soil_Temperature',
            title='Temperature Distribution',
            nbins=20
        )
        st.plotly_chart(fig_temp_dist, use_container_width=True)
    
    with tab3:
        st.header("Water Metrics")
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=df['Water_Level'].iloc[-1],
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Current Water Level (%)"},
            gauge={
                'axis': {'range': [None, 100]},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 80], 'color': "gray"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ))
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        fig_water = px.line(
            df, 
            x='Date', 
            y='Water_Level',
            title='Water Level Trend'
        )
        fig_water.update_layout(yaxis_title="Water Level (%)")
        st.plotly_chart(fig_water, use_container_width=True)
    
    with tab4:
        st.header("Soil Analysis")
        npk_data = pd.melt(
            df,
            id_vars=['Date'], 
            value_vars=['Nitrogen', 'Phosphorus', 'Potassium'],
            var_name='Nutrient',
            value_name='Level'
        )
        
        fig_npk = px.line(
            npk_data, 
            x='Date', 
            y='Level', 
            color='Nutrient',
            title='NPK Levels Over Time'
        )
        fig_npk.update_layout(yaxis_title="Concentration (ppm)")
        st.plotly_chart(fig_npk, use_container_width=True)
        
        fig_ph = px.line(
            df, 
            x='Date', 
            y='Soil_pH',
            title='Soil pH Trend'
        )
        fig_ph.update_layout(yaxis_title="pH Level")
        st.plotly_chart(fig_ph, use_container_width=True)

def main():
    """Main application function."""
    # Initialize session_state variables
    if 'temp_pdf_path' not in st.session_state:
        st.session_state['temp_pdf_path'] = None

    if 'chatbot_manager' not in st.session_state:
        st.session_state['chatbot_manager'] = None

    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

    # Set page configuration
    st.set_page_config(
        page_title="BAZAFARM TECHNOLOGY",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Sidebar
    with st.sidebar:
        st.image("logo.png", use_column_width=True)
        st.markdown("### 🌱 Your Smart Farming Assistant")
        st.markdown("---")
        
        menu = ["🏠 Home", "🤖 Farm Assistant", "📊 Data Analysis", "📧 Contact"]
        choice = st.selectbox("Navigate", menu)

    # Page Router
    if choice == "🏠 Home":
        st.title("🌾 BAZAFARM TECHNOLOGY")
        st.markdown("""
        Welcome to **BAZAFARM TECHNOLOGY** by STES GROUP Ltd! 🚀

        BAZAFARM is a solar-powered IoT device that revolutionizes farming:

        - **Real-time Monitoring**: Measure water level, soil temperature, and fertility.
        - **Smart Decision-Making**: Access data on your mobile, tablet, or PC via Internet.
        - **Optimized Farming**: Achieve high crop yields with precise environmental data.
        - **Weather Forecasts**: Stay informed about upcoming weather conditions.

        Enhance your farming experience with BAZAFARM! 🌱🌞
        """)

    elif choice == "🤖 Farm Assistant":
        st.title("🤖 Farm Assistant Interface")
        st.markdown("---")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.header("📂 Upload A PDF File Which contains Farm Data")
            uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
            if uploaded_file is not None:
                st.success("📄 Farm Data Uploaded Successfully!")
                st.markdown(f"**Filename:** {uploaded_file.name}")
                st.markdown(f"**File Size:** {uploaded_file.size} bytes")
                
                st.markdown("### 📖 Data Preview")
                displayPDF(uploaded_file)
                
                temp_pdf_path = "temp.pdf"
                with open(temp_pdf_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                st.session_state['temp_pdf_path'] = temp_pdf_path

        with col2:
            st.header("🧠 Data Processing")
            create_embeddings = st.checkbox("✅ Process Farm Data")
            if create_embeddings:
                if st.session_state['temp_pdf_path'] is None:
                    st.warning("⚠️ Please upload farm data first.")
                else:
                    try:
                        embeddings_manager = EmbeddingsManager(
                            model_name="BAAI/bge-small-en",
                            device="cpu",
                            encode_kwargs={"normalize_embeddings": True},
                            qdrant_url="http://localhost:6333",
                            collection_name="vector_db"
                        )
                        
                        with st.spinner("🔄 Processing farm data..."):
                            result = embeddings_manager.create_embeddings(st.session_state['temp_pdf_path'])
                            time.sleep(1)
                        st.success(result)
                        
                        if st.session_state['chatbot_manager'] is None:
                            st.session_state['chatbot_manager'] = ChatbotManager(
                                model_name="BAAI/bge-small-en",
                                device="cpu",
                                encode_kwargs={"normalize_embeddings": True},
                                llm_model="llama3.2:3b",
                                llm_temperature=0.7,
                                qdrant_url="http://localhost:6333",
                                collection_name="vector_db"
                            )
                        
                    except Exception as e:
                        st.error(f"An error occurred: {e}")

        with col3:
            st.header("💬 Chat with Farm Assistant")
            
            if st.session_state['chatbot_manager'] is None:
                st.info("🌱 Please upload farm data and process it to start chatting.")
            else:
                for msg in st.session_state['messages']:
                    st.chat_message(msg['role']).markdown(msg['content'])

                user_input = st.chat_input("Ask about your farm data...")
                if user_input:
                    st.chat_message("user").markdown(user_input)
                    st.session_state['messages'].append({"role": "user", "content": user_input})

                    with st.spinner("🤖 Analyzing..."):
                        try:
                            answer = st.session_state['chatbot_manager'].get_response(user_input)
                            time.sleep(1)
                        except Exception as e:
                            answer = f"⚠️ An error occurred while analyzing your farm data: {e}"
                    
                    st.chat_message("assistant").markdown(answer)
                    st.session_state['messages'].append({"role": "assistant", "content": answer})

    elif choice == "📊 Data Analysis":
        render_data_analysis()

    elif choice == "📧 Contact":
        st.title("📬 Contact STES GROUP Ltd")
        st.markdown("""
        We'd love to hear from you! For any questions about BAZAFARM TECHNOLOGY, please reach out.

        - **Email:** [info@stesgroup.rw](mailto:info@stesgroup.rw) ✉️
        - **Website:** [STES GROUP Ltd](https://www.stesgroup.rw) 🌐

        If you'd like to request a feature or report an issue with your BAZAFARM device, please contact our support team.
        """)

    # Footer
    st.markdown("---")
    st.markdown("© 2024 BAZAFARM TECHNOLOGY by STES GROUP Ltd. All rights reserved. 🛡️")

if __name__ == "__main__":
    main()