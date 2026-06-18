# Movie-Rating-Analysis
Movie Rating Analysis includes an interactive Streamlit web app that explores and visualizes Netflix Users Dataset. It combines Python, pandas, numpy,Streamlit,Jupyter Notebook and Plotly to deliver clear charts, descriptive statistics, and insights in a user‑friendly dashboard for quick analysis.

# Project Structure
-**Notebooks/**
  -'Data Cleaning and EDA.ipynb' -Notebook for preprocessing and exploratory data analysis.
  -'Dashboard.py' -Main Streamlit app.
-**Data/**
  -'Raw/' -Original Dataset.
  -'Cleaned/' -Cleaned Dataset after Data Cleaning and Final Dataset after Feature Engineering.
-'README.md' -Documentation and setup guide.
-'requirements.txt' -Dependencies for reproducibility

## Features
- 📊 Data cleaning and preprocessing pipeline  
- 🔎 Exploratory Data Analysis (EDA) notebook with descriptive statistics  
- 🎨 Interactive Streamlit dashboard (`Dashboard.py`)  
- 📈 Visualizations of rating distributions, trends, and genre comparisons  
- 🖥️ Clear separation of raw vs cleaned datasets for reproducibility

## Author
Developed By Cynthia Mueni
Github Profile Link: https://github.com/thea09-cpu

## Setup Instructions
Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/Movie-Rating-Analysis.git
cd Movie-Rating-Analysis
pip install -r requirements.txt

## Run the Streamlit App
streamlit run Notebooks/Dashboard.py
